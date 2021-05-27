from django.shortcuts import redirect, render
from django.http import HttpResponse
# from .models import User, Profile

def error(request):
    return render(request, 'error.html')

def user_register_page(request):
    return render(request, 'account/user_register_page.html')
    
# def user_register_idcheck(request):
#     if(request.method == 'POST'):
#         username = request.POST['username']
#     else:
#         username = ''
    
#     idObject = User.objects.filter(username__exact=username)
#     idCount = idObject.count()
    
#     if idCount > 0:
#         msg = "<span>이미 존재하는 ID입니다.</span><input type='hidden' name='idcheck-result'\
#                id='IDCheckResult' value=0>"
#     else:
#         msg = "<span>사용할 수 있는 ID입니다.</span><input type='hidden' name='idcheck-result'\
#                id='IDCheckResult' value=1>"
               
#     return HttpResponse(msg)
    
# def user_register_result(request):
#     if(request.method == "POST"):
#         username = request.POST['username']
#         password = request.POST['password']
#         last_name = request.POST['last_name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         date_of_birth = request.POST['date_of_birth']
        
#     try:
#         if username and User.objects.filter(username__exact=username).count() == 0:
#             profile = Profile()
#             user = User.objects.create_user(\
#                 username, password, last_name, email, phone, date_of_birth)
#             profile.user = user
#             profile.save()
            
#             redirection_page = "account:registercompleted"
#         else:
#             redirection_page = "account:error"
#     except:
#         redirection_page = "account:error"
    
#     return redirect(redirection_page)
    
# def user_register_completed(request):
#     return render(request, 'account/user_register_completed.html')