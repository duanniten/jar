class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        return f'{self._cookies * "🍪"}'

    def deposit(self, n):
        if not self.check_value(n):
            raise ValueError
        if n + self._cookies > self.capacity:
            raise ValueError
        self._cookies += n

    def withdraw(self, n):
        if not self.check_value(n):
            raise ValueError
        if self._cookies - n < 0:
            raise ValueError
        self._cookies -= n

    def check_value(self, n):
        if not isinstance(n, int):
            return False
        elif n < 0:
            return False
        return True 
        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, c):
        if not self.check_value(c):
            raise ValueError
        self._capacity = c
            

    @property
    def size(self):
        return self._cookies
    
    @size.setter
    def size(self, n):
        self._cookies = n
    
    