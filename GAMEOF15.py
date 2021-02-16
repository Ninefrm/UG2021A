#Clean terminal
from os import system
cls = lambda: system('cls')

class GameOf15():
    def __init__(self) -> None:
        Tablero = [1,2,3,4,
                    5,6,7,8,
                    9,10,11,12,
                    13,14,15, "X"]
        cls()
        self.ImprimirTablero(Tablero)
        while True:
            Move = input("Movimiento: ")
            self.MoveTo(Tablero,Move)
            self.ImprimirTablero(Tablero)
            
    
    def ImprimirTablero(self, Tablero):
        for i in range(0,4):
            print(str(Tablero[(i*4)])+ "    " +str(Tablero[(i*4)+1])+ "    " +str(Tablero[(i*4)+2])+"   " +str(Tablero[(i*4)+3]))
    
    def MoveTo(self, Tablero, dir):
        print(dir)
        Pos = (Tablero.index("X"))
        if dir == "w":
            if Pos <= 3:
                cls()
                print("INVALID")
            else:
                Temp = Tablero[Pos-4]
                Tablero[Pos] = Temp
                Tablero[Pos-4] = "X"
                cls()
                pass
        elif dir == "a":
            if Pos in (0,4,8,12):
                cls()
                print("INVALID")
            else:
                Temp = Tablero[Pos-1]
                Tablero[Pos] = Temp
                Tablero[Pos-1] = "X"
                cls()
                pass
        elif dir == "s":
            if 12 <= Pos <=15:
                cls()
                print("INVALID")
            else:
                Temp = Tablero[Pos+4]
                Tablero[Pos] = Temp
                Tablero[Pos+4] = "X"
                cls()
                pass
        elif dir == "d":
            if Pos in (3,7,11,15):
                cls()
                print("INVALID")
            else:
                Temp = Tablero[Pos+1]
                Tablero[Pos] = Temp
                Tablero[Pos+1] = "X"
                cls()
                pass
        else:
            cls()
            print("INVALID")
            

    
            


GameOf15 = GameOf15()
        