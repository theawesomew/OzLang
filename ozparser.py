import lark

class Parser ():
    def __init__ (self):
        self.parser = lark.Lark('''                
            program: function+ call

            function: decl ":" body

            body: "{" statement* return_statement "}"
            decl: TYPE IDENTIFIER arguments
            arguments: TYPE IDENTIFIER ("," TYPE IDENTIFIER)* 

            statement: IF "(" expression ")" "{" (statement | return_statement) "}"
                    | IF "(" expression ")" "{" (statement | return_statement) "}" ELSE "{" (statement | return_statement) "}"
                    | TYPE IDENTIFIER "=" (STRING | NUMBER | expression)
                    | call

            expression: expression OPERATOR expression
                    | IDENTIFIER OPERATOR IDENTIFIER
                    | IDENTIFIER OPERATOR expression
                    | IDENTIFIER OPERATOR (STRING | NUMBER)
                    | call

            call: IDENTIFIER "(" (call | expression | STRING | NUMBER) ("," (call | expression | STRING | NUMBER))* ")"

            return_statement: RETURN (call | IDENTIFIER | expression | STRING | NUMBER)

            IF: "if" 
            ELSE: "else"
            RETURN: "return"
            OPERATOR: "+" | "-" | "*" | "/" | "==" | "<" | ">" | "!=" | "<=" | ">="
            TYPE: "string" | "int"
            IDENTIFIER: /[a-zA-Z_][a-zA-Z_]*/
            STRING: /\".*?\"/
            NUMBER: /\-?[0-9]+/

            %import common.SIGNED_NUMBER
            %import common.ESCAPED_STRING
            %import common._STRING_INNER
            %import common.WS
            %ignore WS
            ''', start='program')
    
    def parse (self, file):
        _file = open(file)
        tree = self.parse_text(_file.read())
        _file.close()

        return tree
    
    def parse_text (self, text):
        return self.parser.parse(text)
