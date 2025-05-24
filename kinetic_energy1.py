print("Kinetic Energy Program")
print("")
def kinetic_energy(mass, vel):
 return mass * 0.5 * (vel ** 2)

entrynum = 1

while True:

    mass_num = float(input("Please enter mass in kg: "))
    velnum = float(input("Please enter velocity of object in m/s: "))
    KE = kinetic_energy(mass_num, velnum)
    print(f"Num of entries: {entrynum}")
    print(f"Kinetic Energy (KE): {KE} Joules")
    entrynum += 1
    
    another = input("Would you like to convert another value? y/n:").lower()
    if another != "y":
        print("Please restart program to continue. Enter y at the beginning prompt.")
        break
   
    

