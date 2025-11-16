from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_content, name='add_content'),
    path('api/content/', views.content_api, name='content_api'),
    path('display/', views.display_content, name='display_content'),
]
