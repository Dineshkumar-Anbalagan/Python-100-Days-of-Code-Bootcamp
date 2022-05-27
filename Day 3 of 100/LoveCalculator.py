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

love_score = int(str(true_num) + str(love_num))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
