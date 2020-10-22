class Identificador:

    def __init__(self, ident, value, type):
        self.ident = ident
        
        self.value = value
        self.type = type

    def __str__(self):
        return self.ident + '\t' + self.type.name + '\t' + self.value


    __repr__ = __str__