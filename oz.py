import lark

EBNF = open('EBNF.txt', 'r')

parser = lark.Lark(EBNF.read(), start='program')

# expected to return 3
function = r"""
    f int a: {
        return a + 1
    }

    g int b, int x: {
        if (x >= 2) {
            return b * x
        }

        return b
    }

    f(g(1, 2))
"""

tree = parser.parse(function)

print(tree)

EBNF.close()