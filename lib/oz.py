import sys
import os
from ozparser import Parser
from helpers.node import Node

cmd, file = sys.argv[1:]

if cmd not in ["run", "compile"]:
    raise Exception("The supplied command argument is invalid. Try 'oz run' or 'oz compile'.")

if not (file.endswith(".oz") and os.path.exists(file)):
    raise Exception('Invalid file.')

parser = Parser()
tree = parser.parse(file)
