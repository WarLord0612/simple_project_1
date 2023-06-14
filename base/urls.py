from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,'home'),
    path('/count',views.count,name='count')


    
]