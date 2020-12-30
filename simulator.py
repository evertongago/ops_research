from matplotlib import pyplot

def run(weekends, hiring_days, sqd_s1, sqd_s2, sqd_s3, sqd_a1, sqd_a2, sqd_a3, fn):
    x_values = range(1, 30 + 1)

    n1 = []
    n2 = []
    n3 = []

    txu_n1 = -1
    txu_n2 = -1
    txu_n3 = -1

    for d in x_values:
        if d in weekends:
            pass

        if d in hiring_days:
            txu_n1 = fn(d, sqd_a1, sqd_s1)
            txu_n2 = fn(d, sqd_a2, sqd_s2)
            txu_n3 = fn(d, sqd_a3, sqd_s3)

            if txu_n1 > txu_n2 and txu_n1 > txu_n3:
                sqd_a1 = sqd_a1 + 1
            elif txu_n2 > txu_n1 and txu_n2 > txu_n3:
                sqd_a2 = sqd_a2 + 1
            elif txu_n3 > txu_n1 or txu_n3 > txu_n2:
                sqd_a3 = sqd_a3 + 1
            else:
                if txu_n1 == txu_n2  == txu_n3:
                    sqd_a2 = sqd_a2 + 1
                elif txu_n1 == txu_n2:
                    sqd_a2 = sqd_a2 + 1
                elif txu_n1 == txu_n3:
                    sqd_a1 = sqd_a1 + 1
                elif txu_n2 == txu_n3:
                    sqd_a2 = sqd_a2 + 1

        n1.append(txu_n1)
        n2.append(txu_n2)
        n3.append(txu_n3)

    print('Contratações:')
    print('Necessidade 1 - Esperado {} Designado {}'.format(sqd_s1, sqd_a1))
    print('Necessidade 2 - Esperado {} Designado {}'.format(sqd_s2, sqd_a2))
    print('Necessidade 3 - Esperado {} Designado {}'.format(sqd_s3, sqd_a3))

    pyplot.plot(x_values, n1, color='red', label='Necessidade 1')
    pyplot.plot(x_values, n2, color='green', label='Necessidade 2')
    pyplot.plot(x_values, n3, color='blue', label='Necessidade 3')

    pyplot.legend()
    pyplot.show()
