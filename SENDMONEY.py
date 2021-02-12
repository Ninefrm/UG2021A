# FONSECA ROMERO SAMUEL MAXIMILIANO
# SEND + MORE = MONEY

#TIME
from time import sleep
from datetime import datetime, timedelta

class SendMoney():
    def __init__(self):
        Solucion = 0 
        nowS = datetime.now()
        for S in range(0,10):
            # print("S " + str(S))
            for E in range(0,10):
                if E == S:
                    pass
                else:
                    # print("E " + str(E))
                    for N in range(0,10):
                        if N == S or N == E:
                            pass
                        else:
                            # print("N " + str(N))
                            for D in range(0,10):
                                if D == S or D == E or D == N:
                                    pass
                                else:
                                    # print("D " + str(D))
                                    for M in range(0,10):
                                        if M == S or M == E or M == N or M == D:
                                            pass
                                        else:
                                            # print("M " + str(M))
                                            for O in range(0,10):
                                                if O == S or O == E or O == N or O == D or O == M:
                                                    pass
                                                else:
                                                    # print("O " + str(O))
                                                    for R in range(0,10):
                                                        if R == S or R == E or R == N or R == D or R == M or R == O:
                                                            pass
                                                        else:
                                                            # print("R " + str(R))
                                                            for Y in range(0,10):
                                                                if Y == S or Y == E or Y == N or Y == D or Y == M or Y == O or Y == R:
                                                                    pass
                                                                else:
                                                                    # print("Y " + str(Y))
                                                                    # print(str(S)+str(E)+str(N)+str(D))
                                                                    # print(str(M)+str(O)+str(R)+str(E))
                                                                    # print(str(M)+str(O)+str(N)+str(E)+str(Y))
                                                                    # sleep(10)
                                                                    if (int(str(S)+str(E)+str(N)+str(D)))+(int(str(M)+str(O)+str(R)+str(E))) == (int(str(M)+str(O)+str(N)+str(E)+str(Y))):
                                                                        print(str(S)+str(E)+str(N)+str(D))
                                                                        print(str(M)+str(O)+str(R)+str(E))
                                                                        print(str(M)+str(O)+str(N)+str(E)+str(Y))
                                                                        print("----------")
                                                                        Solucion = Solucion+1
                                                                        # sleep(60)
                                                                        # break
        print(nowS.strftime("%Y/%m/%d %H:%M:%S"))
        nowS = datetime.now()
        print(nowS.strftime("%Y/%m/%d %H:%M:%S"))
        print("Se encontrarion " + str(Solucion) + " soluciones.")
        pass

SendMoney = SendMoney()
