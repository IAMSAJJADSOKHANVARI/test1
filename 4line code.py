from tabulate import tabulate
vorodi = input("Enter your character: ")
shomaresh = {i: vorodi.count(i) for i in set(vorodi)}
print(tabulate(shomaresh.items(), headers=["Name", "Frequency"], tablefmt="pretty"))