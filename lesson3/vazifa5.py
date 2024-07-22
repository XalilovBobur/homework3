class Float:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, float):
            self._value = new_value
        else:
            raise ValueError("Float qiymat kiriting")

try:
    f = Float(3.14)
    print(f.value)  
    f.value = 5.67
    print(f.value)  
    f.value = "sdkns"  
    
except ValueError as e:
    print(e)
