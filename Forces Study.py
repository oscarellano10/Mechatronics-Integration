import math

# Shear Forces Calculation

max_shear = 60 # Shear Force in N

sae1050_shear_strength = 15 # Shear Strength in MPa

sf = 5 # Safety Factor

sae1050_perm_shear = sae1050_shear_strength/sf


def axle_measure(max_shear, sae1050_perm_shear):
    r = math.sqrt((max_shear)/(3.1415*(sae1050_perm_shear*1000000)))
    r *= 1000
    print(f"Axle Radius: {r} in mm")
    d_in = (r*2)/(25.4)
    print(f"Axle Diameter: {d_in} inches")
    d_116 = (d_in)/(1/16)
    print(f"Axle Diameter: {d_116} in 1/16 in")

    return r, d_116

def strength_measure(r, d_116, max_shear, sf):

    r /= 1000 # Convert to meters
    length = 0.005

    area = 3.1415 * r * length
    force = (max_shear/2)/(area) # Divided by 2 because its a double cut. Axle is supported on both sides

    print(f"We need a material that has a shear force of: {force/1000000*sf} MPa.")
    print(f"This material will be able to withstand the force of the axle at {max_shear} N.")

    return

print("----------------------")

(r, d_116) = axle_measure(max_shear, sae1050_perm_shear)

print("----------------------")

strength_measure(r, d_116, max_shear, sf)