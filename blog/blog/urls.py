"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from blogA.views import Content_Add_View
from blogA.views import Content_Update_View
from blogA.views import Content_Delete_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', Content_Add_View.as_view(), name='add'),
    path('upd/<int:pk>/', Content_Update_View.as_view(), name='upd'),
    path('del/<int:pk>/', Content_Delete_View.as_view(),name='del')
    
]
