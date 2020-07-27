from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tracker/', views.tracker, name='track'),
    path('search/', views.search, name='search'),
    path('product/<int:myid>', views.productView, name='product'),
    path('checkout/', views.checkout, name='checkout'),
    path('handlerequest/', views.handlerequest, name='request'),
]
