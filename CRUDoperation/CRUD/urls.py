from django.urls import path
from . import views

urlpatterns = [
    path('', views.showEmp, name="showEmp"),
    path('insert', views.insertTemp, name = "insertTemp"),
    path('edit/<int:id>', views.editTemp, name = "editTemp"),
    path('update/<int:id>', views.updateTemp, name = "updateTemp"),
    path('delete/<int:id>', views.delTemp, name = "delTemp")

]