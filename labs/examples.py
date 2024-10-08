#triangle area function
def triangle_area(base, height):
    return base * height * 0.5

x = triangle_area(5,8)
print("The area of a triangle with base 5 and height 8 is " + str(x))

print(triangle_area(5,8))

def print_hbd(name):
    return "happy birthday " + name

print_hbd("name")