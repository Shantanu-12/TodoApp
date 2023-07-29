from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def insert(request):
    if request.method=="POST":
        data=request.POST
        detail=data.get("title")
        description=data.get("description")
        date=data.get("dateTime")

        Todo.objects.create(
            title=detail,
            description=description,
            dateTime=date
        )
        return redirect('/insert/')
    querySet=Todo.objects.all()
    context={'inserts':querySet}
    return render(request,"insert.html",context)

def update(request,id):
    querySet=Todo.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        detail=data.get("title")
        description=data.get("description")
        date=data.get("dateTime")

        querySet.title=detail
        querySet.description=description
        querySet.dateTime=date
        querySet.save()
        return redirect('/insert/')
    context={"updates":querySet}
    return render(request,"update.html",context)

def delete(request,id):
    querySet=Todo.objects.get(id=id)
    querySet.delete()
    return redirect('/insert/')



