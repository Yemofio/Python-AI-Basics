class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def add(x, y, z):
        return x + y + z

print(Math.add(1, 2))      # Output: 3
print(Math.add(1, 2, 3))   # Output: 6
