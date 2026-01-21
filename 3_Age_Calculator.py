# Age Calculator - Takes birth date and calculates how old you are today

def age_calculator(y, m, d):
    import datetime

    today = datetime.date.today()
    dob = datetime.date(y, m, d)
    
    age = today.year - dob.year 

    # adjust age if birthday hasn't occurred yet this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    return age

year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

print(age_calculator(year, month, day))