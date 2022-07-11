# Dia 15

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError: # it will prevent block the code execution after we got an error (if is a different exception, it will block code tough :/)
        print('Cant divide by zero')
        return 'wrong operation'

print(divide(1,0))

print('🚀🚀🚀 keep executing stuff under 🚀🚀🚀')