def cycled_input(text, input_type, valid_cond):
    input_type = input_type.__name__

    while True:
        try:
            if input_type == "int":
                user_input = int(input(text))
            elif input_type == "float":
                user_input = float(input(text))
            else:
                user_input = input(text)
        except ValueError:
            print("You entered wrong value. Let's try again.")
            continue

        if valid_cond is not None and valid_cond(user_input) is not True:
            print("input value is not valid.")
        else:
            return user_input
    return

print("""
    --------------------------------
    Увести з клавіатури дійсні
    числа х і у, не рівні одне
    одному. Менше з цих двох чисел
    замінити половиною їх суми,
    а більше - їх подвоєним добутком.
    ---------------------------------""")
x = cycled_input("x:",float,None)
y = cycled_input("y:",float,None)
if x > y and x!=y:
    y1 = (x + y) / 2
    print('y менше чим x, y=(x+y)/2=',y1)
    x1 = x * y * 2
    print('x більше чим y, x=y*x*2=',x1)
elif x < y and x!= y:
    x2 = (x + y) / 2
    print('x менше чим y, x=(x+y)/2=',x2)
    y2 = x * y * 2
    print('y більше чим x, y=y*x*2=',y2)
else:
    print('repeat programme again')