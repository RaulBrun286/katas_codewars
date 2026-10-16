def diamond(n):
    result = ""
    if n <= 0 or n % 2 == 0:
        return None
    else:
        for i in range (1, n+1, 2):
            espaces = (n - i) // 2
            result += (" " * espaces) + ("*" * i ) + "\n" 
        for i in range (n-2, 0, -2):
            if i % 2 != 0:
                espaces = (n - i) // 2
                result += (" " * espaces) + ("*" * i) + "\n"
    return result