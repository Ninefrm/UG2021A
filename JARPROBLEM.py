import random

def jarDecision(Jar1, Jar2, option):
    if option == 1:
        print("Jarra 1: Llena al máximo")
        Jar1.fillMax()
    if option == 2:
        print("Contenido Jarra 2 a Jarra 1")
        Jar1.fill(Jar2.toOther(Jar1.need()))
        # pass
    if option == 3:
        print("Jarra 1: Vacia")
        Jar1.reset()
    if option == 4:
        print("Jarra 2: Llena al máximo")
        Jar2.fillMax()
    if option == 5:
        print("Contenido Jarra 1 a Jarra 2")
        Jar2.fill(Jar1.toOther(Jar2.need()))
        # pass
    if option == 6:
        print("Jarra 2: Vacia")
        Jar2.reset()
    

class Jar:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def need(self):
        return self.limit - self.current

    def reset(self):
        self.current = 0

    def fillMax(self):
        self.current = self.limit

    def fill(self, fill):
        if (self.current + fill <= self.limit):
            self.current += fill
            # self.object()
        else:
            self.current = self.limit
            # self.object()
    
    def toOther(self, value):
        # print(value)
        if (self.current >= value):
            self.current -= value
            return value
        else: 
            toR = self.current
            self.current = 0
            return toR

    def object(self, value):
        return self.current == value

def jarProblem(jar1, jar2, value):
    X = 1
    while X:
        jarDecision(jar1, jar2, random.randrange(1,6)) 
        # print("Jarra 1: " + str(jar1.current))
        # print("Jarra 2: " + str(jar2.current))
        if jar1.current == 0 and jar2.current == 0:
            print("----------------------------------- RESET -----------------------------------")
        if jar1.object(value):
            print("Resolved")
            X = 0
        print("Jarra 1: " + str(jar1.current))
        print("Jarra 2: " + str(jar2.current))



jarProblem(Jar(5), Jar(3), 4)