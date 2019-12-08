from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Squirrel
from .forms import SqForm

def homepage(request):
    maps = 'Map'
    sightings = 'Sightings'
    add = 'Add'
    stats = 'Stats'
    context = {
        'maps': maps,
        'sightings': sightings,
        'add': add,
        'stats': stats,
    }
    return render(request, 'sightings/homepage.html', context)

def sightings(request):
    sq = Squirrel.objects.all()
    add = 'Add Here'
    context = {
        'sq': sq,
        'add': add,
    }
    return render(request, 'sightings/sightings.html', context)

def map(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/map.html', context)

def edit_sq(request, UID):
    Sq = Squirrel.objects.get(Unique_Squirrel_ID=UID)
    if request.method == 'POST':
        form = SqForm(request.POST, instance=Sq)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SqForm(instance=Sq)

    context = {
        'form': form,
    }
    
    return render(request, 'sightings/edit.html', context)

def add_sq(request):
    if request.method == 'POST':
        form = SqForm(request.POST)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SqForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/edit.html', context)

def stats(request):
    sq = Squirrel.objects.all()
    count = 0
    Running = 0
    Chasing = 0
    Climbing = 0
    Eating = 0
    Foraging = 0
    Kuks = 0
    Quaas = 0
    for s in sq:
        count += 1
        Running += s.Running
        Chasing += s.Chasing
        Climbing += s.Climbing
        Eating += s.Eating
        Foraging += s.Foraging
        Kuks += s.Kuks
        Quaas += s.Quaas
    RP = "{:.2%}".format(Running/count)
    CP = "{:.2%}".format(Chasing/count)
    CLP = "{:.2%}".format(Climbing/count)
    EP = "{:.2%}".format(Eating/count)
    FP = "{:.2%}".format(Foraging/count)
    KP = "{:.2%}".format(Kuks/count)
    QP = "{:.2%}".format(Quaas/count)
    context = {
           'rp': RP,
           'cp': CP,
           'clp': CLP,
           'ep': EP,
           'fp': FP,
           'kp': KP,
           'qp': QP,
    }
    return render(request, 'sightings/stats.html', context)
