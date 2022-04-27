import json
import sys

class PrikazHandler:

    def __init__(self, kompletniPrikaz):
        self.kompletniPrikaz = kompletniPrikaz
        self.city = ''
        self.date = ''
        self.startdate = ''
        self.enddate = ''
    
    def PrijmouPrikaz(self):
        pole = self.kompletniPrikaz.split()
        prikaz = pole.pop(0)
        self.SpracovatPrikaz(prikaz, pole)

    def SpracovatPrikaz(self, prikaz, parametry):
        if prikaz == 'temp':
            self.showBasicInfo(parametry, 'temp')
        elif prikaz == 'humidity':
            self.showBasicInfo(parametry, 'relhum')
        elif prikaz == 'pressure':
            self.showBasicInfo(parametry, 'ap')
        elif prikaz == 'maxtemp':
            self.maxInfo(parametry, 'temp')
        elif prikaz == 'maxhumidity':
            self.maxInfo(parametry, 'relhum')
        elif prikaz == 'maxpressure':
            self.maxInfo(parametry, 'ap')
        elif prikaz == 'warmestcity':
            self.fistRankCity(parametry, 'warmestcity')
        elif prikaz == 'coldestcity':
            self.fistRankCity(parametry, 'coldestcity')
        elif prikaz == 'graphtemp':
            self.graphGenerate(parametry, 'temp')

        elif prikaz == 'graphpressure':
            self.graphGenerate(parametry, 'ap')
        else:
            print('Invalid input')
    
    def showBasicInfo(self, parametry, info):
        params = {'city': '', 'date': -1, 'startdate': -1, 'enddate': -1}

        for p in parametry:
            if p.split(':')[0] == 'city':
                params['city'] = p.split(':')[1]
            elif p.split(':')[0] == 'date':
                params['date'] = p.split(':')[1]
            elif p.split(':')[0] == 'startdate':
                params['startdate'] = p.split(':')[1]
            elif p.split(':')[0] == 'enddate':
                params['enddate'] = p.split(':')[1]

        if(params['city'] != ''):
            if(params['date'] != -1):
                try:
                    city = params['city']
                    date = params['date']
                    value = data[city][date][info]

                    if(info == 'relhum'):
                        info = 'humidity'
                        value = (int)(value*1000/10)
                    
                    if(info == 'ap'):
                        info = 'pressure'

                    print(f'city:{city} date:{date} {info}:{value}')
                except:
                    print('Invalid input')
    
    def maxInfo(self, parametry, info):
        params = {'city': '', 'date': -1, 'startdate': -1, 'enddate': -1}

        for p in parametry:
            if p.split(':')[0] == 'city':
                params['city'] = p.split(':')[1]
            elif p.split(':')[0] == 'date':
                params['date'] = p.split(':')[1]
            elif p.split(':')[0] == 'startdate':
                params['startdate'] = p.split(':')[1]
            elif p.split(':')[0] == 'enddate':
                params['enddate'] = p.split(':')[1]
        
        try:
            city = params['city']
            start = params['startdate']
            end = params['enddate']
            max = -1000
            maxDate = 0
            for date in data[city]:
                if int(start) <= int(date) <= int(end):
                    if data[city][date][info] > max:
                        max = data[city][date][info]
                        maxDate = date
            if max == -1000 or maxDate == 0:
                print('Invalid input')
            else:
                if(info == 'relhum'):
                    info = 'humidity'
                    max = (int)(max*1000/10)
                
                if(info == 'ap'):
                    info = 'pressure'

                print(f'city:{city} date:{maxDate} {info}:{max}')

        except:
            print('Invalid input')

    def fistRankCity(self, parametry, info):
        params = {'city': '', 'date': -1, 'startdate': -1, 'enddate': -1}
        for p in parametry:
            if p.split(':')[0] == 'city':
                params['city'] = p.split(':')[1]
            elif p.split(':')[0] == 'date':
                params['date'] = p.split(':')[1]
            elif p.split(':')[0] == 'startdate':
                params['startdate'] = p.split(':')[1]
            elif p.split(':')[0] == 'enddate':
                params['enddate'] = p.split(':')[1]

        date = params['date']
        

        if(info == 'warmestcity'):
            max = -1000
            result = {}
            for city in data.keys():
                if max < data[city][date]['temp']:
                    max = data[city][date]['temp']
                    result = {'city': city, 'date': date}
            warmestCity = result['city']
            warmestDate = result['date']
            print(f'city:{warmestCity} date:{warmestDate} temp:{max}')
        
        if(info == 'coldestcity'):
            min = 1000
            result = {}
            for city in data.keys():
                if min > data[city][date]['temp']:
                    min = data[city][date]['temp']
                    result = {'city': city, 'date': date}
            coldestCity = result['city']
            coldestDate = result['date']
            print(f'city:{coldestCity} date:{coldestDate} temp:{min}')

    def graphGenerate(self, parametry, info):
        params = {'city': '', 'date': -1, 'startdate': -1, 'enddate': -1}
        for p in parametry:
            if p.split(':')[0] == 'city':
                params['city'] = p.split(':')[1]
            elif p.split(':')[0] == 'date':
                params['date'] = p.split(':')[1]
            elif p.split(':')[0] == 'startdate':
                params['startdate'] = p.split(':')[1]
            elif p.split(':')[0] == 'enddate':
                params['enddate'] = p.split(':')[1]
        
        city = params['city']
        start = params['startdate']
        end = params['enddate']

        if(city == '' or start == '' or end == ''):
            print('Invalid input')
           
        else:
            maxTemp = -1000
            minTemp = 1000
            dateCount = 0
            for date in data[city]:
                if int(start) <= int(date) <= int(end):
                    dateCount += 1
                    if maxTemp < data[city][date][info]:
                        maxTemp = data[city][date][info]
                    if minTemp > data[city][date][info]:
                        minTemp = data[city][date][info]
            
            if(dateCount <= 50):
                sloupce =[]
                for date in data[city]:
                    if int(start) <= int(date) <= int(end):
                        sloupce.append(data[city][date][info])
                
                self.vykrasiGraph(sloupce)       

            else:

                average = dateCount % 50

                n1 = (dateCount//50) + 1
                n2 = (dateCount//50)

                tmp = []
                sloupce = []

                for date in data[city]:
                    if int(start) <= int(date) <= int(end):

                        tmp.append(data[city][date][info])

                        if average > 0:
                            if len(tmp) == n1:
                                sloupce.append((int)(sum(tmp))/n1)
                                tmp = []
                                average -= 1
                        
                        else:
                            if len(tmp) == n2:
                                sloupce.append((int)(sum(tmp))/n2)
                                tmp = []

                # print(sloupce)       
                self.vykrasiGraph(sloupce)

    def vykrasiGraph(self, pole):
        maxTemp = -1000
        minTemp = 1000
        for value in pole:
                if maxTemp < value:
                    maxTemp = value
                if minTemp > value:
                    minTemp = value
        
    
        step = (maxTemp - minTemp) / 19

        arrValueCol = []

        for value in pole:
            t = value
            n = round((t-minTemp) / step) + 1
            arrValueCol.append(n)

        arr = []
    
        for i in range (len(arrValueCol)):
            poleTmp = [' ']*20
            for j in range(arrValueCol[i]):
                poleTmp[j] = '#'
            arr.append(poleTmp)

        arr = [*zip(*arr)] #transpose

        for i in range (len(arr)-1, -1, -1):
            for j in range (len(arr[i])):
                print(arr[i][j], end='')
            print('', end='\n')

pole_kompletnichPrikazu = []

# Opening JSON file
f = open('data2.json')
data = json.load(f)
# Iterating through the json
# list
# print(data)
# print(data['Prague']['20210101'])
# for i in data:
#     print(data[i])
# Closing file
f.close()

for line in sys.stdin:
    p = PrikazHandler(line)
    try:
        p.PrijmouPrikaz()
    except:
        pass

