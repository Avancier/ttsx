# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse

from hashlib import sha1
import datetime
from .models import UserInfo
from signal_decorators import user_login


# Create your views here.
def register(request):
    context = {'title': '注册', 'top': '0'}
    return render(request, 'tt_user/register.html', context)


def register_handler(request):
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    upwd2 = dict.get('cpwd')
    email = dict.get('email')

    if upwd != upwd2:
        return redirect('/user/register/')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = email

    user.save()

    return redirect('/user/login/')


def register_valid(request):
    uname = request.GET
    result = UserInfo.objects.filter(uname=uname).count()
    context = {'valid': result}
    return JsonResponse(context)


def login(request):
    uname = request.COOKIES.get('uname')
    context = {'title': '登录', 'top': '0', 'uname': uname}
    return render(request, 'tt_user/login.html', context)


def login_handler(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('user_pwd')
    uname_jz = post.get('name_jz', '0')
    print uname_jz
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    context = {'title': '登录', 'uname': uname, 'upwd': upwd, 'top': '0'}
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 0:
        context['name_error'] = '1'
        return render(request, 'tt_user/login.html', context)
    else:
        if users[0].upwd == upwd_sha1:
            request.session['uid'] = users[0].id
            request.session['uname'] = uname

            path = request.session.get('url_path', '/')
            response = redirect(path)

            if uname_jz == '1':
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            context['pwd_error'] = '1'
            return render(request, 'tt_user/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/user/login')


def islogin(request):
    result = 0
    if request.session.has_key('uid'):
        result = 1
    return JsonResponse({'islogin': result})


@user_login
def user_info(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    print user
    context = {'title': '用户信息', 'user': user}
    return render(request, 'tt_user/center.html', context)


@user_login
def user_order(request):
    print 'aaaaa'
    context = {'title': '用户订单'}
    return render(request, 'tt_user/order.html', context)


@user_login
def user_site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '收货地址', 'user': user}
    return render(request, 'tt_user/site.html', context)


"""
访问页面，记录当前页面地址
若没有登录，重定向登录页面
登录成功后重定向登录前页面

解决方案-》拦截器（中间件)
process_view
"""



