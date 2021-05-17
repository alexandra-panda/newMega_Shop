from BasketPlatformApp import BasketPlatformApp
from BasketShop import BasketShop
from Customer import Customer

if __name__ == "__main__":
    myAPP = BasketPlatformApp("NewMega-Shop")
    Alexa_Sakura = BasketShop("Alexa_Sakura");
    Alexa_Sakura.setBasketInfo("La Defense Parvis 15, 92000, Haut-Seine", "4 temps commercial center", 3.99)
    Alexa_Sakura.publishBasketInfo(myAPP)
    Auchan = BasketShop("Auchan")
    Auchan.setBasketInfo("22 Rue Alma, 92240, Courbevoie", "Supermarcket A2Pas" , 4.0)
    Auchan.publishBasketInfo(myAPP)
    Sushi = BasketShop("Sushi Shop")
    Sushi.setBasketInfo("La Defense Parvis 15, 92000, Haut-Seine", "4 temps commercial center", 6.99)
    Sushi.publishBasketInfo(myAPP)
    print()

    myAPP.addBaskets()
    print()

    jemaloQ = Customer("jemaloQ")
    BasketInfos = jemaloQ.findBasket("4 temps commercial center", myAPP)
    print()
    print("Searching available baskets for you ……")
    print()
    AppropriateBasket = jemaloQ.viewBasket(BasketInfos)
    jemaloQ.buyBasket(AppropriateBasket, myAPP)