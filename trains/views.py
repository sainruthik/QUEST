from django.shortcuts import render
from .models import Train
from authentication import validate
from django.shortcuts import redirect
#station = Station.objects.all().distinct('name')
# Create your views here.
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
stations= set()
for i in Train.objects.all():
    stations.add(i.source)
stations = sorted(stations)
def index(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    try:
        k = request.POST
        print(k['destination'])
        des = k['destination']
        j = 0
        ans = []
        routes = Train.objects.filter(source=des)
        for i in routes:
            #print(jj)
            ans.append(['hello',i])
        return render(request, 'train/trainsearch.html',{'station':stations,'trains':ans,'days':days,'username':request.session['username']})

    except:
        print("from trains")
    return render(request, 'train/trainsearch.html',{'station':stations,'username':request.session['username']})