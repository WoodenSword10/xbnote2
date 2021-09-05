from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import  cache_page
import time

def first_view(request):
    return render(request, 'index/index.html')

@cache_page(15)
def test_cache_view(request):
    print(' views do ---')
    t = time.time()
    return HttpResponse('t is %s'%(t))

def test_view(requset):
    return HttpResponse('本网页仅能访问5次')

def email_test_view(request):
    a
    return HttpResponse('EMAIL TEST')