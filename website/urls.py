"""
URL configuration for MessMe project.

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
from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    #path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('mess/<int:pk>',views.mess_meu, name='mess'),
    path('delete_menu/<int:pk>',views.delete_menu, name='delete_menu'),
    path('add_menu/<int:pk',views.add_menu, name='add_menu'),
    path('menu/',views.menuee,name='menu')
    
        ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
