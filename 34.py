# def count_vowels(word):
#     vowels = 'aeiouyаеёиоуыэюя'
#     return len([x for x in word.lower() if x in vowels])

# def check_rhythm(poem):
#     lines = poem.split()
#     syllables = []
#     for line in lines:
#         words = line.split('-')
#         count = 0
#         for word in words:
#             count += count_vowels(word)
#             print(count)
#         syllables.append(count)
#     return all(x == syllables[0] for x in syllables)

# poem = input('Введите стихотворение в кавычках:')
# if check_rhythm(poem):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

def cntgls(word,count):
    glas = "аеёиоуэюяы"
    for ch in word:
       if ch in glas:
          count += 1
    return count
stih = input('Введите стихотворение в кавычках:')
stih = stih.split()
count = 0
for fraz in stih:
    # print(fraz)
    if "-" in fraz:
        for word in fraz.split("-"):
            # print(word)
            count = cntgls(word,count)
            # print(count)
    else:
        count = cntgls(fraz,count)
        # print(count)
# print(count)
if count%2 == 0:
    print("Парам пам-пам")
else:
    print("Пам парам")