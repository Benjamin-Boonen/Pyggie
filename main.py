import numpy as np 
import sympy as sp 

CLI = True
auto_def_x = True

def init():
    if auto_def_x:
        x = sp.symbols("x")
    e = sp.E
    pi = sp.pi

def mainloop():
    inp = str(input("> "))
    if inp == "":
        pass
    if inp == "exit" or inp == "break":
        return 0
    
    simp = sp.parse_expr(inp)
    
    try:
        simp.subs(e, sp.E)
        simp.subs(pi, sp.pi)
        simp = sp.N(simp)
        print(simp)
        return 1
    except:
        print("Error parsing string:")
        print(inp, "-->", simp)
        return 0

if __name__ == "__main__":
    init()
    while True:
        main = mainloop()
        if main == 0:
            break

