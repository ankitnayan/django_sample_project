from django.urls import path

from . import views

urlpatterns = [
    
    path('2xx_success/', views.send_2xx, name='send_2xx'),
    path('4xx_not_found/', views.send_4xx, name='send_4xx'),
    path('5xx_exception/', views.send_5xx, name='send_5xx'),
]
