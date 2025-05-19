from django.urls import path
from . import views
from django.shortcuts import render


urlpatterns=[
    path('',views.message_chat,name='chat-message'),
    path("api/login/", views.LoginView.as_view(), name="custom_login"),
    path("login_page/", lambda request: render(request, "login_page.html"), name="login_page"),

]