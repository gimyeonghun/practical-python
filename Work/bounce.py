# bounce.py
#
# Exercise 1.5

bounces = 0
height = 100

while bounces < 10:
    bounces = bounces + 1
    height = height * 0.6
    print(bounces, round(height,4))
