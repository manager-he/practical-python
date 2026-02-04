# bounce.py
#
# Exercise 1.5

height = 100
hit = 0

while hit < 10:
    height *= 3/5
    hit += 1
    print(hit, round(height, 4))
