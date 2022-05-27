print("Welcome to Love Calculator! ❤️ ")
yourname = list(input("What's your name? ").lower())
partner_name = list(input("What's your partners name? ").lower())
yourname.extend(partner_name)
true, love = "true", "love"
true_num, love_num = 0, 0

# your name
for i in yourname:
    if i in true:
        true_num += 1

    if i in love:
        love_num += 1

match_percentage = str(true_num) + str(love_num)
print(f"You both have a match of %{match_percentage}")

