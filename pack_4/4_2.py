class derivative():
    def __init__(self, polinom):
        self.polinom = polinom
        self.deriv = ''
        self.split_polinom_local = []
        self.__split_polinom()
        self.__build_polinom()

    def __split_polinom(self):
        split_to_plus = self.polinom.split('+')
        split_to_minus = []
        for m in split_to_plus:
            split_to_minus.append(m.split('-'))
        for a in split_to_minus:
            for i in range(len(a)):
                if i > 0:
                    self.split_polinom_local.append('-' + a[i])
                else:
                    self.split_polinom_local.append('+' + a[i])

    def __build_polinom(self):
        for local in self.split_polinom_local:
            if 'x' not in local:
                q = ''
            else:
                a = local.split('x')
                if a[1] == '':
                    q = a[0]
                elif a[1] == '^2':
                    q = a[0] + 'x'
                else:
                    b = int(a[1][1:])
                    if a[0] == '+':
                        a[0] = '+1'
                    elif a[0] == '-':
                        a[0] = '-1'
                    c = float(a[0]) * b
                    if c - int(c) == 0:
                        c=int(c)
                    q = str(c) + 'x^' + str(b - 1)
                    if a[0][0] != '-':
                        q = '+' + q
            self.deriv += q
        print(self.deriv) if self.deriv[0] != '+' else print(self.deriv[1:])


print('пример: x^4+2.5x^7-20x^7+14')
derivative(str(input()))
