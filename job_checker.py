print("=== Egypt Remote Job Checker ===")

name = input("Apna naam: ")
age = int(input("Age: "))
skill = input("Python aati hai? yes/no: ").lower()

print("\n--- Result ---")

if age >= 18 and skill == "yes":
    print("Mubarak ho", name)
    print("Tum Egypt remote job ke liye apply kar sakti ho!")
    for i in range(1, 4):
        print("Tip", i, ": Roz 1 ghanta code karo")
else:
    print("Abhi aur mehnat karo", name)
    print("6 months baad try karna")
