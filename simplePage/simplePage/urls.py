"""
URL configuration for simplePage project.

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
from django.urls import path, include
from videojuegos import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('videogames/', views.videogame_list, name='videogame_list'),
    path('videogames/create/', views.videogame_create, name='videogame_create'),
    path('videogames/<int:pk>/update/', views.videogame_update, name='videogame_update'),
    path('videogames/<int:pk>/delete/', views.videogame_delete, name='videogame_delete'),
    path('videogames/<int:videogame_id>/order/', views.create_order, name='create_order'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('videogames/<int:pk>/', views.videogame_detail, name='videogame_detail'),
    path('my-orders/', views.user_orders, name='user_orders'),
]
