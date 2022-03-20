from django.shortcuts import render
from api.models import Task

# Create your views here.
def dashboard(request):
    if request.method == 'POST':

        actions = request.POST.keys()
        if 'create' in actions:
            if request.POST['Title']:
                Task.objects.create(task=request.POST['Title'])
        if 'update' in actions:
            Task.objects.filter(id=request.POST['update']).update(task=request.POST['Title'])
        if 'delete' in actions:
            Task.objects.filter(id=request.POST['delete']).delete()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks if tasks else []
    }
    return render(request, 'frontend/list.html', context=context)
