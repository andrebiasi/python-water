class Glass:
    def __init__(self, capacity):
        if capacity <=0:
            raise ValueError("Capacity must be greater than zero. Given capacity: %f" % capacity)
        
        self.capacity = capacity
        self.volume = 0

    def fill(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero. Given quantity: %f" % quantity)
        
        if quantity > self.capacity:
            raise ValueError("Glass cannot hold the given amount. Given amount: %f. Glass capacity: %f" % (quantity, self.capacity))

        self.volume = quantity