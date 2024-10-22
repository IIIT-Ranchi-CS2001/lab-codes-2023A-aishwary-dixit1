
# Enter the coordinates of two points on the cartesian plane (take user input using comprehension). Find the equation of the straight 
# line passing through these points.
# Hint: Eqn is (x-x1) = ((x1-x2)/(y1-y2)) (y-y1)

x1, y1 = [float(i) for i in input("Enter coordinates of the first point (x1, y1): ").split()]
x2, y2 = [float(i) for i in input("Enter coordinates of the second point (x2, y2): ").split()]

if y1 != y2:
    slope = (x1 - x2) / (y1 - y2)
else:
    slope = None
if slope is not None:
    print(f"The equation of the line is: (x - {x1}) = {slope} * (y - {y1})")
else:
    print(f"The line is vertical, and the equation is x = {x1}")
