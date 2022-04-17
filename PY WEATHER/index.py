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
            self.showInfo(parametry, 'temp')
        elif prikaz == 'humidity':
             self.showInfo(parametry, 'relhum')
        elif prikaz == 'pressure':
            pass
        elif prikaz == 'maxtemp':
            pass
        elif prikaz == 'maxhumidity':
            pass
        elif prikaz == 'maxpressure':
            pass
        elif prikaz == 'warmestcity':
            pass
        elif prikaz == 'coldestcity':
            pass
        elif prikaz == 'graphtemp':
            pass
        elif prikaz == 'graphpressure':
            pass
        else:
            print('Invalid input')
    
    def showInfo(self, parametry, info):

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
                    print(f'city:{city} date:{date} {info}:{value}')
                except:
                    print('Invalid input')

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

