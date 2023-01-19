"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .appforms import AnimalForm, SearchAnimal
from .models import Animal
from django.contrib.admin.views.decorators import staff_member_required

data = []

def home(request):
    global data
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.POST:
        form = SearchAnimal(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            animal_type = form_data['filter_type']
            animal_class=form_data['filter_class']
            size=form_data['filter_size']
            activity_level=form_data['filter_activity_level']
            data = Animal.objects.filter(
                likes_kids=form_data['filter_likes_kids'],
                likes_cats=form_data['filter_likes_cat'],
                likes_dogs=form_data['filter_likes_dog'],
                
                )
            if animal_type.lower() !='any': data = data.filter(animal_type=animal_type)
            if animal_class.lower() != 'any': data = data.filter(animal_class=animal_class)
            if size.lower() != 'any':  data = data.filter(size=size)
            if size.lower() != 'any':  data = data.filter(size=size)
            if activity_level.lower() != 'any':  data = data.filter(activity_level=activity_level)
            data=data.values()
        return redirect('search/results/')
    form = SearchAnimal()
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'form': form
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

# @staff_member_required
def profileForm(request):
    if request.method == "POST":
        animalform = AnimalForm(data=request.POST, files=request.FILES)
        if animalform.is_valid:
            animalform.save()
            return redirect('/')
    else:
        animalform = AnimalForm()
    return render(
                request,
                'app/add.html',
                {
                    'form': animalform
                }
            )

def SearchPage(request):
    print(data)
    return render(request,
                'app/search_Result.html', {'data': data})

def editAdd(request):
    animals = Animal.objects.all().values()
    return render(request, 'app/modify.html', {'animals': animals})

def edit(request, id):
    instance=Animal.objects.get(id=id)
    if request.method == "POST":
        animalform = AnimalForm(data=request.POST, files=request.FILES, instance=instance)
        if animalform.is_valid:
            animalform.save()
            return redirect('/')
    else:
        animalform = AnimalForm(instance=instance)
    return render(
                request,
                'app/edit.html',
                {
                    'form': animalform
                }
            )