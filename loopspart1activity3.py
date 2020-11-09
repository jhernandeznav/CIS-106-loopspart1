def yes_or_no():
    answer_ = False
    if input('Do you want to continue this program? (y/n)').lower() == 'y':
        answer_ = True
    while answer_:
        last_name = input("Enter your last name: ")
        anynumber = int(input("Enter first score: "))
        anynum = int(input("Enter second score: "))
        answer = ((anynumber + anynum) / 200) * 100
        print(last_name)
        print(answer, "percent")
        if input("Do you want to run the program again? (y/n)").lower() == 'n':
            answer_ = False
    print('Goodbye!')


def main():
    yes_or_no()


main()
