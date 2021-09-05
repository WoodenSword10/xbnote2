1. 组件
    基本配置文件/路由文件
    模型层（M）/模板层（T）/视图层（V）
    Cookies和Session
    分页及发邮件
    Admin管理后台
2. 用途（HTTP请求和响应）
    网站
    微信公众号
    小程序后端开发
    人工智能平台融合
3. linux系统中的使用
    安装Django——sudo pip3 install django
    在想要的目录下打开终端执行django-admin startproject 项目名， 即可创建出对应项目文件夹

    启动服务（测试开发阶段）
    1. 终端cd进入到项目文件夹
    2. 进入到项目文件夹后，执行python3 manage.py runserver 启动django服务
    【注：该启动方式下，Django在前台启动服务，默认监听8000端口】
    3. 浏览器访问http://127.0.0.1:8000可看到django的启动页面
    【注：如果想要更换端口，则可以用python3 manage.py runserver 端口号】
    4. 关闭服务
        方式1： 在runserver启动终端下执行Ctrl + c
        方式2： 在其他终端下
            执行sudo lsof -i:8000  查询出django的进程id
            执行kill -9 对应的django进程id
4. 基础结构解析
    1. manage.py 包含项目管理的子命令
    2. 项目同名文件夹
        1. __init__:python包的初始化文件
        2. wsgi.py：web服务网关的配置文件——django正式启动时，需要该文件
        3. urls.py:项目的主路由配置——HTTP请求进入Django时，优先调用该文件
        4. settings.py：项目的配置文件——包含项目启动时需要的配置
5. settings.py
    配置项分为 公有配置 和 自定义配置
    配置项格式   BASE_DIR = 'XXXX'
    【注：名字一定为大写】
    公有配置——django官方提供的基础配置
6. URL
    定义：即统一资源定位符Uniform Resource Locator
    作用：用来表示互联网上某个资源的地址
    URL的一般语法格式为（注：[]表示其中的内容可省略）
        protocol://hostname[:port]/path[?query][#fragment]
        protocol:协议
            http 通过HTTP访问该资源。格式 http://
            https 通过安全的HTTPS访问该资源 格式 https://
            file 资源是本地计算机上的文件 格式：file://
        hostname:主机名
            指存放资源的服务器的域名系统（DNS）主机名、域名或IP地址
        port：端口
            整数，可选，省略时使用方案的默认端口
            各种传输协议都有默认的端口号，如http的默认端口为80
        path:路由地址
            由零或多个‘/’符号隔开的字符串，一般用来表示主机上的一个目录或文件地址，路由地址决定了服务器端如何处理这个请求
        query：查询
            可选，用于给动态网页传递参数，可有多个参数，用“&”符号隔开，每个参数的名和值用‘=’符号隔开。
        fragment：信息片段
            字符串，用于指定网络资源中的片段，

    处理URL请求
        浏览器地址栏 - > http://127.0.0.1:8000/page/2003/
        Django从配置文件中根据ROOT_URLCONF找到主路由文件；默认情况下，该文件在项目同名目录下的urls.py中
        django加载主路由文件中的urlpatterns变量【包含很多路由的数组】
        依次匹配urlpaterns中的path，匹配到第一个合适的中断后续匹配
        匹配成功，调用对应的视图函数处理请求，返回响应
        匹配失败，返回404响应

    视图函数
        是用于接收一个浏览器请求（HttpRequest对象）并通过HttpResponse对象返回响应的函数。此函数可以接收浏览器请求并根据业务逻辑返回相应的响应内容给浏览器。
        语法：
            def xxx_view(request[,其他参数...])：
                return HttpResponse对象

7. 路由配置 path
    path（）函数
    导入： from django.urls import path
    语法： path(route,views,name=None)
    参数：
        route： 字符串类型，匹配的请求路径
        views： 指定路径所对应的视图处理函数的名称
        name：  为地址起别名，在模板中地址反向解析时使用

    path转换器
        语法：<转换器类型：自定义名>
        作用：若转换器类型匹配到对应类型的数据，则将数据按照关键字传参的方式传递给视图函数
        转换器类型               作用                      样例
        str             匹配除了‘/‘之外的非空字符串         /<str:username>匹配/wula
        int             匹配0或者任何正整数，返回一个int     /<int:page>匹配/<100>
        slug            匹配任意由ASCII字母或数字           /<slug:sl>匹配/<this-is-django>
                        以及连字符和下划线组成的短标签
        path            匹配非空字段，包括路径分隔符‘/’       /<path:ph>匹配/</v1/fsd/a/v/vb>

    re_path()
        re_path()函数
            在url的匹配过程中可以使用正则表达式进行精确匹配
            语法：
                re_path(reg,view,name=xxx)
                正则表达式为命名分组模式（?p<name>pattern）；匹配提取参数后用关键字传承方式传递给视图函数

8. 请求和响应
    请求是指浏览器端通过HTTP协议发送给服务器端的数据
    响应是指服务器端接收到请求后做相应的处理后再回复给浏览器端的数据

    请求样例
        起始行
        请求头
        请求体

    请求中的方法
        根据HTTP标准，HTTP请求可以使用多种请求方法
        HTTP1.0定义了三种请求方法：GET,POST和HEAD方法（最常用）
        HTTP1.1新增了五种请求方法：OPTIONS,PUT,DELETE,TRACE和CONNECT方法

        GET:请求指定的页面信息，并返回实体主体
        HEAD：类似于GET请求，只不过返回的响应中没有具体的内容，用于获取报头
        POST：向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据
              被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改
        PUT： 从客户端向服务器传送的数据取代指定的文档的内容
        DELETE：请求服务器删除指定的页面
        CONNECT： HTTP1.1协议中预留给能够连接改为管道方式的代理服务器
        OPTIONS： 允许客户端查看服务器的性能
        TRACE：回显服务器受到的请求，主要用于测试或诊断

    django中的请求
        请求在django中实则就是视图函数的第一个参数，即HttpRequest对象
        django接收到HTTP协议的请求后，会根据请求数据报文创建HttpRequest对象
        HttpRequest对象通过属性描述了请求的所有相关信息

        path_info：URL字符串
        method：字符串，表示HTTP请求方法，常用值：GET、POST
            GET: QueryDict查询字典的对象，包含get请求方式的所有数据
            POET: QueryDict查询字典的对象，包含post请求方式的所有数据
        FILES:类似于字典的对象，包含所有的上传文件信息
        COOKIES：python字典，包含所有的cookie，键和值都为字符串
        session：类似于字典的对象，表示当前的会话
        body：字符串，请求体的内容（POST或PUT）
        scheme：请求协议（‘http'/'https'）
        request.get_full_path()：请求的完整路径
        request.META：请求中的元数据（消息头）
            - request.META['REMOTE_ADDR']：客户端IP地址

    响应
        起始行
        响应头
        响应体

    响应状态码
        常见的HTTP状态码
            -200    请求成功
            -301    永久重定向 资源（网页等）被永久转移到其他URL
            -302    临时重定向
            -404    请求的资源（网页等）不存在
            -500    内部服务器错误
        HTTP状态码由三个十进制数字组成，第一个十进制数字定义了状态码的类型，后两个数字没有分类的作用。HTTP状态码共分为5种
            1**     信息，服务器收到请求，需要请求者继续执行操作
            2**     成功，操作被成功接收并处理
            3**     重定向，需要进一步的操作以完成请求
            4**     客户端错误，请求包含语法错误或无法完成请求
            5**     服务器错误，服务器在处理请求的过程中发生了错误

        构造函数格式
            HttpResponse(content=响应体，content_type=响应体数据类型，status=状态码)
            作用：向客户端浏览器返回响应，同时携带响应体内容
            参数：
                content:表示返回的内容
                status_code:返回的HTTP响应状态码（默认为200）
                content_type:指定返回数据的MIME类型（默认为’text/html'）。浏览器会根据这个属性，来显示数据。
                             如果是text/html，那么就会解析这个字符串，如果text/plain，那么就会显示一个纯文本。
                常用的content_type：
                    ‘text/html'             默认，html文件
                    ’text/plain‘            纯文本
                    'text/css'              css文件
                    'text/javascript'       js文件
                    ’mutipart/form-data‘    文件提交
                    'application/json'      json传输
                    ’application/xml‘       xml文件

            HttpResponse子类
                HttpResponseRedirect    重定向     302
                HttpResponseNotModified 未修改     304
                HttpResponseBadRequest  错误请求    400
                HttpResponseNotFound    没有对应的资源 404
                HttpResponseForbidden   请求被禁止    403
                HttpResponseServerError 服务器错误    500

    GET和POST请求
        无论是GET还是POST,统一都由视图函数接收请求，通过判断request_method区分具体的请求动作
        样例：
            if request.method == 'GET':
                处理GET请求时的业务逻辑
            elif request.method == 'POST':
                处理POST请求的业务逻辑
            else:
                其他请求业务逻辑

        GET请求动作，一般用于向服务器获取数据
        能够产生GET请求的场景：
            浏览器地址栏中输入URL，回车后
            <a href="地址？参数=值&参数=值">
            from表单中的method为get
        GET请求方式中，如果有数据需要传递给服务器，通常会用查询字符串（Query String）传递【注意：不要传递敏感数据】
        URL格式：xxx?参数名1=值1&参数名2=值2...
        服务器端接收参数
            获取客户端请求GET请求提交的数据


        POST处理
            POST请求动作，一般用于向服务器提交大量/隐私数据
            客户端通过表单等POST请求将数据传递给服务器端，如：
                <from method='post' action="/login">
                    姓名：<input type='text' name="username">
                    <input type='submit' value='登录'>
                </form>
            服务器端接收参数
                通过request.method来判断是否为POST请求，如：
                    if request.method == 'POST':
                        处理POST请求的数据并响应
                     else:
                        处理非POST请求的响应
            【注：取消csrf验证，否则Django将会拒绝客户端发来的POST请求，报403响应】#

