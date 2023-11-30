def lab_work_5():
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
print('try')
    print('Вводить: \nt1 \nt2 \nt3 \nt4')
    t1 = str(input())
    t2 = str(input())
    t3 = str(input())
    t4 = str(input())
    while not (isfloat(t1) and isfloat(t2) and isfloat(t3) and isfloat(t4)):
        print('Ой! Возможно, вы ввели значения через запятую.')
        print('Введите значения цифрами через точку.')
        t1 = str(input())
        t2 = str(input())
        t3 = str(input())
        t4 = str(input())
    t1 = float(t1)
    t2 = float(t2)
    t3 = float(t3)
    t4 = float(t4)

    l = 10 / 1000
    M = 510 / 1000
    d_l = 0.5 / 1000
    d_M = 0.005
    d_t = 0.00001
    v1 = l / t1
    v2 = l / t2
    v3 = l / t3
    v4 = l / t4
    print('v (скорость): ', "{:.8f}".format(v1), "{:.8f}".format(v2), "{:.8f}".format(v3), "{:.8f}".format(v4))
    p1 = M * v1
    p2 = M * v2
    p3 = M * v3
    p4 = M * v4
    print('p (импульс): ', "{:.8f}".format(p1), "{:.8f}".format(p2), "{:.8f}".format(p3), "{:.8f}".format(p4))
    w_t1 = d_t / t1
    w_t2 = d_t / t2
    w_t3 = d_t / t3
    w_t4 = d_t / t4
    print('w_t (относительная погрешность времени: ', "{:.8f}".format(w_t1), "{:.8f}".format(w_t2),
          "{:.8f}".format(w_t3), "{:.8f}".format(w_t4))
    a = d_l / l + d_M / M
    w_p1 = a + w_t1
    w_p2 = a + w_t2
    w_p3 = a + w_t3
    w_p4 = a + w_t4
    print('w_p (относительная погрешность импульса): ', "{:.8f}".format(w_p1), "{:.8f}".format(w_p2),
          "{:.8f}".format(w_p3), "{:.8f}".format(w_p4))
    d_p1 = w_p1 * p1
    d_p2 = w_p2 * p2
    d_p3 = w_p3 * p3
    d_p4 = w_p4 * p4
    print('d_p (абсолютная погрешность импульса): ', "{:.8f}".format(d_p1), "{:.8f}".format(d_p2),
          "{:.8f}".format(d_p3), "{:.8f}".format(d_p4))
    print(f'(p1 = {"{:.8f}".format(p1)} +- {"{:.8f}".format(d_p1)})')
    print(f'(p2 = {"{:.8f}".format(p2)} +- {"{:.8f}".format(d_p2)})')
    print(f'(p3 = {"{:.8f}".format(p3)} +- {"{:.8f}".format(d_p3)})')
    print(f'(p4 = {"{:.8f}".format(p4)} +- {"{:.8f}".format(d_p4)})')
    input('Enter для продолжения (если ничего не происходит, ещё раз Enter)')


def lab_work_6():
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    print('Вводить: \nF \nd_s (абсолютная погрешность отклонения среднего арифметического s) \nH \nh')
    F = str(input())
    d_s = str(input())
    H = str(input())
    h = str(input())
    while not (isfloat(F) and isfloat(d_s) and isfloat(H) and isfloat(h)):
        print('Ой! Возможно, вы ввели значения через запятую.')
        print('Введите значения цифрами через точку.')
        F = str(input())
        d_s = str(input())
        H = str(input())
        h = str(input())
    F = float(F)
    d_s = float(d_s)
    H = float(H)
    h = float(h)

    w_m1 = 0.000121
    w_m2 = 0.000776
    d_y = 1
    d_H = 2
    d_h = d_y + d_s
    w_H = d_H / H
    w_h = d_h / h
    w_F = w_m1 + w_m2 + w_H + w_h
    d_F = F * w_F
    print('d_h:', "{:f}".format(d_h))
    print('w_H:', "{:.8f}".format(w_H))
    print('w_h:', "{:.8f}".format(w_h))
    print('w_F:', "{:.8f}".format(w_F))
    print('d_F:', "{:.8f}".format(d_F))
    print(f'F = ({"{:.8f}".format(F)} +- {"{:.8f}".format(d_F)})')
    input('Enter для продолжения')
#
#
# F = float(input())
# d_s = float(input())
# H = float(input())
# h = float(input())
# lab_work_6(F, d_s, H, h)
