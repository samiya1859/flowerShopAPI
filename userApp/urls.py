from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

routers = DefaultRouter()
routers.register('list',views.UserModelViewset)

urlpatterns = [
    path('',include(routers.urls)),
    path('register/',views.UserRegistrationAPIView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]
