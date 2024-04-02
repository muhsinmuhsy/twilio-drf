from django.urls import path
from .views import *

urlpatterns = [
    path('user/list', UserList.as_view(), name='user-list')
]