import json,requests
from places.models import TouristPlaces
def placesByStates(place):
    gl = json.dumps([place[2]])
    #print(gl)
    key = "iB4D6jntYlOdin6qwWqjJpGndY8Dqnbp"
    url = "https://api.tomtom.com/search/2/geometrySearch/IMPORTANT_TOURIST_ATTRACTION.json?key={0}&geometryList={1}&categorySet=9457,7339005,7376003,9927003,9927004,9927005,7376&limit=30".format(key,gl)
    res = json.loads(requests.get(url).text)['results']
    places = []
    for i in res:
        iid = i['poi']['categorySet'][0]['id']
        if int(iid)==7376002 :
            continue
        name = i['poi']['name']
        address = i['address']['freeformAddress']
        state = i['address']['countrySubdivision']
        district = i['address']['countrySecondarySubdivision']
        lat = i['position']['lat']
        lon = i['position']['lon']
        image = imageUrl(name)
        try:
            TouristPlaces.objects.get(name=name)
        except:
            if len(name)<50 and len(address)<500 and len(state)<50 and len(district)<50 and len(image)<200:
                k = TouristPlaces(name=name,address=address,state=state,district=district,lat=lat,lon=lon,imageurl=image,category=iid)
                k.save()

def saveInDatabase(place):
    key = "iB4D6jntYlOdin6qwWqjJpGndY8Dqnbp"
    url = "https://api.tomtom.com/search/2/search/water hole.json?key={0}&countrySet=IN&limit=100&categorySet=7376004".format(key)
    res = json.loads(requests.get(url).text)['results']
    places = []
    for i in res:
        iid = i['poi']['categorySet'][0]['id']
        if int(iid)==7376002 :
            continue
        name = i['poi']['name']
        address = i['address']['freeformAddress']
        state = i['address']['countrySubdivision']
        district = i['address']['countrySecondarySubdivision']
        lat = i['position']['lat']
        lon = i['position']['lon']
        try:
            TouristPlaces.objects.get(name=name)
        except:
            image = imageUrl(name)
            if len(name)<50 and len(address)<500 and len(state)<50 and len(district)<50 and len(image)<200:
                k = TouristPlaces(name=name,address=address,state=state,district=district,lat=lat,lon=lon,imageurl=image,category=iid)
                k.save()


def changingUrl():
    li = TouristPlaces.objects.all()
    for i in li:
        name = i.name
        img = imageUrl(name)
        i.imageurl = img
        i.save()

def deleteObject():
    kk = '''Hanuman Mandir, Chalis Bigha
    Hanuman Mandir, Kurudgi Kh
    Gcie Lio Statue
    Astana A Jamal Dargah Char Kutub
    Meho Ji Smarak
    Rukmani Smarak
    Maqbara Ahmad Ali Shah
    Trans Tower
    Pravasi Thattukada
    Panchayat Cheruvu
    Pampla Cheruvu
    Sultan Pokhar
    Eliers Tank
    Ahla Vg
    Aman Talab
    Aman Talab
    Mitha Talab
    Ameer Ganj Talab
    Nirmaan Excursion Yodhasthal
    Jogi Talav
    Big Chowk Man Point
    Bhosagar
    Panigrahi Pond
    Shri Devnarayan Veer Gurjar Ghat
    Karunasamy Kovil Kulam
    Arni Surya Kulam'''
    for i in kk.split('\n'):
        j = i.strip()
        print(j)
        k = TouristPlaces.objects.all().filter(name=j)
        print(k)
        k.delete()
        #TouristPlaces.save()

def imageUrl(name):
    '''
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"
    querystring = {"pageNumber":"1","pageSize":"10","q":name,"autoCorrect":"false","safeSearch":"true"}
    headers = {
        'x-rapidapi-key': "b7950242dbmsh896e4e949798a68p1a4a56jsn6aa4653dbb2b",
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    '''

    url = "https://rapidapi.p.rapidapi.com/images/search"
    querystring = {"q":name+" place","count":"5"}
    headers = {
        'x-rapidapi-key': "34f621ddcamshe18d69e8bb8da23p120327jsnb7af2ffa6b93",
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    kk = json.loads(response.text)
    try:
        result = kk['value'][0]['thumbnailUrl']
    except:
        result = ""
    if name=="Kotha Cheruvu":
        result=""
    print(result)
    return result