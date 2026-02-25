#Lab 2

print("please enter 6 bits, one at a time, you will enter either 0 or 1")

b5= int(input("Bit 1: "))
b4= int(input("Bit 2: "))
b3= int(input("Bit 3: "))
b2= int(input("Bit 4: "))
b1= int(input("Bit 5: "))
b0= int(input("Bit 6: "))

total= (b5 * 32) + (b4 * 16) + (b3 * 8) + (b2 * 4) + (b1 * 2) + (b0 * 1)

print("Based on your bits, your decimal equivilant is:", total)


