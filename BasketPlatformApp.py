import difflib

## Check the similarity of two strings
def get_equal_rate(str1, str2):
   return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


class BasketPlatformApp:


    def __init__(self, name):
        self.__BasketInfos = []
        self.__name = name

    def getName(self):
        return self.__name

    def addBasketInfo(self, BasketInfo):
        self.__BasketInfos.append(BasketInfo)

    def removeBasketInfo(self, BasketInfo):
        for info in self.__BasketInfos:
            if(info == BasketInfo):
                self.__BasketInfos.remove(info)

    def getSearchCondition(self, description):
        return description

    def getMatchInfos(self, searchCondition):
        print(self.getName(), " shows suitable baskets for you：")
        suitables = []
        for info in self.__BasketInfos:
            if get_equal_rate(searchCondition, info.getLocation()) > 0.9:
                info.showInfo(False)
                suitables.append(info)
        return  suitables

    def addBasket(self, BasketInfo):
        print(self.getName(), " has a new avaible Basket \n  -- Provided by ", BasketInfo.getShopName(), ",\n  -- Located at: ", BasketInfo.getAddress())

    def addBaskets(self):
        for info in self.__BasketInfos :
            self.addBasket(info)