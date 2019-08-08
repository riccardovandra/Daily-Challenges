# Tax Brackets
taxbracket1 = 10000
taxbracket2 = 30000
taxbracket3 = 100000


def tax(income):
    if income < taxbracket1:
        print(0)
    elif income < taxbracket2:
        print((income-taxbracket1)*0.1)
    elif income < taxbracket3:
        print((taxbracket2-taxbracket1)*0.1+(income-taxbracket2)*0.25)
    elif income > taxbracket3:
        print((taxbracket2-taxbracket1)*0.1 +
              (taxbracket3-taxbracket2)*0.25+income-taxbracket3*0.40)


tax(10000)
tax(25000)
tax(35000)
tax(4000000)
