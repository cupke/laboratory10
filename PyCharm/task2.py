if __name__ == "__main__":
    input_str1 = input("Введите первую строку: ")
    input_str2 = input("Введите вторую строку: ")

    set1 = set(input_str1)
    set2 = set(input_str2)

    common_chars = set1.intersection(set2)

    print(f"Общие символы в двух строках: {common_chars}")
