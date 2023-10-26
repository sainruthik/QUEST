from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
import requests
import json
import string
from places.models import TouristPlaces
from django.db.models import Q
from authentication import validate
from django.shortcuts import redirect
from trains.models import Train
from Restaurants.apiFunctions import savindbrestaurants
from trains.apiFunctions import aboutTrain,stationCode,trainsInStations,codeToName,saveindb
from Hotels.models import Hotel
from Restaurants.models import Restaurant
states = []
stateImages = []
categories = [['Historical places','historical'],['Beaches','beaches'],['National parks','parks'],['Hill stations','hills'],['temples','temples'],['cities','cities']]
with open("./project/static/statesImages.txt",'r') as fi:
    j = 0
    for i in fi.readlines():
        li = [j]+ list(i.rsplit(maxsplit=1))
        stateImages.append(li)
        j+=1
#print(stateImages)
#saveInDatabase('')
'''
k = TouristPlaces.objects.distinct('district')
j = 0
for i in k[273:]:
    print(j,i.district)
    j+=1
    try:
        stcode = stationCode(i.district)
        for ii in stcode:
            tra = trainsInStations(ii)
            mm = 0
            for jj in tra:
                mm+=1
                if mm>15:
                    break
                kk = aboutTrain(jj)
                print(kk)
                dayname=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
                daystr = ''
                for i in dayname:
                    daystr += str(kk['days'][i])
                #print(daystr)
                trainobj = Train(no=kk['no'],arrival=kk['arrival'],name=kk['name'][:min(49,len(kk['name']))],departure=kk['departure'],source=kk['source'],destination=kk['destination'],days=daystr)
                print(trainobj.save())
    except:
        print('error occured')
k = Train.objects.distinct('source')
l = Train.objects.distinct('destination')

for i in k:
    li.append(i.source)
for i in l:
    li.append(i.destination)
li = set(li)
print(len(li))
saveindb(li)      


districts = TouristPlaces.objects.all().distinct('district')
j = 0
#print(districts[115].district)
for i in districts[118:]:
    print(i.district)
    savindbrestaurants(i.district,i.state)
#saveindb()
objs = Train.objects.all()
for i in objs:
    obj1 = Station.objects.filter(code=i.destination)
    obj2 = Station.objects.filter(code=i.source)
    i.destination = i.destination + ', '+obj1[0].name
    i.source = i.source + ', '+obj2[0].name
    i.save()
    print(i.source,i.destination)
'''
def index(request):
    print("from home ind")
    if validate.alreadyLoggedIN(request):
        return redirect('/home')
    return render(request, 'home/landingpage.html',{'message':'Login/Signup to continue'})

def home(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'home/home.html', {'range':range(10),'imageUrl':'https://tse1.mm.bing.net/th?id=OIP.p-qglTQvUYPA_bR0R9Eu3AHaEy&pid=Api','states':stateImages,'categories':categories,'username':request.session['username'],'message':'welcome '+request.session['username']+' !!'})

def places(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    ind = request.path.rsplit('/',1)
    if(ind[0]=="/states"):
        place = stateImages[int(ind[1])][1]
        places = TouristPlaces.objects.all().filter(Q(state=place) & ~Q(category=7315023) & ~Q(category=7314003) )
    elif ind[0]=="/categories":
        if ind[1]=='beaches':
            places = TouristPlaces.objects.all().filter(category=9357)
        elif ind[1]=='historical':
            places = TouristPlaces.objects.all().filter(category=7376003)
        elif ind[1]=='temples':
            places = TouristPlaces.objects.all().filter(category=7339005)
        elif ind[1]=='hills':
            places = TouristPlaces.objects.all().filter(Q(category=7337) | Q(category=7376004))
        elif ind[1]=='parks':
            places = TouristPlaces.objects.all().filter(name__contains="Park")
    placefinal = []
    for i in places:
        placefinal.append([i,list(i.address.split(',')),i.imageurl])
    placefinal.sort(key = lambda x: x[2],reverse=True)
    #print(places)
    #places = placesByStates(place)
    #print("here -->",places)
    return render(request, 'home/placeslist.html', {'places':placefinal,'username':request.session['username'],'categories':categories,'states':stateImages})

def historical(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/historical.html', {'placename':"HISTORICAL PLACES",'username':request.session['username']})

def place(request):
    ind = request.path.rsplit('/',1)
    print(ind)
    place = TouristPlaces.objects.filter(name=ind[1])
    place = place[0]
    print(place)
    district = place.district
    hotels = Hotel.objects.filter(district=district)
    restaurants = Restaurant.objects.filter(district=district)
    address = place.address.split(',')
    return  render(request, 'home/hotels.html', {'place':place,'address':address,'username':request.session['username'],'hotels':hotels,'restaurants':restaurants})

def cities(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/cities.html', {'placename':"MAJOR CITIES",'username':request.session['username']})

def parks(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/parks.html', {'placename':"NATIONAL PARKS",'username':request.session['username']})

def beaches(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/beaches.html', {'placename':"BEACHES",'username':request.session['username']})

def temples(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/temples.html', {'placename':"TEMPLES",'username':request.session['username']})

def hills(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'places/hills.html', {'placename':"HILL STATIONS",'username':request.session['username']})

def aboutus(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'home/aboutus.html', {'username':request.session['username']})

def blog(request):
    if not validate.alreadyLoggedIN(request):
        return redirect('/login/login')
    return render(request, 'blogs/blog.html', {'li':list(range(10)),'username':request.session['username']})