def cyl(h, r):
    area_cyl = 2 * 3.14 * r * h
    return(area_cyl)

def con(r, l):
    area_con = 3.14 * r * l
    return(area_con)
def final_price(cost):
    tax = 0.18 * cost
    re_price = cost + tax
    return(re_price)
print("Enter Values of cylindrical part of tent ")
h = float(input("Height : "))
r = float(input("radius : "))
csa_cyl = cyl(h, r)
l = float(input("Enter slant height "))
csa_con = con(r, l)
canvas_area  = csa_cyl + csa_con
print("Area of canvas = ", canvas_area, " m^2")
unit_price = float(input("Enter cost of 1 m^2 "))
total_price = unit_price * canvas_area
print("Total cost of canvas before tax ",total_price)
print("Inluding tax"+ str(final_price(total_price)))
