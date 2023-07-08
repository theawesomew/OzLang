from lark import Lark

l = Lark.open("syntax.lark", rel_to=__file__, parser="lalr")