from django.urls import path
from . import views

# placeholder for easy access to the urls of the TASK APP
app_name = 'TASK'

urlpatterns = [
    path('<str:task_id>/completed/<str:action>', views.completeTask, name='COMPLETED'),
    path('<str:task_id>/delete/', views.deleteTask, name="DELETE")
]
