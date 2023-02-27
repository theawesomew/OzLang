from llvmlite import ir
from helpers.table import SymbolTable
from helpers.node import Node
import lark

IF_ELSE = "if_else"
IF_THEN = "if_then"
VAR_DECL = "var_decl"
CALL = "call"
RETURN = "return_statement"
FUNCTION = "function"

def Compiler ():

    int32 = ir.IntType(32)

    def __init__ (self, name=''):
        self.module = ir.Module(name=name)
        self.builder = None
        self.globalSymbols = SymbolTable()
    
    def compile (self, ast):
        for node in ast.children:
            if node.data == FUNCTION:
                func = fnDeclaration(node)
                self.globalSymbols.set_symbol()
            elif node.data == CALL:
                fnCall(node)

        return self.module

    def fnDeclaration (self, fnNode):
        fn = Node(fnNode)
        returnType = self.typ(fn.decl.children[0].value)
        argumentTypes = []
        # this is probably pretty crude but, a thing > nothing
        args = fn.arguments
        for i, arg in enumerate(args):
            if i%2 != 0:
                continue
            argumentTypes.append(self.typ(arg.value))

        fnType = ir.FunctionType(returnType, tuple(argumentTypes))
        irFunc = ir.Function(self.module, fnType, name=self.decl.children[1].value)
        block = irFunc.append_basic_block(name="entry")

        params = SymbolTable()

        for i in range(0, len(args), 2):
            type = args[i]
            identifier = args[i+1]
            stackPointer = self.builder.alloca(self.typ(type))
            params.set_symbol(identifier.value, stackPointer)
        
        self.builder = ir.IRBuilder(block)
        localSymbols = SymbolTable()
        for node in fn.body:
            if node.data == IF_THEN:
                ifthenStatement(node, localSymbols)
            elif node.data == IF_ELSE:
                ifelseStatement(node, localSymbols)
            elif node.data == VAR_DECL:
                varDeclaration(node, localSymbols)
            elif node.data == CALL:
                fnCall(node)
            elif node.date == RETURN:
                retStatement(node, localSymbols)

        return irFunc


    def fnCall (self, callNode):
        pass

    def varDeclaration (self, varNode, localSymbols):
        pass

    def retStatement (self, retNode, localSymbols):
        pass

    def ifthenStatement (self, ifNode, localSymbols):
        pass

    def ifelseStatement (self, ifelseNode, localSymbols):
        pass

    def expr (self, exprNode, localSymbols):
        pass

    def typ (self, type):
        if type == 'int':
            return ir.IntType(32)
        elif type == 'string':
            return ir.PointerType(ir.IntType(8))