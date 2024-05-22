# Реализовать библиотеку с любым функционалом. К примеру создайте функции для арифметических операций и выстроите фасад
# из импортов. Хочу иметь возможность импортировать кое какие функции из пакета но не все.
from geometry import circle, circumference
from geometry.triangle import area as triangle_area
from geometry.square import perimeter

r = 6.8
print(f"The area of the circle with the radius {r} equals {circle.area(r)}")

print(f"The circumference of the circle with the radius {r} equals {circumference(r)}")

a, b, c = [4.5, 4.5, 5]
print(f"The area of the triangle where a = {a}, b = {b} and c = {c} equals {triangle_area(a, b, c)}")

s = 7.5
print(f"The perimeter of the square where the side is {s} equals {perimeter(s)}")
