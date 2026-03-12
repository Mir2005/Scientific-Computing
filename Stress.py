def calculate_stress(F, A):
    if A == 0:
        return "ERROR! Area can not be zero."
    sigma = F/A
    return sigma


print("___Stress in a Material___")

F = float(input("Enter the force(F) in Newtons: "))
A = float(input("Enter the area(a) in Sq.meters: "))

Stress = calculate_stress(F, A)

if isinstance(Stress, str):
    print(Stress)
else:
    print(f"The Stress in the Material is {calculate_stress(F, A)} Pa.")