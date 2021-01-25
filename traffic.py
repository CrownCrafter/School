#!/usr/bin/env python3

def trafficLight():
    light = input("Enter color")
    if(light == "RED" or light == "YELLOW" or light == "GREEN"):
        return light
    else:
        print("Wrong color")
def light(light):

    if(light == "RED"):
        return 0
    elif(light == "YELLOW"):
        return 1
    elif(light == "GREEN"):
        return 2
l = light(trafficLight())
if(l == 0):
    print("STOP")
elif(l == 1):
    print("WAIT")
else:
    print("GO!")
