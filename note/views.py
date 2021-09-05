import csv

from django.core.paginator import Paginator
from django.shortcuts import render
from users.models import User_info
from .models import Note
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def check_login(fn):
    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            # 检查COOKIES
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/users/login')
            else:
                # 回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return  wrap

@check_login
def index_view(request):
    if request.method == 'GET':
        user = User_info.objects.get(username=request.session.get('username'))
        page_num = request.GET.get('page',1)
        notes = Note.objects.filter(user=user, is_active=False)
        paginator = Paginator(notes, 2)
        c_page = paginator.page(int(page_num))
        return render(request, 'note/笔记.html', locals())
    if request.method == 'POST':
        title = request.POST['title']
        classify = request.POST['classify']
        content = request.POST['content']
        user = User_info.objects.get(username=request.session.get('username'))
        note = Note.objects.create(title=title, classify=classify, content=content, user=user)
        return HttpResponseRedirect('/note/center')

def delete_view(request, note_id):
    try:
        note = Note.objects.get(id=note_id, is_active=False)
        note.is_active = True
        note.save()
    except Exception as e:
        print('删除出错%s'%(e))
        return HttpResponseRedirect('/note/center')
    return HttpResponseRedirect('/note/center')

def download_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mynote.csv"'
    user = User_info.objects.get(username=request.session.get('username'))
    notes = Note.objects.filter(user=user, is_active=False)
    writer = csv.writer(response)
    writer.writerow(['title','classify','content'])
    for note in notes:
        writer.writerow([note.title,note.classify,note.content])
    return response

def download_page_view(request):
    page_num = request.GET.get('page', 1)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="page_%s_note.csv"'%(page_num)
    user = User_info.objects.get(username=request.session.get('username'))
    notes = Note.objects.filter(user=user, is_active=False)
    paginator = Paginator(notes, 2)
    c_page = paginator.page(int(page_num))
    writer = csv.writer(response)
    writer.writerow(['title', 'classify', 'content'])
    for note in c_page:
        writer.writerow([note.title, note.classify, note.content])
    return response