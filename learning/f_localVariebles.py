x = 50

def func(x):
    print('х равен', x)
    x = 2
    print('замена локального х = 50 на', x)

func(x)

print('x по прежнему равен:', x)
