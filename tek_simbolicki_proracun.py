import sympy as sp

# simboličke promenljive
Vin, R1, R2, R3, R4, RL = sp.symbols('Vin R1 R2 R3 R4 RL', positive=True, real=True)
Vp, Vn, Vo, IL = sp.symbols('Vp Vn Vo IL')

# napon na + ulazu
Vp = Vin * R2 / (R1 + R2)

# idealni operacioni pojačavač
Vn = Vp

# KCL u čvoru invertujućeg ulaza
eq1 = (Vn - Vo)/R3 + (Vn - IL*RL)/R4

# rešavanje jednačine po IL
solution = sp.solve(eq1, IL)

IL_expr = sp.simplify(solution[0])

print("Simbolički izraz za izlaznu struju IL:")
sp.pretty_print(IL_expr)