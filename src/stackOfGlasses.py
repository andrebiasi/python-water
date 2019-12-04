from glass import Glass

class StackOfGlasses:
    def __init__(self, numberOfRows):
        GLASS_CAPACITY = 0.25

        if numberOfRows <=0:
            raise ValueError("Number of rows must be greater than zero. Given number of rows: {0}".format(numberOfRows))
        
        if not isinstance(numberOfRows, int):
            raise ValueError("Number of rows must be an integer. Given number of rows: {0}".format(numberOfRows))

        self.stack = []
        for row in range(numberOfRows):
            numberOfColumns = row + 1
            self.stack.append([Glass(GLASS_CAPACITY)] * numberOfColumns)
        
    def pour(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero. Given quantity: {0}".format(quantity))

        for row in self.stack:
            quantityToFill = quantity / (len(row))
            for glass in row:
                if quantityToFill >= glass.capacity:
                    glass.fill(glass.capacity)
                    quantity -= glass.capacity 
                else:
                    glass.fill(quantityToFill)
                    quantity -= quantityToFill

            if quantity <= 0:
                break

    def getAmountAt(self, row, column):
        if row <= 0:
            raise ValueError("Row must be greater than zero. Given row: {0}".format(row))
        if column <= 0:
            raise ValueError("Column must be greater than zero. Given column: {0}".format(column))

        try:
            return self.stack[row - 1][column - 1].volume
        except IndexError:
            raise ValueError("Glass does not exist with given row: %i column: %i" % (row, column))
        