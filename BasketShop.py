from BasketInfo import BasketInfo


class BasketShop:
    """ BasketShop class """

    def __init__(self, name):
        self.__name = name
        self.__BasketInfo = None

    def getName(self):
        return self.__name

    def setBasketInfo(self, address, location, price):
        self.__BasketInfo = BasketInfo(location, price,  address, self)

    def publishBasketInfo(self, App):
        App.addBasketInfo(self.__BasketInfo)
        print(self.getName() + " pushes a Basket on ", App.getName(), ": ")
        self.__BasketInfo.showInfo()


