from prettytable import PrettyTable

if __name__ == '__main__':

    def shrEAQ(E,A,Q):
        EAQ = E + A + Q
        EAQ = '0'+ EAQ[:(len(EAQ)-1)]
        E = EAQ[0]
        A = EAQ[1:(len(A)+1)]
        Q = EAQ[len(A)+1:]
        return E,A,Q
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
        if x<0:
            return 1, decToBin(abs(x))
        else:
            return 0, decToBin(x)
    
    T = PrettyTable()
    B = int(input("Enter the value of B: "))
    Q = int(input("Enter the value of Q: "))
    Bs, B = remove_sign_and_convert_binary(B)
    Qs, Q = remove_sign_and_convert_binary(Q)
    As = Qs ^ Bs
    E = '0'
    A = '0'*len(B)
    
    SC = len(Q)
    print("Bs = {}".format(Bs))
    print("B = {}".format(B))
    print("Qs = {}".format(Qs))
    print("Q = {}".format(Q))
    print("Sign of product (As) = Qs ⊕ Bs = {}".format(As))
    print("Qs = Qs ⊕ Bs = {}".format(As))
    print("A = {} [length equal to B]".format(A))
    print("SC = {}[length of Q]".format(SC))
    

    T.field_names = ['Multiplicant B = {}'.format(B), 'E', 'A', 'Q', 'SC']

    T.add_row( ['Initial condition', E, A, Q,SC])
    while (SC !=0):
        if (Q[len(Q)-1] == '1'):
            sum = bin(int(A,2) + int(B,2))
            EA = sum[2:]
            if len(EA) == len(A):
                E = '0'
                A = EA
            else:
                E ='1'
                A = EA[-len(A):]

            A = EA[-len(A):]
            T.add_row( ['Qn =1 add B', '', B, '',''])
            T.add_row(['','',len(A)*'-','',''] )

            T.add_row( ['', E, A, '',''])
            E,A,Q = shrEAQ(E,A,Q)
            SC -= 1
            T.add_row( ['SHR EAQ', E, A, Q,SC])
        else:
            E,A,Q = shrEAQ(E,A,Q)
            SC -= 1
            T.add_row( ['Qn = 0,SHR EAQ', E, A, Q,SC])

print(T)
# if (Bs^Qs == 1):
#     print("The sign is negative")
# else:
#     print("The sign is positive")