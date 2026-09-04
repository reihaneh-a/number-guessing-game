import random

while True:

    number = random.randint(1, 999)
    print(number)

    print("من یک عدد انتخاب کردم! ")
    print("حدس بزن عدد چیست!")

    attempt = 0

    while attempt < 10:
        guess_input = input("عدد را حدس بزنید:").strip()


        if not guess_input.isdigit():
            print("لطفا فقط عدد انگلیسی وارد کنید!")
            continue

        if len(guess_input)> 3:
            print("حداکثر عدد سه رقمی وارد کنید")
            continue

        guess = int(guess_input)

        if guess == 0:
            print("دوباره تلاش کنید!")
            continue

        attempt += 1
        print("تلاش شماره:", attempt)

        secret_len = len(str(number))
        guess_len = len(str(guess))
        positions = min(secret_len, guess_len)

        sadgan = number // 100
        dahgan = (number // 10) % 10
        yekan = number % 10

        guess_sadgan = (guess // 100) % 10
        guess_dahgan = (guess // 10) % 10
        guess_yekan = guess % 10

        # guess_digits = set(str(guess))
        guess_digits = set(guess_input.zfill(3))
        correct = 0
        digit_correct = 0


        if positions >= 3:
            if guess_sadgan == sadgan:
                print("صدگان درسته")
                correct += 1
            elif str(sadgan) in guess_digits:
                print("عدد صدگان درسته ولی جاش درست نیست")
            else:
                print("عدد صدگان درست نیست")

        if positions >= 2:
            if guess_dahgan == dahgan:
                print("دهگان درسته")
                correct += 1
            elif str(dahgan) in guess_digits:
                print("عدد دهگان درسته ولی جاش درست نیست")
            else:
                print("عدد دهگان درست نیست")

        if positions >= 1:
            if guess_yekan == yekan:
                print("یکان درسته")
                correct += 1
            elif str(yekan) in guess_digits:
                print("عدد یکان درسته ولی جاش درست نیست")
            else:
                print("عدد یکان درست نیست")

        for digit in [str(sadgan), str(dahgan), str(yekan)]:
            if digit in guess_digits:
                digit_correct += 1

        position_percent = (correct / positions) * 100
        print(" درصد درستی جایگاه:", round(position_percent, 2), '%')

        digit_percent = (digit_correct / 3) * 100
        print("درصد درستی رقم",round(digit_percent,2),'%')

        if guess == number:
            print("کامل درست حدس زدید", number)
            break

        print("دوباره حدس بزن!")

    if attempt == 10:
        print("فرصت شما تموم شده عدد موردنظر سیستم", number,"بود")

    play_again = input("میخوای دوباره بازی کنی؟ (Y/N): ").strip()  # <-- تغییر: دریافت پاسخ کاربر

    if play_again != "y":  # <-- تغییر: اگر پاسخ چیزی غیر از "بله" بود
        print("ممنون که بازی کردی! خداحافظ")  # <-- تغییر: پیام پایان بازی
        break