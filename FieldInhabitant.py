# Author: Zhekang Xu
# Date: 2023-11-12
# Description: FieldInhabitant definitions.


class FieldInhabitant:
    """
    Represents an inhabitant on a field with a symbol.

    Attributes:
    - symbol (str): The symbol representing the inhabitant on the field.

    Methods:
    - __init__(symbol: str) -> None: Initializes a FieldInhabitant object with the given symbol.
    - getSymbol() -> str: Returns the symbol of the FieldInhabitant.
    - setSymbol(symbol: str) -> None: Sets the symbol of the FieldInhabitant to the specified value.
    """

    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    def getSymbol(self) -> str:
        """
        Get the symbol of the FieldInhabitant.

        Returns:
        - str: The symbol representing the FieldInhabitant.
        """
        return self._symbol

    def setSymbol(self, symbol: str) -> None:
        """
        Set the symbol of the FieldInhabitant.

        Parameters:
        - symbol (str): The new symbol to be set.
        """
        self._symbol = symbol
