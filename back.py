def inputf(inp):
    fl = True
    while fl:
        x = input()
        try:
            x = x.split(',')
        except:
            x = [x[1:]]
        try:
            out = float(float(str(x[0]) + "." + str(x[1])) if len(x) > 1 else float(x[0]))
            fl = False
        except:
            print("вы ввели не число")
            print(inp, end=' ')
    return out


def lab_work_5():
    print('Введите данные таймера:')
    t = []
    for i in range(4):
        print(f't{i + 1}: ')
        t.append(inputf("t" + str(i+1) + " = "))

    l = 10 / 1000
    M = 510 / 1000
    d_l = 0.5 / 1000
    d_M = 0.005
    d_t = 0.00001

    v = []
    for Ti in t:
        v.append(l / Ti)
    print('v (скорость): ', "{:.8f}".format(v[0]), "{:.8f}".format(v[1]), "{:.8f}".format(v[2]), "{:.8f}".format(v[3]))

    p = []
    for vel in v:
        p.append(M * vel)
    print('p (импульс): ', "{:.8f}".format(p[0]), "{:.8f}".format(p[1]), "{:.8f}".format(p[2]), "{:.8f}".format(p[3]))

    w_t = []
    for Ti in t:
        w_t.append(d_t / Ti)
    print('δt (относительная погрешность времени): ', "{:.8f}".format(w_t[0]), "{:.8f}".format(w_t[1]),
          "{:.8f}".format(w_t[2]), "{:.8f}".format(w_t[3]))
    a = d_l / l + d_M / M
    w_p1 = a + w_t[0]
    w_p2 = a + w_t[1]
    w_p3 = a + w_t[2]
    w_p4 = a + w_t[3]
    print('δp (относительная погрешность импульса): ', "{:.8f}".format(w_p1), "{:.8f}".format(w_p2),
          "{:.8f}".format(w_p3), "{:.8f}".format(w_p4))
    d_p1 = w_p1 * p[0]
    d_p2 = w_p2 * p[1]
    d_p3 = w_p3 * p[2]
    d_p4 = w_p4 * p[3]
    print('Δp (абсолютная погрешность импульса): ', "{:.8f}".format(d_p1), "{:.8f}".format(d_p2),
          "{:.8f}".format(d_p3), "{:.8f}".format(d_p4))
    print(f'(p1 = {"{:.8f}".format(p[0])} +- {"{:.8f}".format(d_p1)})')
    print(f'(p2 = {"{:.8f}".format(p[1])} +- {"{:.8f}".format(d_p2)})')
    print(f'(p3 = {"{:.8f}".format(p[2])} +- {"{:.8f}".format(d_p3)})')
    print(f'(p4 = {"{:.8f}".format(p[3])} +- {"{:.8f}".format(d_p4)})')
    input('Enter для продолжения (если ничего не происходит, ещё раз Enter)')


def lab_work_6():
    print('Вводить: \nF \nd_s (абсолютная погрешность отклонения среднего арифметического s) \nH \nh')
    F = inputf(input())
    d_s = inputf(input())
    H = inputf(input())
    h = inputf(input())

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
    input('Enter для продолжения (если ничего не происходит, ещё раз Enter)')