9. MVC
    传统MVC
        MVC代表Model-View-Controller(模型-视图-控制器)模式
            M模型层（Model），主要用于对数据库层的封装
            V视图层（view），用于向用户展示结果
            C控制（Controller，用于处理请求、获取数据、返回结果（重要））
        作用：降低模块间的耦合度（解耦）
    Django的MTV模式
        MTV代表Model-Template-View(模型-模板-视图)模式
            M模型层（Model）：负责与数据库交互
            T模板层（Template）负责呈现内容到浏览器
            V视图层（View）是核心，负责接收请求、获取数据、返回结果
        作用：降低模块间的耦合度（解耦）
    模板
        模板是可以根据字典数据动态变化的html网页
        模板可以根据视图中传递的字典数据动态生成响应的HTML网页

        模板配置
            创建模板文件夹<项目名>/templates
            在settings.py中TEMPLATES配置项
                BACKEND：指定模板的引擎
                DIRS：模板的搜索目录（可以是一个或多个）
                APP_DIRS:是否要在应用中的templates文件夹中搜索模板文件
                OPTIONS：有关模板的选项
            配置项中需要修改部分
                设置DIRS - 'DIRS'：[os.path.join(BASE_DIR, 'templates')]

            模板的加载方式
                方案1 通过loader获取模板，通过HttpResponse进行响应
                在视图函数中
                    from django.teplate import loader
                    # 通过loader加载模板
                    t = loader.get_template('模板文件名')
                    # 将t转换成HTML字符串
                    html = T.render(字典数据)
                    # 用响应对象将转换的字符串内容返回给浏览器
                    return HttpResponse(html)
                方案2 使用render()直接加载并响应模板
                    在视图函数中：
                        from django.shortcuts import render
                        return render(request,'模板文件名'， 字典数据)

            视图层与模板层之间的交互
                视图函数中可以将python变量封装在字典中传递到模板
                样例：
                    def xxx_view(requset):
                        dic = {
                            '变量1'：'值1'，
                            '变量2'：'值2'，
                        }
                        return render(requset, 'xxx.html', dic)
                模板中，我们可以用{{变量名}}的语法调用视图传进来的变量

            能传递到模板中的数据类型
                str-字符串
                int-整型
                list-数组
                tuple-元组
                dict-字典
                func-方法
                obj-类实例化的对象

            在模板中使用变量语法
                {{变量名}}
                {{变量名.index}} - 索引
                {{变量名.key}} - 字典取值
                {{对象.方法}} - 方法调用
                {{函数名}}

            模板标签
                作用：将一些服务器端的功能嵌入到模板中，例如流程控制等
                标签语法：
                    {% 标签 %}
                    ...
                    {% 结束标签 %}

                if标签
                    语法：
                        {% if 条件表达式1 %}
                        ...
                        {% elif 条件表达式2 %}
                        ...
                        {% else %}
                        ...
                        {% endif %}
                    注：
                        if条件表达式里可以使用的运算符：
                            ==、 !=、 <、 >、 <=、 >=、 in、 not in、
                            is、 is not、 not、 and、 or
                        在if标记中使用实际括号是无效的语法。如果需要指定优先级，则应使用嵌套的if标签

                for标签
                    语法：
                        {% for 变量 in 可迭代对象 %}
                        ...循环语句
                        {% empty %}
                        ...可迭代对象无数据时填充的语句
                        {% endfor %}
                    内置变量 - forloop
                            变量            |           描述
                        forloop.counter         循环的当前迭代（从1开始索引）
                        forloop.counter0        循环的当前迭代（从0开始索引）
                        forloop.revcounter      counter值得倒序
                        forloop.revcounter0     counter0值的倒叙
                        forloop.first           如果这是第一次通过循环，则为真
                        forloop.last            如果这是最后一次循环，则为真
                        forloop.parentloop      当嵌套循环，parentloop表示外层循环

            模板过滤器
                定义：在变量输出时对变量的值进行处理
                作用：可以通过使用过滤器来改变变量的输出显示
                语法：{{ 变量 | 过滤器1:'参数值1' | 过滤器2:'参数值2'... }}
                常用过滤器
                    lower               将字符串转换为全部小写
                    upper               将字符串转换为大写形式
                    safe                默认不对变量内的字符串机进行HTML转义
                    add:'n'             将value的值增加n
                    truncatechars:'n'   如果字符串字符多于指定的字符数量，则会被截断。
                                        截断的字符串将以可翻译的省略号序列’...‘结尾

            模板的继承
                定义：模板继承可以使父模板的内容重用，子模版直接继承父模板的全部内容并可以覆盖父模版中相应的块
                语法：
                    父模板中：
                        定义父模板中的块block标签
                        {% block block_name %}
                        ...
                        {% endblock block_name %}
                        标识出哪些在子模块中是允许被修改的
                        block标签：在父模板中定义，可以在子模板中覆盖
                    子模板中：
                        继承模板extends标签（写在模板文件的第一行）
                            {% extend 'xxx.html' %}
                        子模版重写父模板中的内容块
                            {% block block_name %}
                            ...覆盖内容
                            {% endblock block_name %}
                重写的覆盖规则
                    不重写，将按照父模板的效果显示
                    重写，则按照重写效果显示
                注意
                    模板继承时，服务器端的动态内容无法继承

