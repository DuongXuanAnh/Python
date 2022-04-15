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
                self.pozice = [self.pozice[0] + 1, self.pozice[1]]
                self.pocetKroku -= 1
        if self.smer == 'v':
            if self.OtocilSe():
                pass
            else:
                self.pozice = [self.pozice[0], self.pozice[1] + 1]
                self.pocetKroku -= 1
        if self.smer == '<':
            if self.OtocilSe():
                pass
            else:
                self.pozice = [self.pozice[0] - 1, self.pozice[1]]
                self.pocetKroku -= 1
        if self.smer == '^':
            if self.OtocilSe():
                pass
            else:
                self.pozice = [self.pozice[0], self.pozice[1] - 1]
                self.pocetKroku -= 1

    def JeVePreduPrekazka(self):
        if self.smer == '>' and Maze[self.pozice[0] + 1][self.pozice[1]] == '#':
            return True
        if self.smer == 'v' and Maze[self.pozice[0]][self.pozice[1] + 1] == '#':
            return True
        if self.smer == '<' and Maze[self.pozice[0] - 1][self.pozice[1]] == '#':
            return True
        if self.smer == '^' and Maze[self.pozice[0]][self.pozice[1] - 1] == '#':
            return True
        
        return False
    
    def JeVpravoPrekazka(self):
        if self.smer == '>' and Maze[self.pozice[0]][self.pozice[1] + 1] == '#':
            return True
        if self.smer == 'v' and Maze[self.pozice[0] - 1][self.pozice[1]] == '#':
            return True
        if self.smer == '<' and Maze[self.pozice[0]][self.pozice[1] - 1] == '#':
            return True
        if self.smer == '^' and Maze[self.pozice[0] + 1][self.pozice[1]] == '#':
            return True

        return False
    
    def JeVlevoPrekazka(self):
        if self.smer == '>' and Maze[self.pozice[0]][self.pozice[1] - 1] == '#':
            return True
        if self.smer == 'v' and Maze[self.pozice[0] + 1][self.pozice[1]] == '#':
            return True
        if self.smer == '<' and Maze[self.pozice[0]][self.pozice[1] + 1] == '#':
            return True
        if self.smer == '^' and Maze[self.pozice[0] - 1][self.pozice[1]] == '#':
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
                
            if self.JeVlevoPrekazka():
                for i in range(len(smer)):
                    if(person.smer == smer[i]):
                        person.smer = smer[(i+1)%4]
                        return True

            for i in range(len(smer)):
                if(person.smer == smer[i]):
                    person.smer = smer[(i+1)%4]
                    return True    
        
        return False

person = None

Maze = []
for line in sys.stdin:
    Maze.append(line.split())

move = int(Maze.pop(0)[0])

for i in range(len(Maze)):
    if(person is None):
        for j in range(len(Maze[i])):
            if Maze[i][j] == '>':
                person = Person('>', [j, i], move)
            if Maze[i][j] == 'v':
                person = Person('v', [j, i], move)
            if Maze[i][j] == '<':
                person = Person('<', [j, i], move)
            if Maze[i][j] == '^':
                person = Person('^', [j, i], move)

def printMaze():
    Maze[person.poziceOrigin[1]][person.poziceOrigin[0]] = '.'
    Maze[person.pozice[1]][person.pozice[0]] = person.smer
    for i in range (len(Maze)):
        print(' '.join(Maze[i]))


while(person.pocetKroku > 0):
    person.UdelejKrokDoPredu()

print(Maze)
printMaze()





