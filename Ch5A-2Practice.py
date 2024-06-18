##Robert Fernandez
##Complte
##Program to convert kilometers to miles.

MILES_PER_KM = 0.6214
def convert_and_print_miles(km):
    miles = km * MILES_PER_KM
  
    print(f"There are {miles:,.2f} miles in {km:,.2f} kilometers.")

def main():
    km = float(input("Enter the number of kilometers: "))
    convert_and_print_miles(km)

if __name__ == "__main__":
    main()
