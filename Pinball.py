#Mostafa Bhuiyan
#MATH 2605 Pinball Project

from __future__ import division
from visual import *
import random
import math


r = float(input("Enter a radius for the three circles. "))
s = float(input("Enter a side length for the triangles. "))
if r >= s/2:
    s = int(input("Invalid: r >= s/2. Enter another value for s. "))

print("How should the program choose angles?")
choice = int(input("""   1. Use random angles. \n   2. Use equally spaced angles \n   3. Take a guess! \n"""))

angleList_random = []

num = 0
hits = label(pos=(r*2, r*2), text="Hits: ")
disk2 = cylinder(pos=(s/2, -s*sqrt(3)/6), axis=(0, 0, .05), radius=r, opacity=.5, color=color.white)
disk3 = cylinder(pos=(-s/2,-s*sqrt(3)/6), axis=(0, 0, .05), radius=r, opacity=.5, color=color.white)
disk1 = cylinder(pos=(0,s*sqrt(3)/3), axis=(0, 0, .05), radius=r, opacity=.5, color=color.white)
ball = sphere(pos=(0, 0), radius = r/10, color=color.yellow)
tri = curve(pos=[disk2.pos, disk3.pos, disk1.pos, disk2.pos])
angleCount = label(pos=(-r*2, r*2), text="Angle: ")

if choice == 1:
    n = input("How many angles do you want to test? ")
    
    for angles in range(n):
        angle = random.uniform(0, 2*math.pi)
        angleList_random.append(angle)
elif choice == 2:
    n = input("How many angles do you want to test? ")
    
    for numbers in range(n):
        angle = random.uniform(0, 2*math.pi)
        newAngle = (numbers*2*math.pi)/(n-1)
        angleList_random.append(newAngle)
elif choice == 3:
    angle = float(input("Enter an angle in radians. Type in 'math.pi' for pi. For example, 2/pi is written as 2/math.pi. "))
    
    angleList_random.append(angle)
    angleList_random.append(angle)
    
index = 0
    

    
def reflect():
    pinballText = open("angles_test.txt", "w")
    ballpos = open("ball_pos.txt", "w")
    angleNum = 1
    global index
    num = 0
    
    
    while index < len(angleList_random)-1:
        disk1.color = color.white
        disk2.color = color.white
        disk3.color = color.white
        velocity = vector(math.cos(angleList_random[index]), math.sin(angleList_random[index]))
        velocity = norm(velocity)
        angleSum = 2*math.pi
        ball.pos = vector(0, 0, 0)
        while not angleSum < 2*math.pi - 1e-2 or angleSum > 2*math.pi + 1e-2:
            deltat = .5
            rate(100)
            
            velocity = norm(velocity)
            ball.pos = ball.pos + velocity*deltat
            #print("Flag: ", ball.pos)
            

            vector1 = disk1.pos - ball.pos
            vector2 = disk2.pos - ball.pos
            vector3 = disk3.pos - ball.pos
            
            
            
            theta1_2 = vector1.diff_angle(vector2)
            theta2_3 = vector2.diff_angle(vector3)
            theta3_1 = vector3.diff_angle(vector1)

            angleSum = theta1_2 + theta2_3 + theta3_1
            #print(angleSum)
            
            
            if mag(vector1) <= r:
                a = -velocity
                projection = proj(a, vector1)
                perpendicular = a - projection
                perpendicular = -perpendicular
                final = perpendicular + projection
                velocity = final
                num += 1
                hits.text = "Hits: " + str(num)
                disk1.color = color.green
                pinballText.write(str(angleList_random[index]) + ", :Hit Disk 1!" + "\n")
                ballpos.write(str(num) + ".Angle: " + str(angleList_random[index]) + " :Hit Disk 1 at: " + str(ball.pos) + "\n")
            elif mag(vector2) <= r:
                a = -velocity
                projection = proj(a, vector2)
                perpendicular = a - projection
                perpendicular = -perpendicular
                final = perpendicular + projection
                velocity = final
                num += 1
                hits.text = "Hits: " + str(num)
                disk2.color = color.green
                pinballText.write(str(angleList_random[index]) + " , :Hit Disk 2!" + "\n")
                ballpos.write(str(num) + ".Angle: " + str(angleList_random[index]) + " :Hit Disk 2 at: " + str(ball.pos) + "\n")
            elif mag(vector3) <= r:
                a = -velocity
                projection = proj(a, vector3)
                perpendicular = a - projection
                perpendicular = -perpendicular
                final = perpendicular + projection
                velocity = final
                num += 1
                hits.text = "Hits: " + str(num)
                disk3.color = color.green
                pinballText.write(str(angleList_random[index]) + ", :Hit Disk 3!" + "\n")
                ballpos.write(str(num) + ".Angle: " + str(angleList_random[index]) + " :Hit Disk 3 at: " + str(ball.pos) + "\n")
        pinballText.write("Angle: " + str(angleList_random[index]) + ", Total Hits: " + str(num) + "\n")    
        index += 1
        angleNum += 1
        angleCount.text = "Angle: " + str(angleNum)
        
    pinballText.write("Angles Tested: " + str(angleNum) + "\n" + "Hits: " + str(num))
    pinballText.close()
    ballpos.close()
    print("All Done!")
    
reflect()
        

    
    
    
    

   


