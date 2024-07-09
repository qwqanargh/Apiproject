from django.urls import path

from . import views


urlpatterns = [
    path('shirts/', views.objects_list),
    path('shirts/<int:id>/', views.current_object),
]
