year = int(input("What year do you wanna check? "))

if year%4 == 0 and (year%100 == 0 or year%400 == 0):
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")

