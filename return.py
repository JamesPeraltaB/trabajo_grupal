def salario(h_t):
    return(h_t*20)
def con_bono(h_t):
    return(salario(h_t))+50

salario(8), con_bono(8)