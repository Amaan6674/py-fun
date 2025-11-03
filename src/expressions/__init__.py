# __init__.py executes when the package (this folder) is imported for the
# first time. It is good practice to not include logic in __init__.py, but
# list artifacts exposed from the package. In that sence, 'imports' can be
# viewed as 'exports' of this package.
import os
import importlib
from pathlib import Path

try:
    # attempt to import finished solution/implementation, if present
    # from .expressions_impl import Expressions
    # 
    # programmatic import: 'from .calculator_impl import Calculator'
    p, a = Path(__file__).parent, os.path.abspath(os.curdir)
    mp=str(p.relative_to(a)).replace('\\', '/').replace('/', '.')
    pmod=mp + '.expressions_impl'
    mod = importlib.import_module(pmod)
    # print(f'--> import: \'{pmod}\'')    # 'src.calculator.calculator_impl'
    # 
    # expose objects imported from module
    Expressions=mod.Expressions_sol
#
except ImportError:
    # if no solution is present, import the alternative
    from .expressions import Expressions

from .main import main