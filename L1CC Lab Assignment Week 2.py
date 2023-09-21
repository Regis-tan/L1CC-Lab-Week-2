def main_menu():
    print("="*40)
    print("==Python calculator==")
    print("1.Number calculator")
    print("2.Acceleration calculator")
    print("3.Exit Program")
    main_menu_option = input("Input option number (1-3)):")
    if main_menu_option == "1":
        number_calculator()
    elif main_menu_option == "2":
        acceleration_calculator()
    elif main_menu_option == "3":
        print("Thanks for using this program.")
        print("="*40)
        exit()
    else:
        print("Error: invalid option.")
    main_menu()

def number_calculator():
    print("="*40)
    print("Number calculator has been picked.")
    value_input = input("Input values (x operator y):")
    value_input_split = value_input.split()
    if len(value_input_split) == 3:
        x,operator,y = value_input_split
        try:
            x = float(x)
            y = float(y)
            if operator == "+":
                print(f"Answer is {x+y}")
            elif operator == "-":
                print(f"Answer is {x-y}")
            elif operator == "*":
                print(f"Answer is {x*y}")
            elif operator == "/":
                if y == 0:
                    print("Syntax error: cannot divide by zero.")
                else:
                    print(f"Answer is {x/y}")
            else:
                print("Syntax error: operator invalid.")
        except ValueError:
            print("Syntax error: x and y must be numbers.")
    else:
        print("Syntax error: expression must be in form of 'x operator y' (with spacing).")
    repeat_calculator = input("Calculate again? (y/n):")
    if  repeat_calculator == "y":
        number_calculator()
    elif repeat_calculator == "n":
        worthless_idiot_stupid_dumb_unessecary_garbage_silly_disgrace_variable = 1
    else:
        print("Error: invalid option.")

def acceleration_calculator():
    print("="*40)
    print("Acceleration calculator has been picked.")
    value_input = input("Input values (Kg Newtons):")
    value_input_split = value_input.split()
    if len(value_input_split) == 2:
        try:
            x,y = value_input_split
            x = float(x)
            y = float(y)
            print(f"Acceleration is {y / x} m/s^2")
        except ValueError:
            print("Syntax error: value must be a number.")
    else:
        print("Syntax error: expression must be in form of 'x y' (with spacing). ")
    repeat_calculator = input("Calculate again? (y/n):")
    if repeat_calculator == "y":
        acceleration_calculator()
    elif repeat_calculator == "n":
        worthless_idiot_stupid_dumb_unessecary_garbage_silly_disgrace_variable = 1
    else:
        print("Error: invalid option.")

main_menu()
