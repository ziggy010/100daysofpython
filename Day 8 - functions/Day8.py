def calculate_love_score(name1, name2):
    total_true_in_name1 = 0;
    total_true_in_name2 = 0;
    total_love_in_name1 = 0;
    total_love_in_name2 = 0;
    total_true = 0;
    total_love = 0;
    love_score = "";

    for letter in name1:
        if letter in "true":
            total_true_in_name1 += 1;
        
        if letter in "love":
            total_love_in_name1 += 1;
    
    for letter in name2:
        if letter in "true":
            total_true_in_name2 += 1;
        if letter in "love":
            total_love_in_name2 += 1;
    
    total_true = total_true_in_name1 + total_true_in_name2;
    total_love = total_love_in_name1 + total_love_in_name2;

    love_score = str(total_true) + str(total_love);

    print(love_score);



# calculate_love_score("Angela Yu", "Jack Bauer");
calculate_love_score("Kanye West", "Kim Kardashian")









