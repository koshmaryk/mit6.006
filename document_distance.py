import math


# Time complexity: O(N + N)
# Space complexity: O(N)
def count_frequency(word_list):
    freq_dict = dict()
    for word in word_list:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    return freq_dict


# Inner product between two vectors, where vectors are represented as dictionaries of (word, freq) pairs.
def inner_product(document_1, document_2):
    sum = 0.0
    for key in document_1:
        if key in document_2:
            sum += document_1[key] * document_2[key]

    return sum


# The "distance" between two vectors is the angle between them.
# If x = (x1, x2, ..., xn) is the first vector (xi = freq of word i) and y = (y1, y2, ..., yn) is the second vector,
# then the angle between them is defined as d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y)))
# where inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn and norm(x) = sqrt(inner_product(x,x))
def vector_angle(document_1, document_2):
    numerator = inner_product(document_1, document_2)
    denominator = math.sqrt(inner_product(document_1, document_1) * inner_product(document_2, document_2))
    return math.acos(numerator / denominator)


# (D1 * D2) / (|D1| * |D2|)
word_list_1 = 'The fox is in the hat'.split()
word_list_2 = 'The fox is outside'.split()

document_1 = count_frequency(word_list_1)
document_2 = count_frequency(word_list_2)
print(vector_angle(document_1, document_2))
