from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

def home(request):
    return HttpResponse('<h1>HELLO Django</h1>')

# def login(request):
#     #print(request.method)
#     error_msg = ""
#     if request.method == "POST":
#         # 这里的user，pwd指前台传过来的id
#         user = request.POST.get("user", None)
#         pwd = request.POST.get("pwd", None)
#         if user == "root" and pwd =="123":
#             #重定向
#             print(1)
#             return redirect('http://www.baidu.com')
#         else:
#             error_msg = "请输入正确的用户名密码。。"
#     return render(request,'login.html',{'error_msg':error_msg})

def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        if user == 'admin' and pwd == "123":
            # 去跳转到
            return redirect('http://www.baidu.com')
        else:
            # 用户密码不配
            error_msg = "用户名或密码错误"

    return render(request,'login.html', {'error_msg': error_msg})