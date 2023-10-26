import requests
import json
from .models import Train
def aboutTrain(train_no):
    url = "https://trains.p.rapidapi.com//"
    payload = "{\r\"search\": \""+train_no+"\"\r}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "34f621ddcamshe18d69e8bb8da23p120327jsnb7af2ffa6b93",
        'x-rapidapi-host': "trains.p.rapidapi.com"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    res = json.loads(response.text)
    dic = {}
    for i in res:
        dic['no'] = i['train_num']
        dic['name'] = i['name']
        dic['source'] = i['train_from']
        dic['destination'] = i['train_to']
        dic['days'] = i['data']['days']
        dic['arrival'] = i['data']['arriveTime'][:5]
        dic['departure'] = i['data']['departTime'][:5]
    #print(li)
    return dic

#print(aboutTrain('12235'))
def stationCode(station):

    url = "https://indianrailways.p.rapidapi.com/findstations.php/findstations.php"

    querystring = {"station":station}

    headers = {
        'x-rapidapi-key': "34f621ddcamshe18d69e8bb8da23p120327jsnb7af2ffa6b93",
        'x-rapidapi-host': "indianrailways.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    ans = json.loads(response.text)
    ans = ans['stations']
    l = []
    for i in ans:
        l.append(i['stationCode'])
    return l


def trainsInStations(stationcode):
    key = '3e51e63c0949cba00e4ec2dcd15982ca'
    url = 'http://indianrailapi.com/api/v2/AllTrainOnStation/apikey/{0}/StationCode/{1}/'.format(key,stationcode)
    tmp = json.loads(requests.get(url).text)
    trainList = []
    for i in tmp['Trains']:
        trainList.append(i['TrainNo'])
    trainList = set(trainList)
    return trainList

def codeToName(stationcode):
    key = '3e51e63c0949cba00e4ec2dcd15982ca'
    url = 'http://indianrailapi.com/api/v2/StationCodeToName/apikey/{0}/StationCode/{1}/'.format(key,stationcode)
    tmp = json.loads(requests.get(url).text)
    #print(tmp['Station']['NameEn'])
    return tmp['Station']['NameEn']

def saveindb():
    disno = Train.objects.all().distinct('no')
    for i in disno:
        no = i.no
        print(no)
        key  = '3e51e63c0949cba00e4ec2dcd15982ca'
        #url = "http://indianrailapi.com/api/v2/TrainBetweenStation/apikey/{0}/From/KZJ/To/LTT".format(key)
        url = 'http://indianrailapi.com/api/v2/TrainSchedule/apikey/{0}/TrainNumber/{1}/'.format(key,no)
        res = requests.get(url)
        res = json.loads(res.text)
        #print(res)
        res = res['Route']
        li = []
        for i in res:
            li.append([i['StationCode'],i['ArrivalTime']+','+i['DepartureTime']])
        print(li)
        tmp = ['none','none']
        if len(li)>12:
            li = li[:12]
        elif len(li)<12:
            kk = []
            for i in range(12-len(li)):
                kk.append(tmp)
            li = li + kk
        obj = TrainRoutes(no=no,source1=li[0][0],time1=li[0][1],source2=li[1][0],time2=li[1][1],source3=li[2][0],time3=li[2][1],source4=li[3][0],time4=li[3][1],source5=li[4][0],time5=li[4][1],source6=li[5][0],time6=li[5][1],source7=li[6][0],time7=li[6][1],source8=li[7][0],time8=li[7][1],source9=li[8][0],time9=li[8][1],source10=li[9][0],time10=li[9][1],source11=li[10][0],time11=li[10][1],source12=li[11][0],time12=li[11][1])
        obj.save()

    
    