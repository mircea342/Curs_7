z = 0

try:
    x = int(input("x="))
    y = int(input("y="))
    z = x / y
except ZeroDivisionError as ex:
    print(f"===A avut loc o exceptie de impartire la zero! Detalii: {ex}. ===")
except ValueError as ex:
    print(f"===A avut loc o exceptie numerica! Detalii: {ex}. ===")

print(f"z = x / y = {z}")

