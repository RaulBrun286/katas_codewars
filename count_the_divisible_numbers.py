def divisible_count(x, y, k):
    # Si el rango es inválido, devolvemos 0
    if x > y:
        return 0
        
    # Calculamos los múltiplos de k hasta y, y le restamos los múltiplos hasta x-1
    return (y // k) - ((x - 1) // k)

#def divisible_count(x, y, k):
    
    #result = 0
    
    #for i in range(x, y + 1):
        #if i % k == 0:
            #result += 1
    #return result