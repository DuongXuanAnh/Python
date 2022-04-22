import sys

class Person:
    def __init__(self, smer, pozice, pocetKroku):
        self.smer = smer
        self.pozice = pozice
        self.pocetKroku = pocetKroku
        self.poziceOrigin = pozice

    def UdelejKrokDoPredu(self):
        if self.smer == '>':
            if self.OtocilSe():
                pass
            else:
                self.pozice = [self.pozice[0], self.pozice[1] + 1]
                self.pocetKroku -= 1
        elif self.smer == 'v':
            if self.OtocilSe():
                pass
            else:
                self.pozice = [self.pozice[0] + 1, self.pozice[1]]
                self.pocetKroku -= 1
        elif self.smer == '<':
            if self.OtocilSe():
                pass
            else:
                self.pozice = [self.pozice[0], self.pozice[1] - 1]
                self.pocetKroku -= 1
        elif self.smer == '^':
            if self.OtocilSe():
                pass
            else:
                self.pozice = [self.pozice[0] - 1, self.pozice[1]]
                self.pocetKroku -= 1

    def JeVePreduPrekazka(self):
        if self.smer == '>' and Maze[self.pozice[0]][self.pozice[1] + 1] == '#':
            return True
        if self.smer == 'v' and Maze[self.pozice[0] + 1][self.pozice[1]] == '#':
            return True
        if self.smer == '<' and Maze[self.pozice[0]][self.pozice[1] - 1] == '#':
            return True
        if self.smer == '^' and Maze[self.pozice[0] - 1][self.pozice[1]] == '#':
            return True
        
        return False
    
    def JeVpravoPrekazka(self):
        if self.smer == '>' and Maze[self.pozice[0] + 1][self.pozice[1]] == '#':
            return True
        if self.smer == 'v' and Maze[self.pozice[0]][self.pozice[1] - 1] == '#':
            return True
        if self.smer == '<' and Maze[self.pozice[0] - 1][self.pozice[1]] == '#':
            return True
        if self.smer == '^' and Maze[self.pozice[0]][self.pozice[1] + 1] == '#':
            return True

        return False
    
    def JeVlevoPrekazka(self):
        if self.smer == '>' and Maze[self.pozice[0] - 1][self.pozice[1]] == '#':
            return True
        if self.smer == 'v' and Maze[self.pozice[0]][self.pozice[1] + 1] == '#':
            return True
        if self.smer == '<' and Maze[self.pozice[0] + 1][self.pozice[1]] == '#':
            return True
        if self.smer == '^' and Maze[self.pozice[0]][self.pozice[1] - 1] == '#':
            return True
        
        return False

    def OtocilSe(self):
        smer = ['>', 'v' ,'<', '^']
        if self.JeVePreduPrekazka():
            if self.JeVpravoPrekazka():
                for i in range(len(smer)):
                    if(person.smer == smer[i]):
                        person.smer = smer[(i-1)%4]
                        return True
                
            elif self.JeVlevoPrekazka():
                for i in range(len(smer)):
                    if(person.smer == smer[i]):
                        person.smer = smer[(i+1)%4]
                        return True  
        return False
    
    def SmerBezPravyZdi(self):
        smer = ['>', 'v' ,'<', '^']
        if(person.JeVpravoPrekazka() is False):
            for i in range(len(smer)):
                if(person.smer == smer[i]):
                    person.smer = smer[(i+1)%4]
                    break


person = None

Maze = []
for line in sys.stdin:
    Maze.append(line.split())

move = int(Maze.pop(0)[0])

for i in range(len(Maze)):
    if(person is None):
        for j in range(len(Maze[i])):
            if Maze[i][j] == '>':
                person = Person('>', [i, j], move)
                break
            elif Maze[i][j] == 'v':
                person = Person('v', [i, j], move)
                break
            elif Maze[i][j] == '<':
                person = Person('<', [i, j], move)
                break
            elif Maze[i][j] == '^':
                person = Person('^', [i, j], move)
                break

def printMaze():
    Maze[person.poziceOrigin[0]][person.poziceOrigin[1]] = '.'
    Maze[person.pozice[0]][person.pozice[1]] = person.smer
    for i in range (len(Maze)):
        print(' '.join(Maze[i]))



while(person.pocetKroku > 0):
    person.SmerBezPravyZdi()
    person.UdelejKrokDoPredu()


printMaze()