class Customer:
    """User of TooGoodToGO"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def findBasket(self, description, App):
        print("User " + self.getName() + ", searching a backet with info: " + description )
        print()
        return App.getMatchInfos(App.getSearchCondition(description))

    def viewBasket(self, BasketInfos):
        size = len(BasketInfos)
        return BasketInfos[size-1]

    def buyBasket(self, BasketInfo, App):
        """ command Basket on App """
        print(self.getName(), " made a new command on ", App.getName(), " for a basket in ",  BasketInfo.getShopName())