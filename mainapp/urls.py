from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'mainapp'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('area/', views.area, name='area'),
    path('city/', views.city, name='city'),
    path('shops/<str:service>/<str:area>/', views.shoplist, name="shoplist"),
    path('items/<str:user>/', views.items, name="items"),
    path('edit-item/<str:user>/<int:id>', views.edititem, name="edititem"),
    path('completed-orders/<str:user>/', views.completedorders, name="completedorders"),
    path('pending-orders/<str:user>/', views.pendingorders, name="pendingorders"),
    path('order/', views.order, name="order"),
    path('profile/', views.profile, name="profile"),
    path('update-profile/<int:id>/', views.update_profile, name="update_profile"),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),

]
