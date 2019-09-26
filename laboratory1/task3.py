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
----------------------------
Прогарма виконує функцію
вказану нижче
----------------------------
F(x)={0,       якщо x<=1
     {1/(x+6), якщо x>1 
----------------------------
Ведіть дійсне число
----------------------------""")
var1 = cycled_input("x:",float,lambda v: v!=6)
if var1 > 1:
    z = 1 / (var1 + 6)
    print(z)
else:
    z1 = 0
    print(z1)