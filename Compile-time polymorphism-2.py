#default arguments
class Math:
    def add(self, x, y, z=0):
        return x + y + z

m = Math()
print(m.add(1, 2))      # Output: 3
print(m.add(1, 2, 3))   # Output: 6


#variable-length argument lists, also known as *args and **kwargs
class Math:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]

m = Math()
print(m.add(1, 2))      # Output: 3
print(m.add(1, 2, 3))   # Output: 6


#type annotations
class Math:
    def add(self, x: int, y: int) -> int:
        return x + y

    def add(self, x: int, y: int, z: int) -> int:
        return x + y + z

m = Math()
print(m.add(1, 2))      # Output: 3
print(m.add(1, 2, 3))   # Output: 6

