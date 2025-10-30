def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    # Contar letras de TRUE
    true_total = 0
    for letter in "true":
        true_total += combined.count(letter)
    
    # Contar letras de LOVE
    love_total = 0
    for letter in "love":
        love_total += combined.count(letter)
    
    # Combinar y mostrar
    love_score = int(str(true_total) + str(love_total))
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")