10. URL的反向解析
    代码中URL出现的位置
        模板中
            <a href='url'>超链接</a>
            <form action='URL' method='POST'>
        视图函数
            302跳转   HttpResponseRedirect('URL')

    代码中URL书写规范
        绝对地址：
            http://127.0.0.1:8000/page/1
        相对地址
            1. '/'开头的相对地址，浏览器会把当前地址栏里的协议，ip和端口加上这个地址，作为最终访问地址，
            2. 没有'/'开头的相对地址，浏览器会根据当前url的最后一个/之前的内容加上该相对地址作为最终访问地址

    URL反向解析
        是指在视图或模板中，用path定义的名称来动态查找或计算除相应的路由
        path函数的语法
            path(route, views, name='别名')
            path('page',views.page_view, name='page_url')
        根据path中的’name=‘关键字传参给url确定了一个唯一确定的名字，在模板或视图中，可以通过这个名字反向推断出
        此url信息

        模板中 - 通过url标签实现地址的反向解析
            {% url '别名' %}
            {% url '别名' '参数值1' '参数值2' %}
        视图函数中 - 可调用django中的reverse方法进行反向解析
            from django.urls import reverse
            reverse('别名', args=[], kwargs={})

11. 静态文件
    静态文件配置 - settings.py中
    配置静态文件的访问路径【该配置默认存在】
        通过哪个url地址找静态文件
        STATIC_URL = '/static/'
        说明
            指定访问静态文件时是需要通过/static/xxx
            或http://127.0.0.1:8000/static/xxx
            【xxx表示具体的静态资源位置】

    配置静态文件的存储路径STATICFILES_DIRS
        STATICFILES_DIRS保存的是静态文件在服务器端的存储位置
                os.path.join(BASE_DIR, 'static'),
            )

    模板中访问静态文件 - img标签为例
        方案一：直接拼接访问路径,图片在static下的images文件夹下
            <img src='/static/images/xxx.jpg'>
            或
            <img src='http://127.0.0.1:8000/static/images/xxx.jpg>
        方案二：通过{% static %}标签访问静态文件 更动态
            1. 加载static - {% load static %}
            2. 使用静态资源 - {% static '静态资源路径' %}
            3. 样例：  <img src={% static 'images/xxx.jpg' %}>

12. 应用
    应用在django项目中是一个独立的业务模块，可以包含自己的路由、视图、模块、模型
    创建应用：
        1. 用manage.py中的子命令startapp创建应用文件夹
            python3 manage.py startapp xxx
        2. 在settings.py的INSTALLED_APPS列表中配置安装此应用
            settings.py配置样例
                INSTALLED_APPS=[
                    'user',
                    'music',
                ]

