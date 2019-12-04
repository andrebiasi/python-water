from glass import Glass

class StackOfGlasses:
    def __init__(self, numberOfRows):
        GLASS_CAPACITY = 0.25

        if numberOfRows <=0:
            raise ValueError("Number of rows must be greater than zero. Given number of rows: %i" % numberOfRows)
        
        if not isinstance(numberOfRows, int):
            raise ValueError("Number of rows must be an integer. Given number of rows: %i" % numberOfRows)

        self.stack = []
        for row in range(numberOfRows):
            rowOfGlasses = []
            for column in range(row):
                rowOfGlasses.append(Glass(GLASS_CAPACITY))
            self.stack.append(rowOfGlasses)
        
    def pour(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero. Given quantity: %i" % quantity)

        pass

    def getAmountAt(self, row, column):
        pass
        