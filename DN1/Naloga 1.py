print("--- IZPIS VREDNOSTI, TIPOV IN CASTING   ---\n")

n = int(input("Prosim vnesi celo stevilo: "))
print("Vnesel si: " + str(n) + " ki je tipa: " + str(type(n)))

print("Casting int to float:")
n = float(n)

print("Sedaj je : " + str(n) + " tipa: " + str(type(n)))

input("\nPress any key to close")