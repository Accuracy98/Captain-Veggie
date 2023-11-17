from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, symbol: str, value) -> None:
        self._value = value
        super().__init__(symbol)
    
    def getSymbol(self) -> str:
        return super().getSymbol()

    def getValue(self):
        return self._value

    def setSymbol(self, symbol):
        self._symbol = symbol

    def setValue(self, value):
        self._value = value

    def  __str__(self) -> str:
        return super().__str__()
    
