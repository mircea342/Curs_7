print("First hello world!")


try:
    l = ["abc", 5, 100]
    print(l[5])
except Exception as ex:
    print("---A avut loc o exceptie!")
    print(f"---Detaliile exceptiei: {ex}")

print("Second hello world!")

