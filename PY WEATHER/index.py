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
            pass
        elif prikaz == 'graphpressure':
            pass
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
                if int(start) < int(date) < int(end):
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

prikazy = ['temp', 'humidity', 'pressure', 'maxtemp', 'maxhumidity', 'maxpressure', 'warmestcity' , 'coldestcity', 'graphtemp',
'graphpressure']

parametr = ['city', 'date', 'startdate', 'enddate']

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
    p.PrijmouPrikaz()

