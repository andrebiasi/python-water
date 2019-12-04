class Glass:
    def __init__(self, capacity):
        if capacity <=0:
            raise ValueError("Capacity must be greater than zero. Given capacity: %i" % capacity)
        
        self.capacity = capacity
        self.volume = 0

    def fill(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero. Given quantity: %i" % quantity)
        
        if quantity > self.capacity:
            raise ValueError("Glass cannot hold the given amount. Given amount: %i. Glass capacity: %i" % (quantity, self.capacity))

        self.volume = quantity