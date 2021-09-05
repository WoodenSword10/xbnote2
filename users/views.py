import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User_info
import hashlib
# Create your views here.
def first_view(request):
    return render(request, 'index/index.html')

def user_center_view(request):
    if request.method == 'GET':
        username = request.session.get('username')
        user = User_info.objects.get(username=username)
        dic ={}
        dic['user'] = user
        return render(request, 'users/个人中心.html', dic)
    elif request.method == 'POST':
        # 方式1
        # a_file = request.FILES['myfile']
        # print('上传文件名是：', a_file.name)
        # filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        # with open(filename,'wb') as f:
        #     data = a_file.file.read()
        #     f.write(data)
        # return  HttpResponse('接收文件：' + a_file.name + '成功')
        # 方式2
        a_file = request.FILES['myfile']
        username = request.session.get('username')
        user = User_info.objects.get(username=username)
        user.img = a_file
        user.save()
        return HttpResponseRedirect('/users/user_center')

def register_view(request):
    # get请求返回注册页面
    if request.method == 'GET':
        return render(request, 'users/注册.html')
    # POST请求处理数据，实现用户注册
    elif request.method == 'POST':
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        check_password = request.POST['check_password']
        # 两次密码校验
        if user_password != check_password:
            return HttpResponse('密码不一致')
        # 用户名重复检查
        old_users = User_info.objects.filter(username=user_name)
        if old_users:
            return HttpResponse('用户名已注册')
        # 密码明文处理。使用md5方式
        m = hashlib.md5()
        m.update(user_password.encode())
        password_m = m.hexdigest()
        # 为了避免并发性错误，使用try隐藏重复性插入错误
        try:
            user = User_info.objects.create(username=user_name, password=password_m)
        except Exception as e:
            print('--create user error %s'%(e))
            return HttpResponse('用户名已注册')
        #免登录一天
        request.session['username'] = user_name
        request.session['uid'] = user.id
        return HttpResponseRedirect('/index')

def login_view(request):
    if request.method == 'GET':
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('已登录')
            HttpResponseRedirect('/index')
        c_username = request.COOKIES.get('username')
        c_uid =request.COOKIES.get('uid')
        if c_username and c_uid:
            # 回写session
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            HttpResponseRedirect('/index')
        return render(request, 'users/登入.html')
    elif request.method == 'POST':
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        # 用户名查找
        try:
            user = User_info.objects.get(username=user_name)
        except Exception as e:
            print('--login user error %s'%(e))
            return HttpResponse('您的用户名或密码错误')
        # 比对密码
        m = hashlib.md5()
        m.update(user_password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('您的用户名或密码错误')
        # 记录会话状态
        request.session['username'] = user_name
        request.session['uid'] = user.id
        # 判断用户是否点选了‘记住用户名’
        # resp = HttpResponse('登录成功')
        resp = HttpResponseRedirect('/index')
        if 'remember' in request.POST:
            # 注意存不了中文，需要编码
            resp.set_cookie('username', user_name.encode(), 3600*24*3)
            resp.set_cookie('uid', user.id, 3600*24*3)
        return resp

def quit_view(request):
    # 删除session
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']
    resp = HttpResponseRedirect('/index')
    # 删除cookies
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp