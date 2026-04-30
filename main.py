import numpy as np 
import sympy as sp
from sympy.parsing.sympy_parser import transformations
from sympy import init_printing
init_printing()

CLI = True
auto_def_x = True
vars_dict = {}
ans = None
Numerical = False

def init():
    if auto_def_x:
        x = sp.symbols("x")
    e = sp.E
    pi = sp.pi
    vars_dict["e"] = e
    vars_dict["pi"] = pi

def mainloop(ans=ans):
    inp = str(input("> "))
    if inp == "":
        pass
    elif inp == "exit" or inp == "break":
        return 0, ans
    elif inp == "dec":
        print("ans =", sp.N(ans))
        return 1, ans
    
    simp = sp.parse_expr(inp, local_dict=vars_dict, transformations='all')
    try:
        if Numerical:
            simpN = sp.N(simp)
            print(simpN)
        else:
            sp.pprint(simp)
        ans = simp
        return 1, ans
    except:
        print("Error parsing string:")
        print(inp, "-->", simp)
        return 0, ans

if __name__ == "__main__":
    init()
    while True:
        main, ans = mainloop(ans=ans)
        if main == 0:
            break

