class Room:
    def __init__(self, name, price, color, size) -> None:
        self.name = name
        self.price = price
        self.color = color
        self.__size = size

    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self,value):
        if type(value)==int:
            self.__dict__['__size']=value
        else:
            raise ValueError("Invalid size")
        
    @size.deleter
    def size(self):
        raise PermissionError("You cannot delete")
        del self.__size

room = Room( "Bobur",300,"red",200)
print(room.size)  

del room.size
print(room.size) 