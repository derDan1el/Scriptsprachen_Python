import numpy as np

# Definition der Funktionen
def psi1(x):
    return x, np.sqrt(np.abs(x**2 - 1))

def psi2(u, v):
    return u - v

def psi3(y):
    return np.log(np.abs(y))

def phi1(x):
    return psi1(x)

def phi2(u, v):
    return u + v

def phi3(y):
    return -np.log(np.abs(y))

# Zusammensetzen der Funktionen
def f(x):
    u, v = psi1(x)
    w = psi2(u, v)
    return psi3(w)

def g(x):
    u, v = phi1(x)
    w = phi2(u, v)
    return phi3(w)

# Numerische Auswertung der Funktionen
def f_tilde(x):
    return f(x)

def g_tilde(x):
    return g(x)

# Berechnung der relativen Kondition
def relative_condition(h, x):
    h_x = h(x)
    dh_dx = (h(x + 1e-8) - h(x - 1e-8)) / (2 * 1e-8)
    return np.abs(x / h_x * dh_dx)

# Beispielwert
x = 30

# Berechnung der relativen Kondition
kappa_rel_f = relative_condition(f_tilde, x)
kappa_rel_g = relative_condition(g_tilde, x)

print(f"Relative Kondition von f an der Stelle {x}: {kappa_rel_f}")
print(f"Relative Kondition von g an der Stelle {x}: {kappa_rel_g}")