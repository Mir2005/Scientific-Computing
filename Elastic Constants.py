def calculate_youngs_modulus_from_G(G, nu):
    if nu <= -1 or nu >= 0.5:
        return "ERROR! Poisson's ratio must be between -1 and 0.5 for realistic materials."
    
    E = 2 * G * (1 + nu)
    return E

while True:
    print("\n___Elastic Constant Calculator___")
    
    try:
        G = float(input("Enter the Shear Modulus (G) in Pascals (Pa): "))
        nu = float(input("Enter the Poisson's Ratio (ν) (dimensionless, -1 < ν < 0.5): "))

        youngs_modulus = calculate_youngs_modulus_from_G(G, nu)
        
        if isinstance(youngs_modulus, str):
            print(youngs_modulus)  # Print error message
        else:
            youngs_modulus_str = "{:.2e}".format(youngs_modulus).replace("e+", " x 10^")
            print(f"The Young's Modulus for this material is {youngs_modulus_str} Pa.")

    except ValueError:
        print("ERROR! Please enter valid numerical values.")

    # Ask user if they want to continue
    y_n = input("Do you want to calculate more? (y/n): ").strip().lower()
    if y_n == "n":
        print("Exiting the program. Goodbye!")
        break
