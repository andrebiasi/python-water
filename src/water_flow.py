import sys
from stackOfGlasses import StackOfGlasses

if __name__ == "__main__":
    try:
        row = int(sys.argv[1])
        column = int(sys.argv[2])
        amount = float(sys.argv[3])

        stack = StackOfGlasses(row)
        stack.pour(amount)
        
        amountInGlass = stack.getAmountAt(row, column)
        print("The amount in row %i, column %i is: %f" % (row, column, amountInGlass))
        
    except ValueError as err:
        print("Error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise