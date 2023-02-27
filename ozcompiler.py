from llvmlite import ir
import lark

def Compiler ():

    int32 = ir.IntType(32)

    symbols = {}

    def __init__ (self, name=''):
        self.module = ir.Module(name=name)
    
    def compile (self, ast):
        if isinstance(lark.Token):
            if ast.type == 'NUMBER':
                return int32(ast.value)
            elif ast.type == 'STRING':
                return ir.Constant.literal_array([*ast.value])
        else:
            

    def fnDeclaration (self, fnNode):
        pass

    def fnCall (self, callNode):
        pass

    def varDeclaration (self, varNode):
        pass

    def retStatement (self, retNode):
        pass

    def ifthenStatement (self, ifNode):
        pass

    def ifelseStatement (self, ifelseNode):
        pass

    def expr (self, exprNode):
        pass