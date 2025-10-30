def calculate_love_score(name1, name2):
    # Combinar ambos nombres y convertir a minúsculas
    combined_names = (name1 + name2).lower()
    
    # Contar letras de "TRUE"
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_total = t + r + u + e
    
    # Contar letras de "LOVE"
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e2 = combined_names.count("e")  # Ya lo contamos arriba, pero lo dejamos claro
    love_total = l + o + v + e2
    
    # Combinar para hacer número de 2 dígitos
    love_score = int(str(true_total) + str(love_total))
    
    print(love_score)


# Llamar la función
calculate_love_score("Kanye West", "Kim Kardashian")
