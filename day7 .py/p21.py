""""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2 Then, the output of the program should be:2 """
import math
origin=[0,0]

while True:
    data=input("enter robot data: ")
    if not data:
        break
    data = data.split(" ")
    if len(data)<=2:
        movement=data[0]
        steps=int(data[1])
    
        
        if movement=="UP":
            origin[0]+=steps
        elif movement=="DOWN":
            origin[0]-=steps
        elif movement=="LEFT":
            origin[1]-=steps
        elif movement=="RIGHT":
            origin[1]+=steps
        pass
    
print(int(math.sqrt(origin[0]**2 + origin[1]**2)))