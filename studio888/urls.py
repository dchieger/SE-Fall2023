"""
URL configuration for studio888 project.

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
from django.urls import path
from authentication.views import Signup, Signin, Profile

from django.contrib import admin
from django.urls import path
from authentication import views
<<<<<<< HEAD
=======
from store.views import order_detail, create_order
>>>>>>> david

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', Signup.as_view(), name='signup'),
    path('signin/', Signin.as_view(), name='signin'),
    path('profile/', views.Profile, name='profile'),
<<<<<<< HEAD
]
=======
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('create_order/', create_order, name='create_order'),
]
>>>>>>> david
