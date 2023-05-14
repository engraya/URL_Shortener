from django.urls import path
from . import views

urlpatterns = [
    path('shortenerPage', views.shortenerPage, name='shortenerPage'),
    path('createURL', views.createURL, name='createURL'),
    path('<str:pk>', views.goTO_URL, name='goTO_URL'),
    path('', views.landingPage, name="landingPage")
]