13. 分布式路由
    django中。主路由配置文件（urls.py）可以不处理用户具体路由
    主路由根据配置文件的可以做请求的分发（分布式请求处理）。具体的请求可以由各自的应用来进行处理
    配置分布式路由
        1. 主路由中调用include函数
            语法：include('app_name.url模块名')
            作用：用于将当前理由转到各个应用的路由配置文件的urlpatterns进行分布式处理
            案例：
                from django.urls import path, include
                from . import views

                urlpatterns = [
                    path('admin/', admin.site.urls),
                    path('test_static', views.test_static),
                    path('music/', include('music.urls')
                ]
        2. 应用下配置urls.py
            应用下手动创建urls.py文件
            内容结构同主路由完全一样
                 from django.urls import path, include
                from . import views

                urlpatterns = [
                    path('index', views.index_view)
                ]

    应用下的模板
        应用内部可以配置模板目录
        1. 应用下手动创建templates文件夹
        2. settings.py中开启应用模块功能
            TEMPALTE配置项中的'APP_DIRS'值为True即可

        应用下templates和外层templates都存在时，django的查找模板规则
        1. 优先查找外层templates目录下的模板
        2. 按INSTALLED_APPS配置下的应用顺序逐层查找

13. 模型层
    负责跟数据库之间进行通信
    django配置MySQL
        安装mysqlclient
        Ubuntu系统：需检查是否安装python3-dev和default-libmysqlcilent-dev
            sudo apt list --installed|grep -E 'libmysqlclient-dev|python3-dev'
            没有需要安装：sudo apt-get install python3-dev default-libmysqlclient-dev
            sudo pip3 install mysqlclient

        创建数据库
        进入mysql数据库执行
            create database 数据库名 default charset utf8
            通常数据库名跟项目名保持一致
        settings.py里进行数据库的配置
            修改DATABASES配置项的内容，由splite3变为mysql
                ENGINE - 指定数据库存储引擎
                NAME - 指定要连接的数据库名称
                USER - 指定登入到数据库的用户名
                PASSWORD - 数据库的密码
                HOST/PORT - 连接具体数据库的IP和端口

    模型是一个python类，它是由django.db.models.Model派生出来的子类
    一个模型类代表数据库中的一张数据表
    模型类中每一个类属性都代表数据库中的一个字段
    模型是数据交互的接口，是表示和操作数据库的方法和方式

14. ORM框架
    即对象关系映射，它是一个程序技术，它允许使用类和对象对数据库进行操作，从而避免通过sql语句操作数据库
    作用：
        1. 建立模型类和表之间的对应关系，允许我们通过面向对象的方式来操作数据库
        2. 根据设计的模型类生成数据库中的表格
        3. 通过简单的配置就可以进行数据库的切换
    优点：
        只需要面向对象编程，不需要面向数据库编写代码
            对数据库的操作都转化成对类属性和方法的操作
            不用编写各种数据库的sql语句
        实现了数据模型与数据库的解耦，屏蔽了不同数据库操作上的差异
            不在关注用的是mysql、oracle...等数据库的内部细节
            通过简单的配置就可以轻松更换数据库，而不需要修改代码
    缺点
        对于复杂业务，使用成本较高
        根据对象的操作转化成SQL语句，根据查询的结果转化成对象，在映射过程中有性能损失

    模型类的创建
        from django.db import models
        class 模型类名(models.Model):
            字段名 = models.字段类型（字段选项）

    数据库迁移
        迁移是django同步对模型所作的更改（添加字段，删除模型等）到数据库模式的方式
        1. 生成迁移文件 - 执行python manage.py makemigrations
        将应用下的models.py文件生成一个中间文件，并保存在migrations文件夹中
        2. 执行迁移脚本程序 - 执行python manage.py migrate
        执行迁移程序实现迁移。将每个应用下的migrations目录中的中间文件同步会数据库

    模型类 - 字段类型
        BooleanField()
            数据库类型：tinyint(1)
            编程语音中：使用True或False来表示值
            在数据库中，使用1或0来表示具体的值

        CharField()
            数据库类型：varchar
            注意：必须要指定max_length参数值

        DateField()
            数据库类型：date
            作用：表示日期
            参数：
                1. auto_now: 每次保存对象时，自动设置该字段为当前时间（取值：True/False）
                2. auto_now_add: 当对象第一次被创建时自动设置当前时间（取值：True/False）
                3. default：设置当前时间（取值：字符串格式时间如：'2019-6-1'）
                以上三个参数只能多选一

        DataTimeField()
            数据库类型：datatime(6)
            作用：表示日期和时间
            参数同DataField

        FloatField()
            数据库类型：double
            编程语言中和数据库中都使用小数表示值

        DecimalField()
            数据库类型：decimal(x,y)
            编程语言中：使用小数表示该列的值
            在数据库中使用小数
            参数：
                max_digits:位数总数，包括小数点后的位数。该值必须大于等于decimal_places
                decimal_places:小数点后的数字数量

        EmailField()
            数据库类型：varchar
            编程语言和数据库中使用字符串

        IntergerField()
            数据库类型：int
            编程语言和数据库中使用整数

        ImageField()
            数据库类型：varchar(100)
            作用：在数据库中为了保存图片的路径
            编程语言和数据库中使用字符串

        TextField()
            数据库类型：longtext
            作用：表示不定长的字符数据

    模型类的字段选项
        字段选项，指定创建的列的额外的信息
        允许出现多个字段选项，多个选项之间使用，隔开

        primary_key
            如果设置为True，表明该列为主键，如果指定一个字段为主键，则数据库表不会创建id字段

        blank
            设置为True，字段可以为空，设置为False时，字段是必须填写的

        null
            设置为True，表示该列值允许为空
            默认为false，如果此选项为False建议加入default选项来设置默认值

        default
            设置所在列的默认值，如果字符选项null=False建议添加此项

        db_index
            如果设置为True，表示为该列添加索引

        unique
            如果设置为True，表示该字段在数据库中的值必须是唯一的（不能重复出现的）

        db_column
            指定列的名称，如果不指定的话则采用属性名作为列名

        verbose_name
            设置此字段在admin界面上的显示名称

    Meta类
        定义：使用内部Meta类来给模型赋予属性，Meta类下有很多内建的类属性，可对模型类做一些控制
        class Meta:
            db_table = 'xxx'    # 修改表名

15. ORM操作
    基本操作包括增删改查操作，即（CRUD操作）
    CRUD是指在做计算处理时的增加（Create）、读取查询（Read）、更新（Update)和删除（Delete）

    ORM CRUD核心 -> 模型类 管理器对象
    每个继承自models.Model的模型类，都会有一个objects对象被同样继承下来。这个对象叫管理器对象
    数据库的增删改查可以通过模型的管理器实现
    即模型类.objects.xxx()

    创建数据
        django ORM使用一种直观的方式把数据库表中的数据表示成python对象
        创建数据中每一条记录就是创建一个数据对象

        方案1
            MyModel.objects.create(属性1=值1, 属性2=值2,...)
            成功：返回创建好的实体对象
            失败：抛出异常
        方案2
            创建MyModel实例对象，并调用save()进行保存
            obj = MyModel(属性=值, 属性=值,...)
            obj.属性 = 值
            obj.save()

    Django Shell
        在django提供了一个交互式的操作项目叫django shell，它能够在交互模式用项目工程的代码执行相应的操作
        利用django Shell可以代替编写view的代码来进行直接操作
        注意：项目代码发生变化时，重新进入Django Shell
        启动方式：python manage.py shell

    查询
        数据库的查询需要使用管理器对象进行
        同MyModel.objects管理器方法调用查询方法
        方法：
            all()       查询全部记录，返回QuerySet查询对象
                用法：MyModel.objects.all()
                作用：查询MyModel实体中的所有数据
                等同于select * from table
                返回值：QuerySet容器对象，内部存放MyModel实例
                可用for...in...遍历

            values('列1','列2',...)
                用法：MyModel.objects.values(...)
                作用：查询部分列的数据并返回
                等同与select 列1, 列2, ... from xxx
                返回值:QuerySet
                返回查询结果容器，容器内存字典，每个字典代表一条数据
                格式为：{'列1':值1, '列2':值2}

            values_list('列1', '列2',...)
                用法：MyModel.objects.values_list(...)
                作用：返回元组形式的查询结果
                等同于select 列1, 列2,... from xxx
                返回值：QuerySet容器对象，内部存放元组，遍历时使用索引

            order_by()
                用法：MyModel.objects,order_by('-列', '列')
                作用：
                    与all()方法不同，它会用SQL语句的ORDER BY子句对查询结果进行根据某个字段选择性的进行排序
                说明：默认是按照升序排序，降序排序则需要在列前添加'-'表示

            get(条件)       查询符和条件的单一记录
                语法：MyModel.objects.get(条件)
                作用：返回满足条件的唯一一条数据
                说明：该方法只能返回一条数据
                     查询结果多余一条数据则会抛出Model.MultipleObjectsReturned异常
                     查询结果如果没有数据则排出Model.DoesNotExist

            filter(条件)    查询符和条件的多条记录
                语法：MyModel.objects.filter(属性1=值1, 属性2=值2)
                作用：返回包含此条件的全部的数据集
                返回值：QuerySet容器对象，内部存放MyModel实例
                说明：当多个属性在一起时为'与'的关系

            exclude(条件)   查询符和条件之外的全部记录
                语法：MyModel.objects.exclude(条件)
                作用：返回不包含此条件的全部的数据集


    可以在模型类中定义__str__方法，自定义QuerySet中的输出格式
    对QuerySet对象可以使用query获得SQL语句

    查询谓词
        定义：做更灵活的条件查询时需要使用查询谓词
        说明：每个查询谓词是一个独立的查询功能
        __excat: 等值匹配
        __contains: 包含指定值
            author.objects.filter(name__contains='w')
            等同于 select * from author where name like '%w%'
        __startswith: 以xxx开始
        __endswith: 以xxx结束
        __gt: 大于指定值
        __gte: 大于等于
        __lt: 小于
        __lte: 小于等于
        __in: 查找数据是否在指定范围内
            author.objects.filter(country__in=['中国','美国'])
            等同与select * from author where country in ('中国','美国')
        __range: 查找数据是否在指定的区间范围内
            anthor.objects.filter(age__range=(35,60))
            等同于select ... where author between 35 and 50

    更新单个数据
        修改单个实体的某些字段值的步骤：
            1. 查
                - 通过get()得到要修改的实体对象
            2. 改
                - 通过对象.属性的方式修改数据
            3. 保存
                - 通过对象.save()保存数据

    批量更新数据
        直接调用QuerySet的update(属性=值)实现批量修改

    单个数据删除
        步骤
            1. 查找查询结对应的一个数据对象
            2. 调用这个数据对象的delete()方法实现删除

    批量删除
        步骤
            1. 查找查询结果集中满足条件的全部QuerySet查询集合对象
            2. 调用查询集合对象的delete()方法实现删除

    伪删除
        通常不会轻易在业务里把数据真正删掉，取而代之的是做伪删除，即在表中添加一个布尔型字段（is_active），
        默认为True；执行删除时，将欲删除数据的is_active字段置为False
        注意：用伪删除时，确保显示数据的地方，均加了is_active=True的过滤查询

    F对象
        一个F对象代表数据库中某条记录的字段的信息
        作用：
            - 通常是对数据库中的字段值在不获取的情况下进行操作
            - 用于类属性（字段）之间的比较
        语法：
            from django.db.models import F
            F('列名')

    Q对象
        当在获取查询结果集使用复杂的逻辑或|、逻辑非~等操作时可以借助于Q对象进行操作
        Q对象在数据包django.db.models中，需要先导入再使用
        作用：在条件中用来实现除and（&）以外的or(|)或not(~)操作
        运算符：
            & 与操作
            | 或操作
            ~ 非操作

    聚合查询
        聚合查询是指对一个数据表中的一个字段的数据进行部分或全部进行统计查询，
        查bookstore_book数据表中的全部书的平均价格，查询所有书的总个数等，都要使用聚合查询
        聚合查询分为：
            整表聚合
            分组聚合

        整表整合
            不带分组的聚合查询是指导将全部数据进行集中统计查询聚合函数【需要导入】
            - 导入方法：from django.db.models import *
            - 聚合函数：Sum、Avg、 Count、Max、Min
            语法：MyModel.objects.aggregate(结果变量名=聚合函数('列'))
            - 返回结果：结果变量名和值组成的字典
            格式为：{'结果变量名': 值}

        分组聚合
            分组聚合是值通过计算查询结果中每一个对象所关联的对象集合，从而得出总计值
            （也可以是平均值或总和），即为查询集的每一项生成聚合
            语法：
                - QuerySet.annotate(结果变量名=聚合函数('列'))
            返回值：
                - QuerySet
            步骤：
                1. 通过先用查询结果MyModel.objects.values查找查询要分组聚合的列
                2. 通过返回结果的QuerySet.annotate方法分组聚合得到分组结果

    原生数据库操作
        django也可以支持，直接用sql语句的方式通信数据库
        查询：使用MyModel.objects.raw()进行，数据库查询操作查询
        语法：MyModel.objects.raw(sql语句, 拼接参数)
        返回值：RawQuerySet集合对象【只支持基础操作，比如循环】

        使用原生语句时小心SQL注入
        定义：用户通过数据上传，将恶意的sql语句提交给服务器，从而达到攻击效果
        案例1：用户在搜索好友的表单框里输入’1 or 1=1' 攻击结果：可查询除所有用户数据

    cursor
        完全跨过模型类操作数据库 - 查询/更新/删除
        导入cursor所在的包
            from django.db import connection
        在创建cursor类的构造函数创建cursor对象，再使用cursor对象，
        为保证在出现异常时能释放cursor资源，通常使用with语句进行创建操作
            from django.db import connection
            with connection.cursor() as cur:
                cur.execute('SQL语句', 拼接参数)


