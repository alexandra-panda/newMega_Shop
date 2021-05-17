class BasketInfo:
    """Food Basket info"""

    def __init__(self, location, price,  address, Shop):
        self.__location = location
        self.__price = price
        self.__address = address
        self.__Shop = Shop

    def getLocation(self):
        return self.__location

    def getAddress(self):
        return self.__address

    def getShopName(self):
        return self.__Shop.getName()

    def showInfo(self, isShowShop = True):
        print(" ++ Location: {}".format(self.__location) )
        print(" ++ Price: {}" .format( str(self.__price) + " euros") )
        print(" ++ Address: {}" .format( self.__address) )
        print(" ++ Shop: " + self.getShopName() if isShowShop else "")
        print()