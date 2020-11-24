__operators = ('+', '-', '/', '//', '*', '**', '%')

def calculator():
    x = eval(input())
    operator = input()
    y = eval(input())
    if operator not in __operators:
        print("Nevalidna operacija")
        return

    rezultat = 0
    if operator == '+':
        rezultat = x+y
    elif operator == '-':
        rezultat = x-y
    elif operator == '/':
        rezultat = x/y
    elif operator == '//':
        rezultat = x//y
    elif operator == '*':
        rezultat = x*y
    elif operator == '**':
        rezultat = x**y
    elif operator == '%':
        rezultat = x%y
    print(rezultat)


if __name__ == "__main__":
    calculator()