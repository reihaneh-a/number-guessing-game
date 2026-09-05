import random

while True:

    digit_len = random.randint(1, 6)
    number = random.randint(1, 9) if digit_len == 1 else random.randint(10 ** (digit_len - 1), 10 ** digit_len - 1)
    print(number)

    print("من یک عدد انتخاب کردم! ")
    print("حدس بزن عدد چیست!")

    attempt = 0

    while attempt < 10:
        guess_input = input("عدد را حدس بزنید:").strip()


        if not guess_input.isdigit():
            print("لطفا فقط عدد انگلیسی وارد کنید!")
            continue

        if len(guess_input)> 6:
            print("حداکثر عدد شش رقمی وارد کنید")
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

        place_names = ["یکان", "دهگان", "صدگان", "هزارگان", "ده‌هزارگان", "صدهزارگان"]

        secret_places = [(number // (10 ** i)) % 10 for i in range(6)]
        guess_places = [(guess // (10 ** i)) % 10 for i in range(6)]

        # guess_digits = set(str(guess))
        guess_digits = set(guess_input.zfill(6))
        correct = 0
        digit_correct = 0


        for i in range(5, -1, -1):
            if positions >= i + 1:
                name = place_names[i]
                if guess_places[i] == secret_places[i]:
                    print(name, "درسته")
                    correct += 1
                elif str(secret_places[i]) in guess_digits:
                    print("عدد", name, "درسته ولی جاش درست نیست")
                else:
                    print("عدد", name, "درست نیست")

        for digit in secret_places:
            if str(digit) in guess_digits:
                digit_correct += 1

        position_percent = (correct / positions) * 100
        print(" درصد درستی جایگاه:", round(position_percent, 2), '%')

        digit_percent = (digit_correct / 6) * 100
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