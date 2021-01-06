from django.urls import path

from .import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    # path('test/', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('session/', views.catalogue_session, name='session'),
]