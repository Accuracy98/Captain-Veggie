from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, symbol: str, name, points) -> None:
        self._name = name
        self._points = points
        super().__init__(symbol)
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPoints(self):
        return self._points

    def setPoints(self, points):
        self._points = points

    def  __str__(self) -> str:
        return super().__str__()
    
