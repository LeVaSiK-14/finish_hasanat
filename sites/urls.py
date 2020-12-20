from django.urls import path
from .views import *
from . import views

urlpatterns = [
	path('index/', views.index, name='index'),
	path('product/', views.product, name='product'),
	path('second/', views.second, name='second'),
	path('three/', views.three, name='three'),
	path('four/', views.four, name='four'),
	path('five/', views.five, name='five'),
	path('six/', views.six, name='six'),
	path('seven/', views.seven, name='seven'),
	path('projects/', views.projects, name='projects'),
	path('news/', views.news, name='news'),
	path('nine/', views.nine, name='nine'),
	path('ten/', views.ten, name='ten'),
	path('eleven', views.eleven, name='eleven'),
	path('slider/', views.slider, name='slider'),
	path('five_blocks/', views.five_blocks, name='five_blocks'),
	path('detail_five/', views.detail_five, name='detail_five'),
]