while True:
    try:  # any code which is likely to give error is inserted in try
        number1 = float(input("Enter Dividend (number1) for division : "))
        number2 = float(input("Enter Divisor (number2) for division : "))
        result = number1 / number2
    except ValueError:  # it will run when ValueError occurs in try block
        print("Looks like you didn't enter number. Try again.")
        continue
    except ZeroDivisionError:  # it will run ZeroDivisionError occurs in try block
        print("Looks like your divisor is 0. Try again.")
        continue
    except:  # it will run when error occur but doesn't belong to above expected errors
        print("Something is wrong. Try again.")
        continue
    else:  # It will only run when either of the expect don't run
        print("Division is = " + str(result))
        break
    finally:  # Whatever may be the case this will run for sure
        print("Great Learning !!")
