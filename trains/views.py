from django.shortcuts import render,redirect
from trains.models import Trains
from random import randint
from .forms import TrainsForm

def accueil(request):
    trains = Trains.objects.all()
    n = trains.count()
    return render(request, 'trains/accueil.html',{
        'trains': trains,
        'n' : n
    })
def show(request,train_id):
    train = Trains.objects.get( id =train_id )
    n = Trains.objects.all().count()
    return render(request, 'trains/show.html',{
        'id' : train.id,
        'depart' : train.depart,
        'destination' : train.destination,
        'arrets' : train.arrets,
        'h_depart' : train.h_depart,
        'h_arrivee' : train.h_arrivee,
        'n' : n,
        
    })
def random(request):
    n = Trains.objects.all().count()
    r = randint(0,n-1)
    train = Trains.objects.all()[r]

    return render(request, 'trains/random.html',{
        'id' : train.id,
        'depart' : train.depart,
        'destination' : train.destination,
        'arrets' : train.arrets,
        'h_depart' : train.h_depart,
        'h_arrivee' : train.h_arrivee,
    })




def create(request):
    form = TrainsForm()
    if request.method == 'POST':
        form = TrainsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/trains/accueil')
    return render(request,'trains/create.html',{'form':form})