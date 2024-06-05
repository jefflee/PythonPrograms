from collections import namedtuple

circle = namedtuple('Point', ['x', 'y', 'r'])
c = circle(10, 20, 50)

print(c)                 # Point(x=10, y=20, r=50)
print(c.x, c.y, c.r)     # 10 20 50
print(c[0], c[1], c[2])  # 10 20 50
