hours = input("How many hours did you work?")
rate = input("What is your hourly rate?")
bonus = input("What is your hourly bonus?")

try:
    hours = float(hours)
    rate = float(rate)
    bonus = float(bonus)
    bonusPay = 0
except Exception as e:
    print("Invalid input. Rerun the program and input only integers")
    quit()

def computepay(hrs, rt, bon):
    bonusPay = 0
    regularHours = hrs
    if hrs > 40:
        regularHours = 40
        bonusHours = hrs - 40
        bonusPay = bonusHours*rt*bon
    regularPay = regularHours*rate
    return(regularPay + bonusPay)

print("Pay", computepay(hours, rate, bonus))
