import requests
import json
from Hotels.models import Hotel
def savindbrestaurants(district,state):
    key = "iB4D6jntYlOdin6qwWqjJpGndY8Dqnbp"
    t = "Hotels in {0} countrySubdivision='{1}'".format(district,state)
    url = "https://api.tomtom.com/search/2/search/{1}.json?key={0}&countrySet=IN&limit=30".format(key,t)
    try:
        res = json.loads(requests.get(url).text)['results']
        jj = 0
        for i in res:
            name = i['poi']['name']
            categories = ''
            for j in i['poi']['categories']:
                categories += j + ', '
            address = i['address']['freeformAddress']
            dis = i['address']['countrySecondarySubdivision']
            if jj==5:
                break
            if district==dis:
                jj+=1
                obj = Hotel(name=name[:min(len(name),30)],categories=categories[:min(len(categories),30)],address=address[:min(len(address),50)],district=dis)
                obj.save()
    except:
        #till hamirpur
        print('error occured')
    
