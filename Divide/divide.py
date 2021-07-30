from prettytable import PrettyTable

if __name__ == '__main__':

    def restore(A, B):
        sum = bin(int(A, 2) + int(B, 2))
        EA = sum[2:]
        if len(EA) == len(A):
            E = '0'
            A = EA
        else:
            E = '1'
            A = EA[-len(A):]
        return E, A

    def compPlusOne(x):
        y = x
        lst = list(x)
        for i in range(len(x)):

            if x[i] == '0':
                lst[i] = '1'
            else:
                lst[i] = '0'
        x = ''.join(lst)
        x = int('0b' + x, 2)
        x += 1
        x = bin(x)
        x = x[2:]
        while len(x) < len(y):
            x = '0' + x
        return str(x)

    def decToBin(n):
        if(n == 0):
            return "0"

        bin = ""

        while (n > 0):
            if (n & 1 == 0):
                bin = '0' + bin
            else:
                bin = '1' + bin

            n = n >> 1

        return bin

    def remove_sign_and_convert_binary(x):
        if x < 0:
            return 1, decToBin(abs(x))
        else:
            return 0, decToBin(x)

    def validate(AQ, B):
        while len(AQ) < 2*len(B):
            AQ = '0'+AQ
        while len(AQ) > 2*len(B):
            B = '0' + B
            while len(AQ) < 2*len(B):
                AQ = '0'+AQ
        return AQ, B

    def shlEAQ(E, A, Q):
        EAQ = E+A+Q
        if E == '':
            EAQ = EAQ + '0'
        else:
            EAQ = EAQ[1:] + '0'
            # print(EAQ)

        E = EAQ[0]
        A = EAQ[1:len(A)+1]
        Q = EAQ[len(A)+1:len(A)+len(Q)+1]

        # print('E is {}'.format(E))
        # print('A is {}'.format(A))
        # print('Q is {}'.format(Q))
        return E, A, Q

    T = PrettyTable()
    AQ = int(input("Enter the value of AQ: "))
    B = int(input("Enter the value of B: "))

    As, AQ = remove_sign_and_convert_binary(AQ)
    Bs, B = remove_sign_and_convert_binary(B)
    AQ, B = validate(AQ, B)
    # print('this is AQ{}'.format(AQ))
    Qs = As ^ Bs

    SC = len(B)
    Bcomp = compPlusOne(B)
    print("As = {}".format(As))
    print("AQ = {} [double the length of B]".format(AQ))
    print("Bs = {}".format(Bs))
    print("B = {}".format(B))
    print("B'+1 = {}".format(Bcomp))
    print("Sign of Quotient = As ⊕ Bs = {} ⊕ {} = {}".format(As, Bs, Qs))
    print("Sign of Remainder = As = {} ".format(As))
    print("SC = {} [length of Q]".format(SC))
    A = AQ[:len(B)]
    Q = AQ[-len(B):]
    print("Checking for overflow,")
    print("EA <- A + B'+1 ")
    print(A)
    print(Bcomp)
    print(len(A)*'-')
    sum = bin(int(A, 2) + int(Bcomp, 2))
    tempEA = sum[2:]
    print(tempEA)
    while len(tempEA) < len(A):
        tempEA = '0'+tempEA
    if len(tempEA) == len(A):
        print("E = 0. So, No overflow")
        E = ''
        T.field_names = [" B = {}, B'+1 = {}".format(B, compPlusOne(B)), 'E', 'A', 'Q', 'SC']
        T.add_row(['Initial condition', E, A, Q, SC])
        while(SC != 0):
            E, A, Q = shlEAQ(E, A, Q)
            T.add_row(['shl EAQ', E, A, Q, ''])
            if E == '0':
                sum = bin(int(A, 2) + int(Bcomp, 2))
                EA = sum[2:]
                # print("This is EA {}".format(EA))
                while len(EA) < len(A):
                    EA = '0'+EA
                if len(EA) == len(A):
                    E = '0'
                    A = EA
                else:
                    E = '1'
                    A = EA[1:]
                T.add_row(['E = 0, Sub B', '', Bcomp, '', ''])
                T.add_row(['', '', len(B)*'-', '', ''])
                T.add_row(['', E, A, '', ''])
                if E == '0':
                    sum = bin(int(A, 2) + int(B, 2))
                    EA = sum[2:]
                    if len(EA) == len(A):
                        E = '0'
                        A = EA
                    else:
                        E = '1'
                        A = EA[1:]
                    SC -= 1
                    T.add_row(['E = 0, Restore A', '', B, '', SC])
                    T.add_row(['', '', len(B)*'-', '', ''])
                    T.add_row(['', E, A, '', ''])
                else:
                    lst = list(Q)
                    lst[len(Q)-1] = '1'
                    Q = ''.join(lst)
                    SC -= 1
                    T.add_row(['E = 1 ,SetQn', '', A, Q, SC])
            else:
                sum = bin(int(A, 2) + int(Bcomp, 2))
                EA = sum[2:]
                while len(EA) < len(A):
                    EA = '0'+EA
                if len(EA) == len(A):
                    E = '0'
                    A = EA
                else:
                    E = '1'
                    A = EA[1:]
                # print(len(Q))

                lst = list(Q)
                # print(len(Q))
                # print(Q)
                lst[len(Q)-1] = '1'
                Q = ''.join(lst)
                SC -= 1
                T.add_row(['E = 1, Sub B and set Qn', '', Bcomp, '', ''])
                T.add_row(['', '', len(B)*'-', '', ''])
                T.add_row(['', E, A, Q, SC])

        print(T)
    else:
        print("E = 1 So, overflow occurs")

        # print('AQ is {}'.format(AQ))
        # print('B is {}'.format(B))

        # print('this is A{}'.format(A))
        # print('this is Q{}'.format(Q))
        # print('Q is {}'.format(Q))


    # print("The sign of Quotient is {} and that of remainder is {}".format(Qs, As))
