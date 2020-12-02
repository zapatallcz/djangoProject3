from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_task, name="index_task"),
    path('add', views.add_task, name="add_task"),
    path('update/<int:task_id>', views.update_task, name="update_task"),
    path('delete/<int:task_id>', views.delete_task, name="delete_task"),
    path('complete_task/<int:task_id>', views.complete_task, name="complete_task"),

]