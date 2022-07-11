# Dia 16

# Multiple except 
def divide():
    try:
        op1=(float(input('Enter the first number: ')))
        op2=(float(input('Enter the second number: ')))
    
        print('division result is: ' + str(op1/op2))
    except ValueError:
        print('input added must be a number')
    except ZeroDivisionError:
        print('cant divide by zero')
    except:                                                 # general except error: (no recommended)
         print('Unknown error')
    finally:                                                # Adding finally exception will make this part of code, run regardless if it fails or
        print('🚀🚀🚀 keep executing stuff under 🚀🚀🚀')

divide()


