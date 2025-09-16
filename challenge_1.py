'''
Input: "the quick brown fox jumps over the lazy dog"
Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

Input: "hello world hello python world hello"
Output: {'hello': 3, 'world': 2, 'python': 1}
'''

sentence = "the just just just quick brown brown fox umps over the lazy dog"
my_dict = {}
sentence_list = sentence.split()

for item in sentence_list:
    if item not in my_dict:
        my_dict[item] = 1

    else:
        my_dict[item] += 1
print(my_dict)
