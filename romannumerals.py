import math

number = input()

if number[0] in ["I", "V", "X", "L", "C", "D", "M"]:
    dec = 0
    i = 0
    while i < len(number):
        if number[i] == "M":
            dec += 1000
            i += 1

        elif number[i] == "D":
            dec += 500
            i += 1

        elif number[i] == "C":
            if i < len(number) - 1 and (number[i + 1] == "M" or number[i + 1] == "D"):
                dec -= 100
            else:
                dec += 100
            i += 1

        elif number[i] == "L":
            dec += 50
            i += 1

        elif number[i] == "X":
            if i < len(number) - 1 and (number[i + 1] == "C" or number[i + 1] == "L"):
                dec -= 10
            else:
                dec += 10
            i += 1
        elif number[i] == "V":
            dec += 5
            i += 1

        elif number[i] == "I":
            if i < len(number) - 1 and (number[i + 1] == "X" or number[i + 1] == "V"):
                dec -= 1
            else:
                dec += 1
            i += 1
    print(dec)

else:
    decNum = number
    digit = len(decNum) - 1
    decNum = int(decNum)
    romNum = ""
    while digit >= 0:
        current = int(int(decNum)/math.pow(10,digit))

        if current == 9:
            if digit == 0:
                romNum += "IX"
                decNum -= 9
            elif digit == 1:
                romNum += "XC"
                decNum -= 90
            elif digit == 2:
                romNum += "CM"
                decNum -= 900

        elif current > 5 and current < 9:
            current -= 5
            if digit == 0:
                romNum += "V"
                decNum -= 5
            elif digit == 1:
                romNum += "L"
                decNum -= 50
            elif digit == 2:
                romNum += "D"
                decNum -= 500

            for i in range(0, int(current)):
                if digit == 0:
                    romNum += "I"
                    decNum -= 1
                elif digit == 1:
                    romNum += "X"
                    decNum -= 10
                elif digit == 2:
                    romNum += "C"
                    decNum -= 100

        elif current == 5:
            if digit == 0:
                romNum += "V"
                decNum -= 5
            elif digit == 1:
                romNum += "L"
                decNum -= 50
            elif digit == 2:
                romNum += "D"
                decNum -= 500

        elif current == 4:
            if digit == 0:
                romNum += "IV"
                decNum -= 4
            elif digit == 1:
                romNum += "XL"
                decNum -= 40
            elif digit == 2:
                romNum += "CD"
                decNum -= 400

        elif current != 0:
            for i in range(0, int(current)):
                if digit == 0:
                    romNum += "I"
                    decNum -= 1
                elif digit == 1:
                    romNum += "X"
                    decNum -= 10
                elif digit == 2:
                    romNum += "C"
                    decNum -= 100
                elif digit == 3:
                    romNum += "M"
                    decNum -= 1000

        digit -= 1


    print(romNum)