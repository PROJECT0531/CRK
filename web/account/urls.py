from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(
    #     template_name='account/password_change.html'), name='password_change'),
    # path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
    # template_name='account/password_change_done.html'), name='password_change_done'), 
    path('user_register/', views.user_register_page, name='register'),
    # path('user_register_idcheck/', views.user_register_idcheck, name='registeridcheck'),
    # path('user_register_res/', views.user_register_result, name='registerres'),
    # path('user_register_completed/', views.user_register_completed, 
    # name='registercompleted'),
    path('error/', views.error, name='error'),
    
]