admin管理后台
    django提供了比较完善的后台管理数据库的接口，可供开发过程中调用和测试使用
    django会搜索所有已注册的模型类，为这些模型类提供数据管理界面，供开发者使用
    创建后台管理账号 - 该账号为管理后台最高权限账号
        python manage.py createsuperuser

    注册自定义模型类
        若要自己定义的模型类也能在/admin后台管理界面中显示和管理，需要将自己的类注册到后台管理界面
        注册步骤：
            在应用app中的admin.py中导入注册要管理的模型models类，如：
                from .models import Book
            调用admin.site.register（自定义模型类）方法进行注册
            在后台按照模型类定义中的__str__方法定义的显示

    模型管理器类
        作用：
            为后台管理界面添加便于操作的新功能
        说明：
            后台管理器类必须继承自django.contrib.admin里的ModelAdmin类
        使用方法
            1. 在<应用app>/admin.py里定义模型管理器类
                class XXXManager(admin.ModelAdmin):
                    ...
            2. 绑定注册模型管理器和模型类
                from django.contrib import admin
                from .models import *
                admin.site.register(YYYY ,XXXXManager)  # 绑定YYYY模型类与管理器类XXXManager


16. 关系映射
    在关系型数据库中，通常不会把所有数据都放在同一张表中，不易于扩展，常见的关系映射有：
        一对一映射
            一人一个身份证
        一对多映射
            一个版有很多个学生
        多对多映射
            一个学生可以报多个课程，一个课程可以有多个学生学习

    一对一 【创建】
        一对一是表示现实事物间存在的一对一的对应关系
        语法：OneToOneField(类名, on_delete = xxx)
        class A(model.Model):
            ...
        clas B(model.Model):
            属性 = models.OneToOneField(A, on_delete=xxx)

        特殊字段选项【必须】
            on_delete - 级联删除
            1. models.CASCADE 级联删除。 Django模拟SQL约束ON DELETE CASCADE的行为，并删除包含ForeignKey的对象
            2. models.PROTECT 抛出protectedError以阻止被引用对象的删除；【等同于mysql默认的RESTRICT】
            3. SET_NULL 设置ForeignKey null; 需要指定null=True
            4. SET_DEFAULT 将ForeignKey设置为其默认值；必须设置ForeignKey的默认值

        对无外键的模型类[以Author为例]：
            author1 = Author.objects.create(name='王老师')
        对有外键的模型类[以wife为例]：
            # 关联王老师obj
            wife1 = Wife.objects.create(name='王夫人', author=author1)
            或
            # 关联王老师对应主键值
            wife1 = Wife.objects.create(name='王夫人', author_id=1)

        查询数据
            正向查询：直接通关外键属性查询，则称为正向查询
            反向查询：没有外键属性的一方，可以调用反向属性查询到关联的另一方，python提供，不需要设置
                反向关联属性为'实例对象.引用类名（小写）'
                当反向引用不存在时，则会触发异常


    一对多
        表示现实事物之间存在的一对多的对应关系
        语法：
            当一个A类对象关联多个B类对象时
            class A(model.Model):
                ...
            class B(model.Model):
                属性 = models.ForeignKey(A对象模型类, on_delete=xx)
            ForeignKey必须指定on_delete模式

        数据的创建
            先创建1，再创建多。 以出版社和书籍为例
            1的创建：正常创建数据即可：
                pub1 = Publisher.objects.create(name=‘xxx出版社’)
            多的创建，两种方式
                Book.objects.create(title='c++', publisher=pub1)
                或
                Book.objects.create(title='python', publisher_id=1)

        查询数据
            正向查询【通过Book查询Publisher】
                直接通过Book.Publisher属性查询
            反向查询【通过Publisher查询对应的所有的Book】
                需要用到反向属性
                # 方式一：通过book_set获取pub1对应的多个Book数据对象
                books = pub1.book_set.all()
                # 方式二：采用filter查询
                books = Book.objects.filter(publisher=pub1)

17. 会话
    定义：
        从打开浏览器访问一个网站，到关闭浏览器结束此次访问，称之为一次会话
        HTTP协议是无状态的，导致会话状态难以保持
        Cookies和Session就是为了保持会话状态而诞生的两个存储技术

    Cookies
        Cookies是保存在客户端浏览器上的存储空间
        Chorme浏览器可能通过开发作工具的Application>>Storage>>Cookies查看和操作浏览器端所有的Cookies值
        火狐浏览器可能通过开发者工具的存储->Cookies查看

        特点
            cookies在浏览器上是以键-值对的形式进行存储的，键和值都是以ASCII字符串的形式存储（不能是中文字符串）
            存储的数据带有生命周期
            cookies的内部的数据会在每次访问此网址时都会携带到服务器端，如果cookies过大会降低响应速度

        使用
            HttpResponse.set_cookie(key,value = '', max_age=None, expires=None)
                -key: cookie的名字
                -value: cookie的值
                -max_age: cookie存活时间， 秒为时间单位
                -expires: 具体过期时间
                -当不指定max_age和expires时，关闭浏览器时此数据失效

            删除Cookies
                HttpReponse.delete_cookies(key)
                删除指定的key的Cookies。如果key不存在则什么也不发生

            获取Cookies
                通过request.COOKIES绑定的字典（DICT）获取客户端的COOKIES数据
                value = request.COOKIES.get('COOKIES名'， '默认值')

    session定义
        session是在服务器上开辟一段空间用于保留浏览器和服务器交互时的重要数据，
        实现方式：
            使用session需要在浏览器客户端启动cookie，且在cookie中存储sessionid
            每个客户端都可以在服务器端有一个独立的Session
            注意：不同的请求者之间不会共享这个数据，与请求者一一对应

        使用
            session对应项是一个类似于字典的SessionStore类型的对象，可以用类似于字典的方式进行操作
            session能够存储如字符串，整型、字典、列表等
            保存session的值到服务器
                request.session['KEY'] = VALUE
            获取session的值
                value = request.session['KEY']
                value = request.session.get['key','默认值']
            删除session
                del request.session['KEY']

            settings.py中的相关配置项
                1. SESSION_COOKIE_AGE
                    作用：指定sessionid在cookies中的保存时长（默认为两周）
                2. SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                    设置只要浏览器关闭时，session就失效（默认为false）
                注意：Django中的session数据存储在数据库中，所以使用session前需要确保已经执行过migrate

            django session的问题
                1. django_session表是单表设计；且该表数据量持续增持【浏览器故意删掉sessionid或过期数据未删除】
                2. 可以每晚执行python manage.py clearsessions【该命令可删除已过期的session数据】

    cookies和session对比
         种类             存储          安全性
        Cookies         浏览器         相对不安全
        session         服务器         相对安全

