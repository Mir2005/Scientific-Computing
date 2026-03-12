def calculate_youngs_modulus(stress, strain):
    if strain == 0:
        return "ERROR! strain can not be ZERO."
    E = stress/strain
    return E

print("___Young’s Modulus___")
stress = float(input("Enter the Stress(σ) in Pa: "))
strain = float(input("Enter the Strain(ε): "))

youngs_modulus = calculate_youngs_modulus(stress, strain)

if isinstance(youngs_modulus, str):
    print(youngs_modulus)
else:
    E_str = "{:.2e}".format(youngs_modulus).replace("e+", " × 10^")
    print(f"The Young’s Modulus of this material is {E_str} Pa")