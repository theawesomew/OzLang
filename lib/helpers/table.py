
class SymbolTable ():

    def __init__ (self):
        self.symbols = {}

    def get_symbol(self, name):
        if name not in self.symbols:
            raise Exception('Referencing uninitialized variable.')
        
        return self.symbols[name]
    
    def set_symbol(self, name, sp):
        if name in self.symbols:
            raise Exception('Variable is already declared! All variables in Oz are immutable.')
        
        self.symbols[name] = sp