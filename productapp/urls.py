from django.urls import path
from . import views

app_name = 'productapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
]
