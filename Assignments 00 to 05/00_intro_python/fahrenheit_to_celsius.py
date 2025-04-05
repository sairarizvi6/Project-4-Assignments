#Write a program which prompts the user for a temperature in Fahrenheit 
#(this can be a number with decimal places!) and outputs the temperature converted to Celsius.

#The Celsius scale is widely used to measure temperature, but places still use Fahrenheit.
#Fahrenheit is another unit for temperature,but the scale is different from Celsius
# -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!
#The equation you should use for converting from Fahrenheit to Celsius is the following:

#*******degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0**********
#*******(Note. The .0 after the 5 and 9 matters in the line above!!!)******

def main():

    fahrenheit = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))


    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {fahrenheit}F = {celsius}C")



if __name__ == '__main__':
    main()
