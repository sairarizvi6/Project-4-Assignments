#Write a program that continually reads in mass from the user and then outputs the equivalent
#energy using Einstein's mass-energy equivalence formula 
#(E stands for energy, m stands for mass, and C is the speed of light:
#E = m * c**2
#Almost 100 years ago, Albert Einstein famously discovered that mass and 
#energy are interchangeable and are related by the above equation. 
#You should ask the user for mass (m) in kilograms and use a constant value for the speed 
#of light -- C = 299792458 m/s.
#Here's a sample run of the program (user input is in bold italics):
#Enter kilos of mass: 100
#e = m * C^2...
#m = 100.0 kg
#C = 299792458 m/s
#8.987551787368176e+18 joules of energy!


# Define the speed of light in meters per second (constant)
C: int = 299792458

# Main function to calculate energy using Einstein's equation (E = mc^2)
def main():
    # Prompt the user to input mass in kilograms
    mass_in_kg: float = float(input("Enter kilos of mass: "))
    
    # Calculate energy in joules using the formula E = mc^2
    energy_in_joules = mass_in_kg * (C ** 2)
    
    # Display the formula used for calculation
    print("e = m * C^2...")

    # Show the mass input by the user
    print("m = " + str(mass_in_kg) + " kg")

    # Display the speed of light constant
    print("C = " + str(C) + " m/s")

    # Print the final calculated energy in joules
    print(str(energy_in_joules) + " joules of energy!")

# Call the main function to execute the program
main()
