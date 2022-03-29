import sys

class Solution:
    def __init__(self, content, width):
        self.pole = content.split()
        self.count = width
        self.row = []
        self.temp = []
        self.const_count = width
    

    def add_space(self, line):
        miss_space = self.const_count - len(line)
        temp_pole = line.split()
        i = 0
        while miss_space > 0:
            try:
                temp_pole[i] = temp_pole[i] + " "
            except:
                try:
                    return temp_pole[0]
                except:
                    return "NO"
            i += 1
            if i == len(line.split())-1:
                i = 0
            miss_space -= 1
        return " ".join(temp_pole).rstrip()

    def justify(self):
        for i in range(len(self.pole)):
            if len(self.pole[i])+1 <=  self.count+1:
                self.row.append(self.pole[i]+" ")
                self.count -= (len(self.pole[i])+1)
            else:
                self.row.append("\n")
                self.row.append(self.pole[i]+" ")
                self.count = self.const_count - (len(self.pole[i])+1)

        for line in "".join(self.row).splitlines():
            if (self.add_space(line.rstrip()) == "NO"):
                pass
            else:
                self.temp.append(self.add_space(line.rstrip()))

        fw = open("odst.out", "a")
        for i in range(len(self.temp) - 1):
            fw.write(self.temp[i] + "\n")
        try:
            fw.write(" ".join(self.temp[-1].split()))
            fw.write("\n")
            # fw.write("\n")
        except:
            fw.write("")

    def justifyLast(self):
        for i in range(len(self.pole)):
            if len(self.pole[i])+1 <=  self.count+1:
                self.row.append(self.pole[i]+" ")
                self.count -= (len(self.pole[i])+1)
            else:
                self.row.append("\n")
                self.row.append(self.pole[i]+" ")
                self.count = self.const_count - (len(self.pole[i])+1)

        for line in "".join(self.row).splitlines():
            if (self.add_space(line.rstrip()) == "NO"):
                pass
            else:
                self.temp.append(self.add_space(line.rstrip()))

        fw = open("odst.out", "a")
        for i in range(len(self.temp) - 1):
            fw.write(self.temp[i] + "\n")
        try:
            fw.write(" ".join(self.temp[-1].split()))
            fw.write("\n")
        except:
            fw.write("")


f = open("INPUT", "r")
open('odst.out', 'w').close()

widthLength = int(sys.argv[1])

content = ''
isSpace = False

countParagraph = 0
newParagraf = False
countNewLineChar = 0

while True:
        c = f.read(1)
        if not c:
            break

        if(c == '\n'):
            countNewLineChar += 1
            if(countNewLineChar == 2):
                newParagraf = True
            else:
                newParagraf = False

        if(newParagraf):
            if(len(content) != 0):
                s1 = Solution(content.rstrip(), widthLength)
                s1.justify()
            content = ''
            countParagraph = 1
            countNewLineChar = 0
            newParagraf = False
        else:
            if(c.isspace() and isSpace):
                pass
            elif(c == '\n'):
                if(countNewLineChar == 1):
                    content += ' '
                pass
            else:
                content += c
                countNewLineChar = 0
                if(countParagraph == 1):
                     countParagraph = 0
                     fw = open("odst.out", "a")
                     fw.write("\n")
                    #  fw.write("\n")
                     fw.close()                 

            if(c.isspace()):
                isSpace = True
            else:
                isSpace = False
            

s1 = Solution(content.rstrip(), widthLength)
s1.justifyLast()