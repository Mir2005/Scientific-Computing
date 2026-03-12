def calculate_poissons_ratio(lateral_strain, axial_strain):
    if axial_strain == 0:
        return "ERROR! Axial Strain can not be ZERO"
    else:
        nue = lateral_strain/axial_strain
        return nue
    
print("___Poisson’s Ratio Calculation___")
lateral_strain = float(input("Enter the Lateral Strain: "))
axial_strain = float(input("Enter the Axial Strain: "))

poissons_ratio = calculate_poissons_ratio(lateral_strain, axial_strain)

if isinstance(poissons_ratio, str):
    print(poissons_ratio)
else:
    pr = abs(poissons_ratio)
    print(f"The Poisson's ratio of this material is {pr:.3f}.")
