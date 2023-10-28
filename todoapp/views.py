from django.shortcuts import redirect, render
from todoapp.forms import todoform
from django.views.generic import ListView
from todoapp.models import task

# Create your views here.
def home (request):
    task1 = task.objects.all()
    if request.method == 'POST':
        name =  request.POST.get('name', '')
        priority = request.POST.get('priority' ,'')
        date =  request.POST.get('date','')
        
        t1 = task(name= name ,priority = priority , date = date)
        t1.save()

    return render(request,'home.html',{'task1':task1} )


def delete(request,taskid):
    t1 = task.objects.get(id = taskid)

    if request.method == "POST":
        t1.delete()
        return redirect('/')
    return render(request,'delete.html')


from django.shortcuts import render, redirect
from .models import task
from .forms import todoform

def edit(request, id):
    t1 = task.objects.get(id=id)
    f = todoform(request.POST or None, instance=t1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 't1': t1})


def task_lists(request):
    completed_tasks = task.objects.filter(status='completed')
    pending_tasks = task.objects.filter(status='pending')
    expired_tasks = task.objects.filter(status='expired')

    return render(request, 'task_lists.html', {
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'expired_tasks': expired_tasks,
    })


class tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task1'