def calculate_strain(delta_L, L):
    if L == 0:
        return "ERROR! original Length can not be zero."
    epsilon = delta_L/L
    return epsilon


print("___Strain in a Material___")

delta_L = float(input("Enter the elongation(delta_L) in Meters: "))
L = float(input("Enter the original Length(L) in Meters: "))

Strain = calculate_strain(delta_L, L)

if isinstance(Strain, str):
    print(Strain)
else:
    print(f"The Stress in the Material is {calculate_strain(delta_L, L)} Pa.")