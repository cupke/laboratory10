if __name__ == "__main__":
    vowels = set("ауоыэяюёиеАУОЫЭЯЮЁИЕ")
    user_input = input("Введите строку: ")

    count = sum(1 for char in user_input if char in vowels)

    print(f"Количество гласных в строке: {count}")
