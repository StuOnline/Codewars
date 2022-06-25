G = 6.67 * (10**(-11))

def convert_to_kg(mass, unit):
    if unit == "kg":
        return mass
    if unit == "g":
        return mass/1000
    if unit == "mg":
        return mass/1000000
    if unit == "μg":
        return mass/1000000000
    if unit == "lb":
        return mass*0.453592
    return 0
    
def convert_to_m(dist, unit):
    if unit == "m":
        return dist
    if unit == "cm":
        return dist/100
    if unit == "mm":
        return dist/1000
    if unit == "μm":
        return dist/1000000
    if unit == "ft":
        return dist*0.3048
    return 0
    
def solution(arr_val, arr_unit) :
    mass1 = convert_to_kg(arr_val[0], arr_unit[0]);
    mass2 = convert_to_kg(arr_val[1], arr_unit[1]);
    
    distance = convert_to_m(arr_val[2], arr_unit[2]);
    
    gravity = G * ((mass1*mass2)/(distance**2))
    
    return gravity