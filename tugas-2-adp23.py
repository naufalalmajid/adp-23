finish = "N"

while finish == "N":
    fsal = float(input("Salary Based: "))
    samt = float(input("Sales Value: "))

    if samt > 5000:
        comm = (samt - 5000) * 0.12
    else:
        comm = 0

    finalSalary = fsal + comm
    print("Total Salary is:", finalSalary)

    finish = str(input("Wanna recalculate(Y/N)?: ").upper)

    if finish == "Y":
        break

print("calculation was finished")
