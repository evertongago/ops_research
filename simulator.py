def run(w_values, c_values, s1, s2, s3, a1, a2, a3, fn_urgencia):
    x_values = range(1, 30 + 1)

    n1 = []
    n2 = []
    n3 = []

    txu_n1 = -1
    txu_n2 = -1
    txu_n3 = -1

    for d in x_values:
        if d in w_values:
            pass

        if d in c_values:
            txu_n1 = fn_urgencia(d, a1, s1)
            txu_n2 = fn_urgencia(d, a2, s2)
            txu_n3 = fn_urgencia(d, a3, s3)

            if txu_n1 > txu_n2 and txu_n1 > txu_n3:
                a1 = a1 + 1
            elif txu_n2 > txu_n1 and txu_n2 > txu_n3:
                a2 = a2 + 1
            elif txu_n3 > txu_n1 or txu_n3 > txu_n2:
                a3 = a3 + 1
            else:
                if txu_n1 == txu_n2  == txu_n3:
                    a2 = a2 + 1
                elif txu_n1 == txu_n2:
                    a2 = a2 + 1
                elif txu_n1 == txu_n3:
                    a1 = a1 + 1
                elif txu_n2 == txu_n3:
                    a2 = a2 + 1

        n1.append(txu_n1)
        n2.append(txu_n2)
        n3.append(txu_n3)

    print('Contratações:')
    print('Necessidade 1 - Esperado {} Designado {}'.format(s1, a1))
    print('Necessidade 2 - Esperado {} Designado {}'.format(s2, a2))
    print('Necessidade 3 - Esperado {} Designado {}'.format(s3, a3))

    return x_values, n1, n2, n3
