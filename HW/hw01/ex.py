from math import pi

def area(r, shape_constant):
	assert r > 0, 'r必须大于0'
	return r * r * shape_constant

def area_circle(r):
	return area(r, pi)

def area_square(r):
	return area(r, 1)

