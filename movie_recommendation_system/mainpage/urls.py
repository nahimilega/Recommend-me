from django.urls import path
from . import views

app_name='mainpage'
urlpatterns=[
    #/music/
    #path('',views.index,name='index'),
    path('result',views.result,name='result'),
    path('form',views.form,name='form'),
    path('store_data',views.store_data,name='store_data')

]