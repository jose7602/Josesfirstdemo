##Jose Mestre
type_of_car = "Van"

company = "FiberCare"

primary_van_color = "White"

secondary_van_color = "Green"

van_text = "FIBERCARE"

person = input("Enter your name: ")

print ("Hello new employee!", person)

test_van = input("Would you like to give the FiberCare van a test drive? ")
if test_van.lower() == "yes":
  print("Great!")
else:
    print ("That's ok, maybe next time")

def main():
    while True:
        game()
        restart = input("Would you like to apply again? Please enter '1' for YES or '2' for NO: ")
        if not restart == 1:
            break
    print ("Thanks for applying!")

def speed():
	x = 45
	print("You should go at this speed or below it:",x)

x = 60
speed()
print("Don't go at this speed or above it:",x)
        
