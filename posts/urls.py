from django.urls import path
from . import views
urlpatterns = [
path('home/', views.home,name='home'),
path("<int:id>/",views.post,name='post') # 13 value will be passed to the post function in views.py file
]