from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('signup/',views.signup,name="signup"),
    path('account/', views.accountProfile, name='account'),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name="users/change_password.html"),name="change_password"),
    path('changepassword/done/',auth_views.PasswordChangeDoneView.as_view(template_name="users/change_password_done.html"),name="change_passworddone"),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('create-skill/', views.createSkill, name='create-skill'),
    path('edit-skill/<str:pk>/', views.editSkill, name='edit-skill'),
    path('delete-skill/<str:pk>/', views.deleteSkill, name='delete-skill'),
]
