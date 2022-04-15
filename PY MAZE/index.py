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
        
        return False


file1 = open('INPUT', 'r')
lines = file1.readlines()

move = int(lines[0]) # Pocet kroku nutno udelat

person = None

Maze = []
for i in range(1, len(lines)):
    Maze.append(lines[i].split())
    if person is None:
        line = lines[i].split()
        mazeWidth = len(line)
        for j in range(mazeWidth):
            if line[j] == '>':
                person = Person('>', [j, i-1], move) # i-1, protze to bylo posunuty kvuli 1.radku
            if line[j] == 'v':
                person = Person('v', [j, i-1], move)
            if line[j] == '<':
                person = Person('<', [j, i-1], move)
            if line[j] == '^':
                person = Person('^', [j, i-1], move)


def printMaze():
    Maze[person.poziceOrigin[1]][person.poziceOrigin[0]] = '.'
    Maze[person.pozice[1]][person.pozice[0]] = person.smer
    for i in range (len(Maze)):
        print(' '.join(Maze[i]))


for i in range (person.pocetKroku):
    person.UdelejKrokDoPredu()

printMaze()





