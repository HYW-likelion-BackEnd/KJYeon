from django.shortcuts import render, redirect

from .models import List
from .forms import ListForm

# Create your views here.
def f_list(request) :
    lists = List.objects.all()
    return render(request, 'list/list.html', {'lists': lists})

def f_detail(request, pk) :
    list = List.objects.get(id=pk)
    return render(request, 'list/detail.html', {'list' : list})

def f_post(request) :
    if request.method == "POST" :
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.save()
            return redirect('f_list')
    else :
        form = ListForm()
    return render(request, 'list/create.html', {'form':form})

def f_edit(request, pk) :
    list = List.objects.get(id=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            list = form.save(commit=False)
            list.save()
            return redirect('f_list')
    else :
        form = ListForm(instance=list)
    return render(request, 'list/update.html', {'form':form})

def f_delete(request, pk) :
    list = List.objects.get(id=pk)
    if request.method == "POST" :
        list.delete()
        return redirect('f_list')
    return render(request, 'list/delete.html', {'list':list})