18. 哈希算法
    给定明文，计算出一段定长的、不可逆的值；md5, sha-256
    特点
        1. 定长输出：不管明文输入长度为多少，哈希值都是定长的，md5 - 32位16进制
        2. 不可逆：无法反向计算出对应的明文
        3. 雪崩效应：输入改变，输出必然变
    场景：
        1. 密码处理
        2. 文件的完整性校验
    使用：
        1. 调包hashlib，自带 import hashlib
        2. 生成md5计算对象 m = hashlib.md5()
        3. m.update(password.encode())
        4. 拿到哈希值结果  m.hexdigest()


19. 缓存
    定义：缓存是一类可以更快的读取数据的介质统称，也指其他可以加快数据读取的存储方式。
        一般用来存储临时数据，常用介质的是读取速度很快的内存
    意义：视图渲染有一点成本，数据库的频繁查询过高；所以对于低频变动的页面可以考虑使用缓存技术，
        减少实际渲染次数；用户拿到响应的时间成本会更低
    django中设置缓存 - 数据库缓存
        将缓存的数据存储在您的数据库中
        说明：尽管存储介质没有更换，但是当把一次负责查询的结果直接存储到表里。
            比如多个条件的过滤查询结果，可避免重复进行复杂查询，提升效率
        需要手动创建缓存用表： python manage.py createcachetable
        配置样例
            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.db.DatabaseCache',   # 引擎
                    'LOCATION': 'my_cache_table',   # 缓存到哪张表，表名
                    'TIMEOUT': 300,     # 缓存保存时间，单位秒，默认值为300
                    'OPTIONS': {
                        'MAX_ENTRIES': 300,  # 缓存最大数据条数
                        'CULL_FREQUENCY': 2,    # 缓存条数达到最大值时，删除1/x的缓存数据
                    }
                }
            }

    django中设置缓存 - 本地内存缓存
        数据缓存到服务器内存中
        配置样例：
            CACHES = {
                'default': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',     # 引擎
                    'LOCATION': 'unique-snowflake',     # 雪花算法，内存地址寻找问题
                    # 基于文件的缓存
                    # 'LOCATION': 'C:\TEST\CACHE'   # 文件夹路径
                }
            }

    缓存api的使用
        整体缓存策略
            视图函数中：
                from django.views.decorators.cache import cache_page
                @cache_page(30)
                def my_view(request):
                    ...
            路由中：
                from django.views.decorators.cache import cache_page
                from djanfo.urls import path
                from . import views
                urlpatterns = [
                    path('', cache_page(60)(my_view)),
                ]

        局部缓存策略:更灵活、可复用
            先引入cache对象
                方式1：使用caches['CACHE配置key']导入具体对象
                    from django.core.cache import caches
                    cache1 = caches['myalias']
                    cache2 = caches['myalias_2']
                方式2:
                    from django.core.cache import cache
                    相当于直接引入CACHES配置项中的'default'项

            cache.set(key, value, timeout)   - 存储缓存
                key:缓存的key，字符串类型
                value:python对象
                timeout:缓存存储时间（s），默认为CACHES中的TIMEOUT值
                返回值；None

            cache.get(key)  - 获取缓存
                key:缓存的key
                返回值：为key的具体值，如果没有数据，则返回None

            cache.add(key, value)   - 存储缓存，只在key不存在时生效
                返回值:True(即存储成功) or False(即存储失败)

            cache.get_or_set(key,value,timeout) - 如果未获取到数据，则执行set操作
                返回值：value

            cache.set_many(dict, timeout) - 批量存储缓存
                dict:key和value的字典
                timeout:存储时间（s）
                返回值：插入不成功的key的数组

            cache.get_many(key_list)  - 批量获取缓存数据
                key_list:包含key的数组
                返回值：取到的key和value的字典

            cache.delete(key) - 删除key的缓存数据
                返回值：None

            cache.delete_many(key_list) - 批量删除
                返回值：None

    浏览器缓存   - 强缓存
        不会向服务器发生请求，直接从缓存中读取资源
        1.响应头 - Expires
            定义： 缓存过期时间，用来指定资源到期的时间，是服务器端的具体的时间点
            样例：Expires:Thu, 02 Apr 2030 05:14:08 GMT
        2.响应头 - Cache-Contorl
            在HTTP/1.1中，Cache-Control主要用于控制网页缓存。
            比如当Cache-Control:max-age=120 代表请求创建时间后的120秒，缓存失效
            说明：目前服务器都会带有这两个头同时响应给浏览器，浏览器优先使用Cache-Control

    协商缓存
        考虑到大图片这类比较费带宽且不易变化的数据，强缓存时间到期后，浏览器会去跟服务器协商，
        当前缓存是否可用，如果可用，服务器不必返回数据，浏览器继续使用原来缓存的数据，如果文件不可用，则返回最新数据

        Last_Modified响应头 和 If-Modified-Since请求头
        说明：
            1. Last-Modified为文件的最近修改时间，浏览器第一次请求静态文件时，服务器如果返回Last-Modified响应头，则代表该资源为需协商的缓存
            2. 当缓存到期后，浏览器将获取到的Last-Modified值作为请求头If-Modified-Since的值，与服务器发请求协商，服务端返回304响应码【响应体为空】
                ，代表缓存继续使用，200响应码代表缓存不可用【响应体为最新资源】

        ETag响应头和If-None-Match请求头
        说明：
            1. ETag是服务器响应请求时，返回当前资源文件的一个唯一标识（由服务器生成），只要资源有变化，ETag就会重新生成
            2. 缓存到期后，浏览器将ETag响应头的值作为If-None-Match请求头的值，给服务器发请求协商；
                服务器街道请求头后，比对文件标识，不一致则认为资源不可用，返回200响应码【响应体为最新资源】
                可用则返回304响应码

