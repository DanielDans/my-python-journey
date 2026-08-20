print('addition: ', 5 + 3)
print('subtraction: ', 2 - 1)
print('multiplication: ', 2 * 3)
print ('division: ', 4 / 2) # division in python gives float
print('division: ', 6 / 2)
print('division without remainder: ', 7 // 2)
print('modulus: ', 3 % 2) # gives remainder
print('exponent: ', 2 ** 3)
# complexes: 1 + 1j
# multiplying complexes: (1 + 1j) * (1 - 1j)

age = int(14)
height = float(1.80)
complex = '1x + 2x'
basetri = int(input('enter base of triangle: '))
heighttri = int(input('enter height of triangle: '))
area_of_tri = 0.5 * basetri * heighttri
print('the area of triangle is:', area_of_tri, 'm^2')
# triangle perimeter
side_a = int(input('enter side a: '))
side_b = int(input('enter side b: '))
side_c = int(input('enter side c: '))
perimeter_tri = side_a + side_b + side_c
print('the perimeter of the triangle:', perimeter_tri)
# rectangle area and perimeter
length_rec = int(input('enter rectangle length: '))
width_rec = int(input('enter rectangle width: '))
area_rec = length_rec * width_rec
perimeter_rec = 2 * (length_rec + width_rec)
print('area of rec is:', area_rec)
print('perimeter of rec is:', perimeter_rec)
# circle area and circumference
radius = float(input('enter radius: '))
area_circ = 3.14 * radius * radius
circum_circ = 3.14 * radius * 2
print('area of circl is:', area_circ)
print('circum of circl is:', circum_circ)
# graph thing
# y = 2x -2
slope1 = (2 - 1) / (2 - 0.75)
print(slope1)
# p1 2,2 p2 6,10
point1 = (2, 2)
point2 = (6, 10)
slope2 = (point2[1] - point1[1]) / (point2[0] - point1[0])
print(slope2)
distance = 0.5 * (point2[0] - point1[0])**2 + (point2[1] - point1[1])
print(distance)
print(slope1 < slope2)
print('on' in ('python' and 'dragon'))