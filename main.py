import numpy as np 
import sympy as sp 

CLI = True
auto_def_x = True

def init():
    if auto_def_x:
        x = sp.symbols("x")

def mainloop():
    inp = str(input(">"))
    if inp == "":
        continue
    if inp == "exit" or inp == "break":
        return 1

    simp = sp.parse_expr(inp)
