def calculate_love_score(name1, name2):
    combined = (name1 + name2).lower()
    
    true_total = sum(combined.count(letter) for letter in "true")
    love_total = sum(combined.count(letter) for letter in "love")
    
    love_score = int(str(true_total) + str(love_total))
    print(love_score)


calculate_love_score("Kanye West", "Kim Kardashian")
