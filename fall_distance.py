# Name: Jamar Hill
# Date: 10/20/2020
# Description: Assignment 4.a

def fall_distance(t):
    """Returns a calculation for fall distance in meters: distance = (1/2) * gravity * time (squared)"""
    g = 9.8
    dist = ( 1 / 2 ) * g * ( t ** 2 )
    return dist

dist = fall_distance(3.2)
print(dist)
