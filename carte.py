import random as rnd


class Carta:
    def __init__(self,power,tipo,costo,vita):
        self.costo=costo
        self.power=power
        self.tipo=tipo
        self.vita=vita
        

    



def spawn_carte():
    tipo=rnd.randint(0,2)
    power=-1
    vita=-1
    if tipo==0:
        power=rnd.randint(1,3)
        vita=rnd.randint(5,6)
    if tipo==1:
        power=rnd.randint(4,7)
        vita=rnd.randint(6,8)
    if tipo==2:
        power=rnd.randint(8,10)
        vita=rnd.randint(8,10)
    return Carta(power,tipo,rnd.randint(3,8),vita)

def make_list_cards():
    card1=spawn_carte()
    card2=spawn_carte()
    card3=spawn_carte()
    return [card1,card2,card3]