20. 中间件
    中间件是django请求/响应处理的钩子框架。它是一个轻量级的、低级的"插件"系统，用于全局改变django的输入或输出
    中间件以类的形式体现
    每个中间件组件负责做一些特定的功能。例如，django包含一个中间件组件AuthenticationMiddleware,它使用会话将用户与请求关联起来

    编写中间件
        中间件类必须继承自django.utils.deprecation.MiddlewareMixin类
        中间件类必须实现下列五个方法中的一个或多个：
            process_request(self,request)
                执行路由之前被调用，在每个请求上调用，返回None或HttpResponse对象
            process_view(self,request,callback,callback_args,callback_kwargs)
                调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
            process_response(self,request,response)
                所有响应返回浏览器被调用，在每个请求上调用，返回HttpResponse对象
            process_exception(self,request,exception)
                当处理过程中抛出异常时调用，返回一个HttpResponse对象
            process_template_response(self,request,response)
                在视图函数执行完毕且试图返回的对象中包含render方法时被调用，该方法需要返回实现了render方法的响应对象
                注：中间件中的大多数方法在返回None时表示忽略当前操作进入下一项事件，当返回HttpResponse对象时表示此请求介绍，直接返回给客户端

    注册中间件
        settings.py中需要注册一下自定义的中间件
            # file: settings.py
            MIDDLEWARE = [
                ...
            ]
        注意：配置为数组，中间件被调用时以'先上到下'再'由下到上'的顺序调用，分割点在进入视图之后


CSRF - 跨站伪造请求攻击
    某些恶意网址上包含连接、表单按钮或者javaScript，它们会利用登录过的用户在浏览器中的认证信息试图在你的网站上完成某些操作，这就是跨站请求伪造（CSRF,即Cross-Site Request Forgey）
    CSRF防范
        django采用'比对暗号'机制 防范攻击
        Cookies中存储暗号1，模板中表单里藏着暗号2，用户只有在本网站下提交数据，暗号2才会随着表单提交给服务器，django对比两个暗号，对比成功，则认为是合法请求，否则是违法请求-403响应码
    配置步骤：
        1. settings.py中确认MIDDLEWARE中django.middleware.csrf.CsrfViewMideeleware
        2. 模板中，form标签下添加如下标签
            {% csrf_token%}

    特殊说明：
        如果某个视图不需要django进行csrf保护，可用用装饰器关闭对此视图的检查
        from django.views.decorators.csrf import csrf_exempt
        @csrf_exempt
        def my_view(request):
            ...

21. 分页
    分页是指在web页面有大量数据需要显示，为了阅读方便在每一个页面中仅显示部分数据
    优点：
        1. 方便阅读
        2. 减少数据提取量，减轻服务器压力
    django提供了Paginator类可以方便的实现分页功能
    Paginator类位于django.core.paginator模块中

    Paginator对象
        负责分页数据整体的管理
        对象的构造方法
            paginator = Paginator(object_list,per_page)
                object_list 需要分页数据的对象列表
                per_page 每页数据个数
                返回值：Paginator的对象
        paginator属性
            count:需要分页数据的对象总数
            num_pages:分页后的页面总数
            page_range:从1开始的range对象，用于记录当前面码数
            per_page：每页数据的个数
        paginator方法
            paginator对象.page(number)
                参数：number为页码信息（从1开始）
                返回当前number页对应的页信息
                如果提高的页码不存在，抛出Invalidpage异常

                Invalidpage:总的异常基类，包含一下两个异常子类
                    PageNotAnlntegar:当向page()传入一个不是整数的值时抛出
                    Emptypage:当向page()提供一个有效值，但是那个页面上没有任何对象时抛出


        page对象
            负责具体某一页的数据的管理
            创建对象
                Paginator对象的page()方法返回Page对象
                page = paginator.page(页码)
            Page对象属性
                object_list:当前页上所有数据对象的列表
                number：当前页的序号，从1开始
                paginator:当前page对象相关的paginator对象

            page对象方法
                has_next():如果有下一页返回True
                has_previous():如果有上一页返回True
                has_other_pages():如果有上一页或下一页返回True
                next_page_number():返回下一页的页码，如果下一页不存在，抛出InvalidPage异常
                previous_page_number():返回上一页的页码，如果上一页不存在，抛出InvalidPage异常

21. CSV文件定义
    逗号分隔值（Comma-Separated Values. CSV，有时也称为字符分隔值，因为分割字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）
    说明：可被常见制表工具，如excel等直接进行读取
    python中生成csv文件
        python提供了内建库-csv；可直接通过该库操作CSV文件
        案例如下:
            import csv
            with open('eggs.csv','w',newline='') as csvfile:
                writer = csv.write(csvfile)
                writer.writerow(['a','b','c'])

    csv文件下载
        在网站中，实现下载csv，注意如下：
            响应Context_Type类型需修改text/csv。这告诉浏览器该文档是CSV文件，而不是HTML文件
            响应会获得一个额外的Content-Disposition标头，其中包含csv文件的名称。它将被浏览器用于开启“另存为...”对话框

21. 内建用户系统
    django带有一个用户认证系统，它处理用户账号、组、权限以及基于cookie的用户会话
    用户可以直接使用django自带的用户表
    模型类位置 from django.contrib.auth.models import User
    包含属性：
        username        用户名
        passward        密码
        email           邮箱
        frist_name      名
        last_name       姓
        is_superuser    是否是管理员账号
        is_staff        是否可以访问admin管理界面
        is_active       是否是活跃用户，默认True。一般不删除用户，而是将用户的is_active设为False
        last_login      上一次的登录时间
        date_joined     用户创建的时间

    创建用户
        创建普通用户create_user
            from django.contrib.auth.models import User
            # 仅username和password是必须的
            user = User.objects.create_user(username='用户名', password='密码', email='邮箱'...)
        创建超级用户create_superuser
            from django.contrib.auth.models import User
            user = User.objects.create_superuser(username='用户名', password='密码', email='邮箱'...)

    删除用户 - 伪删除
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(username='用户名')
            user.is_active = False
            user.save()
            print('删除普通用户成功！')
        except:
            print('删除普通用户失败')

    校验密码
        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)
        说明：如果用户名密码校验成功则返回对应的user对象，否则返回None

    修改密码
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(username='xiaonao')
            user.set_password('654321')
            user.save()
            return HttpResponse('修改密码成功！')
        except:
            return HttpResponse('修改密码失败！')

    登录状态保持
        from django.contrib.auth import login
        def login_view(request):
            user = authenticate(username=username,password=password)
            login(request,user)

    登录状态校验
        from django.contrib.auth.decorators import login_required
        @login_required
        def index_view(request):
            # 该视图必须为用户登录状态下才可访问
            # 当前登录用户可通过request.user获取
            login_user = request.user
            ...

    登录状态取消
        from django.contrib.auth import logout
        def logout_view(request):
            logout(request)

    扩展字段
        方案1：通过建立新表，跟内建表做1对1
        方案2：继承内建的抽象user模型类
            1. 添加新的应用
            2. 定义模型类 继承AbstractUser
            3. settings.py中指明AUTH USER MODEL = '应用名.类名'
            注意：此操作需要在第一次Migrate之前进行


