"""
URL configuration for Sample project.

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
from app.views import Student_Add_View
# from app.views import Employee_Add_View
from app.views import Home
from app.views import Student_List_View
from app.views import Student_Update_View
from app.views import Student_Delete_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',Student_Add_View.as_view(),name='add'),
    # path('emp/',Employee_Add_View.as_view(),name='add'),
    path("",Home.as_view(),name='home'),
    path('all/',Student_List_View.as_view(),name='all'),
    path('upd/<int:pk>',Student_Update_View.as_view(),name='upd'),
    path('del/<int:pk>',Student_Delete_View.as_view(),name='del')
    
]
