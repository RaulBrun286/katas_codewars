def get_middle(string):
    
    if len(string)%2 == 0:
        mitad_par = len(string) // 2 #Refactorizable co una funcion que haga la mitad
        return string[mitad_par-1 : mitad_par+1]
    
    elif len(string) == 1:
        return string
    
    else:
        mitad_impar = len(string) // 2
        return string[mitad_impar]