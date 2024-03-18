import QuadraticBezierDAC
import QuadraticBezierBF
import GeneralBezierDAC
import GeneralBezierBF

print("==========Kurva Bezier===========")
print("1. Divide And Conquer (Default)")
print("2. Brute Froce")
print("============================")
tipe_algoritma = int(input("Pilih Algoritma: "))
if tipe_algoritma == 2:
    print("========Brute Force===========")
    print("1. General (Default)")
    print("2. Quadratic")
    print("============================")
    pilihan = int(input("Pilih tipe: "))
    print("")
    if pilihan == 2:
        QuadraticBezierBF.main()
    else:
        GeneralBezierBF.main()
else:
    print("========Divide and Conquer===========")
    print("1. General (Default)")
    print("2. Quadratic")
    print("============================")
    pilihan = int(input("Pilih tipe: "))
    print("")
    if pilihan == 2:
        QuadraticBezierDAC.main()
    else:
        GeneralBezierDAC.main()