22. 文件上传
    定义：用户可以通过浏览器将图片等文件传至网站
    场景：
        用户上传头像
        上传流程性的文档【PDF, TXT等】
    上传规范 - 前端【HTML】
         文件上传必须为POST提交方式
         表单'<form>'中文件上传时必须有带有enctype='multipart/form-data'时才会包含文件内容数据
         表单中用<input type='file' name='xxx'>标签上传文件
    上传规范 - 后端【django】
        视图函数中，用request.FILES取文件框的内容
        file=request.FILES['xxx']
        说明：
            1. FILES的key对应页面中file框的name值
            2. file绑定文件流对象
            3. file.name文件名
            4. file.file文件的字节流数据
        配置文件的访问路径和存储路径
        在setting.py中设置MEDIA相关配置;django把用户上传的文件统称为media资源
        django把用户上传的文件，统称为media资源
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR,'media')

        MEDIA_URL和MEDIA_ROOT需要手动绑定
        步骤：主路由中添加路由
            from django.conf import settings
            from django.conf.urls.static import static
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        说明：等价于做了MEDIA_URL开头的路由，django接到该特征请求后去MEDIA_ROOT路由查找资源

        文件写入方案1：传统的open方式
            @crsf_exempt    # 装饰器，用于避开crsf检查，与在模板里加{% crsf_token %}效果一样
            def upload_view(request):
                if request.method == 'GET':
                    return render(request,'test_upload.html')
                elif request.method == 'POST':
                    a_file = request.FILES['myfile']
                    print('上传的文件名是：'，a_file.name)
                    filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
                    with open(filename,'wb') as f:
                        data = a_file.file.read()
                        f.write(data)
                    return HttpResponse('接收文件：'+ a_file.name + '成功')

        文件写入方案1：借组ORM
        字段：fileField(upload='子目录名')
        @csrf_exempt
        def upload_view_dj(request):
            if request.method == 'GET':
                return render(request,'test_upload.html')
            elif request.method == 'POST':
                title = request.POST['title']
                a_file = request.FILES['myfile']
                content.objects.create(desc=title,myfile=a_file)
                return HttpResponse('--upload is ok--')

22. 发送邮件
    业务场景
        业务告警
        邮件验证
        密码找回
    邮件相关协议 - SMTP
        SMTP的全称是“Simple Mail Transfer Protocol”, 即简单邮件传输协议（25号端口）
        它是一组用于从源地址到目的地址传输邮件的规范，通过它来控制邮件的中转
        属于“推送”协议
    邮件相关协议 - IMTP
        IMTP全称是Internet Mail Access Protocol，即交互式邮件访问协议，是一个应用层协议（端口是143）
        用来从本地邮件客户端（Outlook Express、Foxmail、Mozilla Thunderbird等）访问远程服务器上的邮件
        属于“拉取”协议
    邮件相关协议 - POP3
        POP3是Post Office Protocol 3的简称，即邮局协议的第三个版本，是TCP/IP协议族中的一员（默认端口是110）
        本协议主要用于支持使用客户端远程管理服务器上的电子邮件
        属于”拉取“协议
    两者均为”拉取“型协议，负责从邮件服务器中下载邮件
    1. IMAP具备摘要浏览功能，可预览部分摘要，再下载整个邮件
    2. IMAP为双向协议，客户端操作可反馈给服务器

    1. POP3必须下载全部邮件，无摘要功能
    2. POP3为单向协议，客户端操作无法同步服务器

    django发邮件
        django中配置邮件功能，主要为SMTP协议，负责发邮件
        原理
            给Django授权一个邮箱
            django用该邮箱给对应收件人发送邮件
            django.core.mail封装了电子邮件的自动发送SMTP协议
        授权步骤     - 以QQ邮箱为例
            申请QQ号
            用QQ号登录QQ邮箱并修改设置
            -用申请到的QQ号和密码登陆到https://mail.qq.com/
            -修改”QQ邮箱”->设置->账号->“POP3/IMAP...服务”
        POP3/SMTP服务授权码：gkemuupwlumxgdbg
        IMAP/SMTP服务授权码：rcekgqocprebhggg

        函数调用
            from django.core import import mail
            mail.send_mail(
                subject,    #题目
                message,    #消息内容
                from_email  #发送者【当前配置邮件】
                recipient_list = ['xxx@qq.com',]    #接收者邮件列表
            )

22. 项目部署
    项目部署是指在软件开发完毕后，将开发机器上运行的软件实际安装到服务器上进行长期运行
    1. 在安装机器上安装和配置同版本的环境【py,数据库等】
    2. django项目迁移
        ubantu上
            sudo scp 项目地址
            请输入root密码：
    3. 用uWSGI替代python3 manage.py runserver方法启动服务器
    4. 配置nginx反向代理服务器
    5. 用nginx配置静态文件路径，解决静态路径问题

    WSGI
        Web Server Gateway Interface
        web服务器网关接口，是Python应用程序或框架和web服务器之间的一种接口，被广泛使用
        使用python manage.py runserver通常只在开发和测试环境中使用
        当开发结束后，完善的项目代码需要在一个高效稳定的环境中运行，这时可以使用WSGI

    uWSGI
        是WSGI的一种，它实现了http协议WSGI协议以及uwsgi协议
        uWSGI功能完善，支持协议众多，在python web圈热度极高
        uWSGI主要以学习配置为主

    uWSGI安装
        Ubuntu执行 sudo pip3 install uwsgi==2.0.18 -i https://pypi.tuna.tsinghua.edu.cn/simple/
        检查是否安装成功
        sudo pip3 freeze|grep -i 'uwsgi'
        如果成功安装，会输出uWSGI==2.0.18
    配置uWSGI
        添加配置文件 项目同名文件夹/uwsgi.ini
        文件以【uwsgi】开头，有如下配置
        套接字方式的IP地址：端口号【此模式需要有nginx】
        socket = 127.0.0.1:8000
        Http通信方式的IP地址：端口号
        http=127.0.0.1:8000
        项目当前工作目录
        chdir=项目绝对地址
        项目中wsgi.py文件的目录，相对与当前工作目录
        wsgi-file = my_project/wsgi.py
        进程个数
        process=4
        每个进程的线程个数
        threads=2
        服务的pid记录文件
        pidfile = uwsgi.pid
        服务的日志文件位置
        daemonize=uwsgi.log
        开启主进程管理模式
        master=True

    特殊说明：django的settings.py需要做如下配置
    1. 修改settings.py将DEBUG=True改为DEBUG=False
    2. 修改settings.py将ALLOWED_HOSTS=[]改为ALLOWED_HOSTS=['网站域名']或者['服务监听的ip地址']

    启动uwsgi
        cd到uWSGI配置文件所在目录
        uwsgi -- ini uwsgi.ini
    停止uwsgi
        cd到uWSGI配置文件所在目录
        uwsgi -- stop uwsgi.pid
    uwsgi的运行说明
        1. 无论是启动还是关闭，都需要执行ps aux|grep 'uwsgi'确认是否符合预期
        2. 启动成功后，进程在后台执行，所有日志均输出在配置文件所在目录的uwsgi.log中
        3. django中代码有任何修改，需要重新启动uwsgi

    uwsgi常见问题汇总
        1. 启动失败：端口被占用
            原因：有其他进程占用uwsgi启动的端口；
            解决方案：可执行sudo lsof -i:端口号，查询出具体进程，杀掉进程后，重新启动uwsgi即可
        2. 停止失败：stop无法关闭uwsgi
            原因：重复启动uwsgi，导致pid文件中的进程号失准
            解决方案：ps出uwsgi进程，手动kill掉

    Nginx
        Nginx是轻量级的高性能web服务器，提供了诸如HTTP代理和反向代理、负载均衡等一系列重要特性
        C语言编写，执行效率高
        nginx作用
            -负载均衡，多台服务器轮流处理请求
            -反向代理
        原理
            客户端请求nginx，再由nginx将请求转发uwsgi运行的django
        安装
            sudo apt install nginx
            如果下载速度很慢，考虑更换为国内源
            vim /etc/apt/sources.list
            更改国内源
            sudo apt-get update

            安装完毕后，ubuntu终端中输入nginx -v显示如下
            nginx version:nginx/1.14.0(Ubuntu)





ctrl+alt+l:格式化


