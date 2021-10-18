from django.urls import path

from etudiant import views

urlpatterns = [
    path('', views.index, name='index'),

]
