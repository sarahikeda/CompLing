def c_to_f(temp):
    return(temp * 9/5 + 32)

def to_f_wordy(temp):
    if temp > 30:
        print("Watch out! It's getting really hot in here!")
    print("Celsius temp is: ", temp)
    print("Fahrenheit temp is: ", c_to_f(temp))
    print("^^^^ ^^^^")

temps = [50,80, 30, 22]
temps.sort()

for temp in temps:
    to_f_wordy(temp)
