def calculate_bulk_modulus(stress, volumetric_strain):
    if volumetric_strain == 0:
        return "ERROR! Volumetric Strain can not be ZERO."
    else:
        bulk_modulus = stress/volumetric_strain
        return bulk_modulus
    
print("___Bulk Modulus Calculation___")
stress = float(input("Enter the Stress (σ) in Pascals (Pa): "))
volumetric_strain = float(input("Enter the Volumetric Strain (dimensionless): "))

bulkModulus = calculate_bulk_modulus(stress, volumetric_strain)
if isinstance(bulkModulus, str):
    print(bulkModulus)
else:
    bm = "{:.2e}".format(bulkModulus).replace("e+", " x 10^")
    print(f"The Bulk Modulus of this material is '{bm}'.")
