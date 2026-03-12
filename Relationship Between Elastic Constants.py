def calculate_bulk_modulus_from_E(E, nu):
    denominator = ( 1 - 2 * nu)
    if denominator == 0:
        return "ERROR!, (1 - 2ν) cannot be ZERO."
    else:
        K = E/(3 * denominator)
        return K

print("___Relationship Between Elastic Constants___")

E = float(input("Enter the value of Young's Modulus in Pa: "))
nu = float(input("Enter the value of Poisson's Ratio (dimensionless): "))

bulk_modulus = calculate_bulk_modulus_from_E(E, nu)

if isinstance(bulk_modulus, str):
    print(bulk_modulus)
else:
    bulk_modulus_str = "{:.2e}".format(bulk_modulus).replace("e+", " x 10^")
    print(f"The Bulk Modulus is '{bulk_modulus_str}' Pa.")