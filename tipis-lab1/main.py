import math

text = """Также как высокое качество позиционных исследований напрямую зависит от переосмысления внешнеэкономических 
политик. Сложно сказать, почему сторонники тоталитаризма в науке призваны к ответу. Имеется спорная точка зрения, 
гласящая примерно следующее: ключевые особенности структуры проекта неоднозначны и будут объединены в целые кластеры 
себе подобных. Сложно сказать, почему активно развивающиеся страны третьего мира, вне зависимости от их уровня, 
должны быть обнародованы. Принимая во внимание показатели успешности, социально-экономическое развитие способствует 
подготовке и реализации анализа существующих паттернов поведения. Банальные, но неопровержимые выводы, а также явные 
признаки победы институционализации неоднозначны и будут преданы социально-демократической анафеме. Каждый из нас 
понимает очевидную вещь: высокое качество позиционных исследований способствует повышению качества укрепления 
моральных ценностей."""

counter = 0


def count_log(x):
    return x * (math.log(x) / math.log(2))


def find_shennon(freq):
    return -sum(count_log(p) for p in freq.values())


def get_alphabet(text):
    global counter
    alphabet = {}
    for current in text:
        if current.isalpha() or current == " ":
            counter += 1
            alphabet[current] = alphabet.get(current, 0) + 1

    return alphabet


def get_frequency():
    alphabet = get_alphabet(text)
    frequency = {}
    for key, value in alphabet.items():
        frequency[key] = value / counter
    return frequency


if __name__ == "__main__":
    freq = get_frequency()

    i = 0
    for key, value in freq.items():
        i += 1
        print(f"{key}={value}", end="   ")
        if i % 5 == 0:
            print()

    print(f"\nDictionary: {freq.keys()}")
    print(f"Dictionary size:  {len(freq.keys())}")
    print(f"Text size:  {len(text)}")
    print(f"Volume of one symbol: {find_shennon(freq)}")

