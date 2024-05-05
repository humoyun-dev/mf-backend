from django.urls import path
from .api import CustomUserLoginView, CustomUserLoadApi

urlpatterns = [
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('detail/', CustomUserLoadApi.as_view(), name='detail'),
]
