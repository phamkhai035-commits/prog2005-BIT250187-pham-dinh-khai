def count_vowels(s):
    vowels = "aeiou"
    count = 0

    for c in s.lower():
        if c in vowels:
            count += 1

    return count

text = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(text))