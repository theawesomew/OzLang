import sys
import os
from ozparser import Parser

cmd, file = sys.argv[1:]

if cmd not in ["run", "compile"]:
    raise Exception("The supplied command argument is invalid. Try 'oz run' or 'oz compile'.")

if not (file.endswith(".oz") and os.path.exists(file)):
    raise Exception('Invalid file.')

parser = Parser()
print(tree := parser.parse(file))

