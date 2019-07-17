from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.todo_list, name='todo_list'),
    path('addtodo/', views.addtodo, name = 'addtodo'),
    path('deletetodo/<int:todo_id>', views.deletetodo, name = 'deletetodo')
]
