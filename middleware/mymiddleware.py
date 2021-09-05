import re
import traceback
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.core import mail
from django.conf import settings

class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print('MyMW process_request do ---')
        pass

    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('MyMW process_views do ---')
        pass

    def process_response(self,request, response):
        print('MyMW process_response do ---')
        return response


class VisitLimit(MiddlewareMixin):
    visit_times = {}
    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info
        if not re.match('^/test', path_url):
            return
        times = self.visit_times.get(ip_address, 0)
        print('ip', ip_address, '已经访问', times)
        if times < 5:
            self.visit_times[ip_address] = times+1
            return
        return HttpResponse('您已经访问过' + str(times) +'次，访问被禁止')

class ExceptionMW(MiddlewareMixin):
    # 收集报错消息并发送邮件
    def process_exception(self, request, exception):
        print(traceback.format_exc())
        mail.send_mail(subject='xbNote服务器报错',message=traceback.format_exc(),
                       from_email='1205793031@qq.com', recipient_list=settings.EX_EMAIL)
        return HttpResponse('抱歉，当前网页有点忙')