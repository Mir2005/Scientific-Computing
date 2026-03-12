def calculate_shear_modulus(shear_stress, shear_strain):
    if shear_strain == 0:
        return "ERROR! Shear Strain can not be ZERO."
    else:
        shear_modulus = shear_stress/shear_strain
        return shear_modulus
    
print("___Shear Modulus Calculation___")
shear_stress = float(input("Enter the Shear Stress: "))
shear_strain = float(input("Enter the Shear Strain in Pa: "))

shear_modulus = calculate_shear_modulus(shear_stress, shear_strain)
if isinstance(shear_modulus, str):
    print(shear_modulus)
else:
    sm = "{:.2e}".format(shear_modulus).replace("e+", " x 10^")
    print(f"The Shear Modulus of this material is '{sm}' Pa.")
