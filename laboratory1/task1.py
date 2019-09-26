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
------------------------------------
Користувач уводить три числа. 
Збільшити перше число в два рази,
друге числа зменшити на 3, 
третє число звести в квадрат і
потім знайти суму нових трьох чисел.
------------------------------------""")
x = cycled_input("x:",float,None)
y = cycled_input("y:",float,None)
z = cycled_input("z:",float,None)
x = x * 2
y = y - 3
z = pow(z, 2)
print('Number one*2:',x)
print('Number two-3:',y)
print('Number three^2:',z)
print('Number one*2+Number two-3+Number three^2:',z+y+x)