from django.shortcuts import render, redirect
from .forms import PracticeDjangoForm, ModelForm

def practice_form_view(request):
    if request.method == 'POST':
        form = PracticeDjangoForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = PracticeDjangoForm()

    return render(request, 'practice_form.html', {'form': form})

def model_form_view(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ModelForm()

    return render(request, 'model_form.html', {'form': form})

def home(request):
    return render(request, 'home.html')
