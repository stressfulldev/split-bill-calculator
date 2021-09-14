while True :
    print("\U0001F4B0 Welcome to the Bill Split Calculator \U0001F4B0")
    totalbill = input("What was the total of the bill? Rp")
    totalperson = input("How many people to split the bill? ")
    tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

    totaltip = float(totalbill) * float(tip) / 100
    personaltip = float(totaltip) / float(totalperson)
    personalbill = float(totalbill) / float(totalperson)
    personshouldpay = personalbill + personaltip
    youshouldpay = str(round(personshouldpay, 2))

    print(f"Each person should pay: Rp {youshouldpay} \n")

    while True :
        restart = input("Do you want to split another Bill? (y/n): ")
        if restart in ("y, n"):
            break
    if restart == "y":
        continue
    else :
        print("Thanks for using the Apps, Good Day !")
        break