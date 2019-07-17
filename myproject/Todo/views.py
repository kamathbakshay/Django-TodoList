from django.shortcuts import render
from .models import List
from django.http import HttpResponseRedirect


def todo_list(request):
    all_todo_items = List.objects.all()
    return render(request, 'Todo/index.html', {'all_todo_items':all_todo_items})

def addtodo(request):
    list_item = request.POST['list_item']
    List.objects.create(list_item = list_item)
    return HttpResponseRedirect('/todo/list/')

def deletetodo(request, todo_id):
    print("hai")       ###
    item_to_delete = List.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/list/')
