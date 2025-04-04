from django.urls import path
from .views import add_app, get_app, delete_app

urlpatterns = [
    path('api/add-app/', add_app, name='add-app'),
    path('api/get-app/<int:id>/', get_app, name='get-app'),
    path('api/delete-app/<int:id>/', delete_app, name='delete-app'),
]
