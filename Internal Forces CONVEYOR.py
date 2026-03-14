import matplotlib.pyplot as plt
import random

# Internal Forces Calculation

num_bottle = 1000            # Number of bottle caps
length  = 10000             # Length of Conveyor Belt in MM
masses  = [random.uniform(2, 10) for _ in range(num_bottle)]   # Masses in GRAMS
lengths = [random.uniform(0, length) for _ in range(num_bottle)]  # Corresponding lengths in MM

lengths.sort()

# Conversion of Units
length = length / 1000
for i in range(len(masses)):
    masses[i] = masses[i] / 1000 * 9.81
    lengths[i] = lengths[i] / 1000

def ext_forces(length, masses, lengths):
    # Calculation of External Forces

    By = 0
    for i in range(len(masses)):
        By += (masses[i] * lengths[i])
    By /= length
    print(f"By: {By}")

    Ay = 0
    for i in range(len(masses)):
        Ay += masses[i]
    #print(Ay)
    #print(By)
    Ay = Ay - By

    print(f"Ay: {Ay}")

    Ax = 0

    return (Ax, Ay, By)

def internal_forces(length, masses, lengths, Ax, Ay, By):

    xc = []
    xm = []
    Fc = []
    Vc = []
    Mc = []

    # Code for first cut

    FC1 = -Ax
    Fc.append(FC1)
    Fc.append(FC1)

    VC1 = Ay
    Vc.append(VC1)
    Vc.append(VC1)

    xc.append(0)
    for i in range(len(masses)):
        xc.append(lengths[i])
        xc.append(lengths[i])
    xc.append(length)

    # Calculating VCn

    counter = 1 # Number of masses

    for i in range(len(masses)):

        FCn = Ax * -1
        VCn = Ay * -1
        # Multiplie Cuts
        # print(VCn)
        for i in range(counter):
            VCn += masses[i]
            #print(i)

        #print(VCn)
        #print(counter)

        Fc.append(FCn)
        Fc.append(FCn)

        Vc.append(VCn)
        Vc.append(VCn)

        counter += 1

    # Calculating MCn

    # Calculating MC1

    Mc.append(0)
    Mc.append(Ay * lengths[0])

    for j in range(len(masses)-2):
        j += 1

        MCN = Ay * lengths[j]

        for i in range(j):
            i += 1

            #print(f"Ref1: {lengths[len(masses)-2]}")
            #print(f"Ref2: {lengths[i-1]}")

            distance = lengths[len(masses)-2] - lengths[i-1]
            MCN -= masses[i-1]*distance
            #print(i)

        #print("-----------------")
        Mc.append(MCN)
        #print(MCN)

    # Calculating MCN

    Mc.append(By * (length - lengths[len(masses)-1]))
    #print(f"Ref {By * (length - lengths[len(masses)-1])}")
    Mc.append(0)

    xm.append(0)
    for i in range(len(Mc)-2):
        xm.append(lengths[i])
    xm.append(length)

    #print(xc)
    #print(xm)
    #print(Fc)
    #print(Vc)
    #print(Mc)

    return xc, xm, Fc, Vc, Mc

(Ax, Ay, By) = ext_forces(length, masses, lengths)

(xc, xm, Fc, Vc, Mc) = internal_forces(length, masses, lengths, Ax, Ay, By)

# Graphs
plt.figure()
plt.plot(xc, Fc, marker='o')
plt.fill_between(xc, Fc, 0, alpha=0.3)
plt.title("Normal Force Diagram")
plt.xlabel("XC")
plt.ylabel("FC")
plt.grid()

plt.figure()
plt.plot(xc, Vc, marker='o')
plt.fill_between(xc, Vc, 0, alpha=0.3)
plt.title("Shear Force Diagram")
plt.xlabel("XC")
plt.ylabel("VC")
plt.grid()

plt.figure()
plt.plot(xm, Mc, marker='o')
plt.fill_between(xm, Mc, 0, alpha=0.3)
plt.title("Moment Diagram")
plt.xlabel("XM")
plt.ylabel("MC")
plt.grid()

plt.show()