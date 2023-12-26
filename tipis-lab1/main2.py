import random
import math

sum_ = 0
russian_alphabet_dists = {}

russian_alphabet = ['Т', 'а', 'к', 'ж', 'е', ' ', 'в', 'ы', 'с', 'о', 'ч', 'т', 'п', 'з', 'и', 'ц', 'н', 'х', 'л', 'д', 'й', 'р', 'я', 'м', 'у', 'ю', 'ш', 'э', 'С', 'ь', 'И', 'г', 'щ', 'б', 'ъ', 'П', 'Б', 'ф', 'К']

for elem1 in russian_alphabet:
    russian_alphabet_dists[elem1] = {}
    for elem2 in russian_alphabet:
        weight = math.ceil(random.random() * 10)
        russian_alphabet_dists[elem1][elem2] = weight
        sum_ += weight

for elem1 in russian_alphabet:
    for elem2 in russian_alphabet:
        russian_alphabet_dists[elem1][elem2] /= sum_

def entropy_func(p: float) -> float:
    return 0 if p == 0 else -p * math.log2(p)

entropy = 0
for elem1 in russian_alphabet:
    rad = russian_alphabet_dists[elem1]
    p1 = sum(rad[elem2] for elem2 in russian_alphabet)
    entropy1 = sum(entropy_func(rad[elem2] / p1) for elem2 in russian_alphabet)
    entropy += p1 * entropy1

print(entropy)
