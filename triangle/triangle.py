def equilateral(sides):
    if is_triangle(sides):
        if triangle_inequality(sides):
            return len(set(sides)) == 1 
    return False
    
def isosceles(sides):
    if is_triangle(sides):
        if triangle_inequality(sides):
            return len(set(sides)) == 2 or len(set(sides)) == 1
    return False

def scalene(sides):
    if is_triangle(sides):
        if triangle_inequality(sides):
            return len(set(sides)) == 3
    return False

def triangle_inequality(sides):
    a, b, c = sides
    return a + b >= c and b + c >= a and c + a >= b

def is_triangle(sides):
    a, b, c = sides
    if a == b == c == 0:
        return False 
    return True