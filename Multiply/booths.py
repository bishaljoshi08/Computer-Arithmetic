from prettytable import PrettyTable

if __name__ == '__main__':
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

    def compPlusOne(x):
        y =x
        lst = list(x)
        for i in range(len(x)):
            
            if x[i] == '0':
                lst[i] = '1'
            else:
                lst[i] = '0'
        x = ''.join(lst)
        x = int('0b'+ x, 2)
        x += 1
        x = bin(x)
        x = x[2:]
        while len(x) <len(y):
            x = '0' +x
        return str(x)
        
    def twosComp(x):
        if x<0:
            return compPlusOne('0'+ decToBin(abs(x)))
        else:
            return '0'+ decToBin(x)

    def ashrACQR(AC,QR,Qn1):
        ACQR = AC+QR+Qn1
        ACQR = ACQR[0]+ ACQR[:len(ACQR)-1]
        AC = ACQR[:len(AC)]
        QR = ACQR[len(AC):len(AC)+len(QR)]
        Qn1 = ACQR[len(AC)+len(QR):]
        return AC, QR ,Qn1


    T = PrettyTable()
    BR = int(input("Enter the value of BR: "))
    QR = int(input("Enter the value of QR: "))
    BR = twosComp(BR)
    QR = twosComp(QR)
    AC = '0'*len(BR)
    Qn1 = '0'
    SC = len(QR)
    print("BR = {}".format(BR))
    print("QR = {}".format(QR))
    print("Qn+1 = {}".format(Qn1))
    print("AC = {} [length equal to BR]".format(AC))
    print("SC = {} [length of QR]".format(SC))

    T.field_names = ['Qn Qn+1'," BR = {}, BR'+1 = {}".format(BR, compPlusOne(BR)), 'AC', 'QR', 'Qn+1', 'SC']
    T.add_row( ['','Initial condition', AC, QR, Qn1, SC])

    while (SC !=0):
        if ((QR[len(QR)-1] == '0') and Qn1 == '1'):
            sum = bin(int(AC,2) + int(BR,2))
            y = AC
            AC = sum[2:]
            if len(AC) > len(y):
                AC = AC[1:]
            T.add_row( ['01','Add BR', BR, '', '', ''])
            T.add_row(['','',len(BR)*'-', '', '','' ])
            T.add_row( ['','', AC, '', '', ''])
            AC, QR, Qn1 = ashrACQR(AC,QR,Qn1)
            SC -= 1
            T.add_row( ['','ashr AC & QR', AC, QR, Qn1, SC])
        elif ((QR[len(QR)-1] == '1') and Qn1 == '0'):
            sum = bin(int(AC,2) + int(compPlusOne(BR),2))
            y = AC
            AC = sum[2:]
            if len(AC) > len(y):
                AC = AC[1:]
            while len(AC) < len(y):
                AC = '0'+AC
            T.add_row( ['10','Subtract BR', compPlusOne(BR), '', '', ''])
            T.add_row(['','',len(BR)*'-', '', '','' ])
            T.add_row([ '','', AC, '', '', ''])
            AC, QR, Qn1 = ashrACQR(AC,QR,Qn1)
            SC -= 1
            T.add_row( ['','ashr AC & QR', AC, QR, Qn1, SC])
        else:
            AC, QR, Qn1 = ashrACQR(AC,QR,Qn1)
            SC -= 1
            T.add_row( ['11/00','ashr AC & QR', AC, QR, Qn1, SC])

    print(T)
    # print(compPlusOne('1011'))