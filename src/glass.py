class Glass:
    def __init__(self, capacity):
        if capacity <=0:
            raise ValueError("Capacity must be greater than zero. Given capacity: {0}".format(capacity))
        
        self.capacity = capacity
        self.volume = 0

    def fill(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero. Given quantity: {0}".format(quantity))
        
        if quantity > self.capacity:
            raise ValueError("Glass cannot hold the given amount. Given amount: {0}. Glass capacity: {1}".format(quantity, self.capacity))

        self.volume = quantity