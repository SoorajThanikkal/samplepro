"""
URL configuration for books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from public import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg', views.reg),
    path('log', views.log),
    path('', views.index),
    path('addbooks', views.addbooks),
    path('failed', views.failed),
    path('logout', views.logout),
    path('btable', views.btable),
    path('bdelete', views.bdelete),
    path('edit', views.edit),
    path('bookedit', views.bookedit),
    path('wrong', views.wrong),
    path('buy', views.buy),
    path('bookbuy/', views.bookbuy, name='bookbuy'),
    path('success', views.success),
    path('Pro_fail', views.Pro_fail),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('edit_password/', views.edit_password, name='edit_password'),
  
]
