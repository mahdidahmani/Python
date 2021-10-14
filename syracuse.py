# Calcule de la suite de Syracuse 
# 1er Programme sur Python 


def syracuse(Nombre,Count,Max) :
    while Nombre != 1 :
        if Nombre%2 == 0 :
            Nombre = Nombre // 2
        else :
            Nombre = Nombre * 3 + 1
        print(Count," : ",Nombre)
        Count += 1 
        if Nombre >= Max :
            Max = Nombre
    return Count,Max
Nombre = int (input("Entre le Nombre :"))
Count = int
Max = int
print(Count," : ",Nombre)
Count,Max = syracuse(Nombre,0,0)
print("La durée du vol pour ",Nombre," est de ",Count,"et son altitude est de",Max,".")