# Dia 7

# Condicionales:

student_grade = input('add a student grade: ')

def evaluation(grade):
    val = 'approved'
    if grade < 5:
        val='failed'
    return val


print('your test is', evaluation(int(student_grade)))

