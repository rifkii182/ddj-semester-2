print("\n penggunaan if else dalam looping")
print("--------------------\n")
a = 0
b = float(input("masukan angka anda"))
while a < b: 
    if a == (b - 1):
        print("perulangan berhenti")
        break;
    else:
        print("perulangan ke -",a)
        a += 1