
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('budget.urls')),
    path('register/', user_views.register, name='register'),
    path('home/', auth_views.LoginView.as_view(template_name='users/signin.html'), name='home'),
    path('signout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='signout'),
    path('users/', user_views.manage_users , name='users-list')
]
