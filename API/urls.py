from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'GetCardInfo',views.UserATMView, basename='UserATM')
router.register(r'AuthenticCard',views.AuthenticUserView, basename='AuthenticUser')
router.register(r'UserWithDrawal',views.UserWithDrawal, basename='UserWithDrawal')
router.register(r'DepositMoney',views.DepositMoney, basename='DepositMoney')




urlpatterns = [
    path('',include(router.urls)),
    ]
