#Write a code with function to the check if the water is cold, if the water temperature is more than 30 return True else false


def can_swim(temp):
    if temp <=59:
        print("The water is swimable")
    elif temp < 60 and temp < 80:
        print("The water is too hot")
    else:
        print("The water is boiling you can die if you swim")


temperature = float(input("Please put the temperature here : "))
can_swim(temperature)
