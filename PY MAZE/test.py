import sys

maze = []
for line in sys.stdin:
    maze.append(line.split())
    
print(maze.pop(0)[0])
print(maze)