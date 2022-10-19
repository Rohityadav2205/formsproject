from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index),
    path('form/', views.form),

    path('bookform/', views.bookform, name='bookform'),

    path('Student/', views.Studentview, name='Student'),
    path('', views.index),
    # path('create/', views.createuser),
    path('create/', views.createUser),
    path('changepassword/', views.changepassword),
    path('login/', views.authenticateuser),
    path('logout/', views.dologout),
    path("logincheck/", views.onlyloggedin),

]
