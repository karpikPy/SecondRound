temperature = float(input("Input temperature: "))
def message(temp):
        if temp < -30:
            print("Either you’re lying, or you’re probably dead, ggs.")
        elif -30 < temp < 0:
            print("Freezing cold")
        elif 0 < temp <= 10:
            print("Eh, manageable")
        elif 10 < temp <= 20:
            print("Pretty good weather, I really like it actually")
        elif 20 < temp <= 30:
            print("My AC is in that range so fine by me")
        elif 30 < temp <= 40:
            print("Oh hell nah, this is too much")
        elif 40 < temp <= 50:
            print("Electricity bills will skyrocket from the amount of AC that will be used lmao")
        elif temp > 50:
            print("You are dead ngl")
message(temperature)