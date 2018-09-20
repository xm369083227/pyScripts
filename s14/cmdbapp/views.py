from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# def home(request):
#     return HttpResponse('<h1>HELLO Django</h1>')

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
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'admin' and pwd == "123":
            # 去跳转到
            return redirect('http://www.baidu.com')
        else:
            # 用户密码不配
            error_msg = "用户名或密码错误"
            #这里的‘error_msg’作为字典的key传到前台页面上的{{error_msg}}，与前台匹配
    return render(request,'login.html', {'error_msg': error_msg})

def home(request):
    user_list = [
        {'username':'uzi','age':21,'gender':'男'},
        {'username':'faker','age':22,'gender':'男'},
        {'username':'mlxg','age':23,'gender':'男'},
    ]
    if request.method == "POST":
        u = request.POST.get("username")
        a = request.POST.get("age")
        g = request.POST.get("gender")
        tmp = {'username': u, 'age': a, 'gender': g}
        user_list.append(tmp)
    return render(request,'home.html',{'user_list':user_list})