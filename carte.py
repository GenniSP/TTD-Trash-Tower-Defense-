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
    costo=-1
    if tipo==0:
        power=rnd.randint(1,3)
        vita=rnd.randint(5,6)
        costo=rnd.randint(1,3)
    if tipo==1:
        power=rnd.randint(4,7)
        vita=rnd.randint(6,8)
        costo=rnd.randint(4,5)
    if tipo==2:
        power=rnd.randint(8,9)
        vita=rnd.randint(8,9)
        costo=rnd.randint(6,7)
    return Carta(power,tipo,costo,vita)

def make_list_cards():
    card1=spawn_carte()
    card2=spawn_carte()
    card3=spawn_carte()
    return [card1,card2,card3]
