from django.shortcuts import render,redirect
from todo_app.models import todo_table
# Create your views here.
def frist(request):
    return render (request,'firstpage.html')
def second(request):
    return render(request,'addtodo.html')
def addtodo(request):
    if request.method=='POST':
        todolist=request.POST['todolist']
        todolist1=request.POST['enter']
        # datelist=request.POST['date']
        datasave=todo_table(todo=todolist,todo2=todolist1)
        datasave.save()
        return redirect('showpage')
    return render(request,'addtodo.html')
def showpage(request):
    todolists=todo_table.objects.all()
    return render(request,"tableshow.html",{'key':todolists})
def editing(request,num):
    edit_todo=todo_table.objects.get(id=num)

    return render(request,'edit.html',{'key':edit_todo})
def updatedatas(request,num):
    if request.method=='POST':
        updatedatas=todo_table.objects.get(id=num)
        updatedatas.todo=request.POST['todo1']
        updatedatas.todo2=request.POST['todo2']
        # updatedatas.todo=request.POST['date']
        updatedatas.save()
        return redirect('showpage')
def deleting(request,num):
    deletedatas=todo_table.objects.get(id=num)
    deletedatas.delete()
    
    return redirect('showpage')
    
    