"""xbNote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.first_view),
    # admin后台
    path('admin/', admin.site.urls),
    # user_space应用路由
    path('users/', include('users.urls')),
    # index应用路由
    path('index/', include('index.urls')),
    # note应用路由
    path('note/', include('note.urls')),
    # 127.0.0.1:8000/test_cache
    # 测试中间件
    path('test_cache', views.test_cache_view),
    # 127.0.0.1:8000/test
    # 用于测试访问限制
    path('test', views.test_view),
    # 127.0.0.1:8000/email_test
    # 用于测试邮箱
    path('email_test', views.email_test_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
