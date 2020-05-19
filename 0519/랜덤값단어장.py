import random

# 1. 사전 만들어서 key 값과 value 값 추출후 randint
vocab = {}
with open('new_file2.txt', 'r') as f:
    for line in f:
        quiz = line.strip().split(": ")
        korean, english = quiz[1], quiz[0]
        vocab[english] = korean


while True:
    keys = list(vocab.keys())  # 리스트로 만듬
    index = random.randint(0, len(keys) - 1)  # 랜덤한수 만들기
    english = keys[index]
    korean = vocab[english]
    temp = input("{}: ".format(korean))

    if temp == 'q':
        break
    if temp == english:
        print("맞았습니다!")
    else:
        print("틀렸습니다. 정답은 {}입니다.".format(english))