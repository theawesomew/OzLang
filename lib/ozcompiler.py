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
STATEMENT = "statement"
INT = 'int'
STRING = 'string'

class Compiler ():

    int32 = ir.IntType(32)

    def __init__ (self, name=''):
        self.module = ir.Module(name=name)
        self.builder = None
        self.globalSymbols = SymbolTable()
    
    def compile (self, ast):
        for node in ast.children:
            if node.data == FUNCTION:
                fnName, func = self.fnDeclaration(node)
                self.globalSymbols.set_symbol(fnName, '')
            elif node.data == CALL:
                self.fnCall(node)
        
        return self.module

    def fnDeclaration (self, fnNode):
        fn = Node(fnNode)
        returnType = self.typ(fn.decl.children[0].value)
        argumentTypes = []
        # this is probably pretty crude but, a thing > nothing
        args = fn.arguments.children
        for i, arg in enumerate(args):
            if i%2 != 0:
                continue
            argumentTypes.append(self.typ(arg.value))

        fnName = fn.decl.children[1].value
        fnType = ir.FunctionType(returnType, tuple(argumentTypes))
        irFunc = ir.Function(self.module, fnType, name=fnName)
        block = irFunc.append_basic_block(name="entry")

        params = SymbolTable()
        self.builder = ir.IRBuilder(block)

        for i in range(0, len(args), 2):
            type = args[i]
            identifier = args[i+1]
            stackPointer = irFunc.args[i]
            params.set_symbol(identifier.value, stackPointer)
        
        localSymbols = SymbolTable()
        for node in fn.body.children:
            if node.data == STATEMENT:
                self.statement(node, localSymbols)
            elif node.data == RETURN:
                self.retStatement(node, localSymbols)            

        return fnName, irFunc

    def statement (self, statementNode, localSymbols):
        for node in statementNode.children:
            if node.data == IF_THEN:
                self.ifthenStatement(node, localSymbols)
            elif node.data == IF_ELSE:
                self.ifelseStatement(node, localSymbols)
            elif node.data == VAR_DECL:
                self.varDeclaration(node, localSymbols)
            elif node.data == CALL:
                self.fnCall(node)
            elif node.data == RETURN:
                self.retStatement(node, localSymbols)

    def fnCall (self, callNode):
        pass

    # TODO: String variable declaration
    def varDeclaration (self, varNode, localSymbols): 
        varIdentifier = varNode.children[1].value

        if localSymbols.has_symbol(varIdentifier):
            raise Exception('Variable with same name is already declared! All variables in Oz are immutable')
        
        varType = self.typ(varNode.children[0])

        if varType == self.int32:
            varValue = varType(varNode.children[2].value) 
            self.builder.store(varValue, sp := self.builder.alloca(varType))
            localSymbols.set_symbol(varIdentifier, sp)

    def retStatement (self, retNode, localSymbols):
        valueToBeReturned = retNode.children[1].value
        typeOfValueToBeReturned = retNode.children[1].type

        if typeOfValueToBeReturned == 'IDENTIFIER':
            if not localSymbols.has_symbol(valueToBeReturned):
                raise Exception('Local variable not declared!')
            
            self.builder.ret(self.builder.load(localSymbols.get_symbol(valueToBeReturned)))
        elif typeOfValueToBeReturned == 'NUMBER':
            self.builder.ret(self.int32(valueToBeReturned))



    def ifthenStatement (self, ifNode, localSymbols):
        pass

    def ifelseStatement (self, ifelseNode, localSymbols):
        pass

    def expr (self, exprNode, localSymbols):
        pass

    def typ (self, type):
        if type == INT:
            return ir.IntType(32)