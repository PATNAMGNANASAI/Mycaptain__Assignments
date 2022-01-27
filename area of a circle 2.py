import math
radius = float(input("enter a radius value:"))
area = math.pi*radius*radius
print(area)

filename=input("input the file")
extens=filename.split(".")
print("extension of a file is:","",(extens[-1]),"")
