#앞선 실습 과제에서 vocabulary.txt라는 파일을 만들었죠? 이 파일에는 우리가 암기하고 싶은 단어들이 정리되어 있는데요.
#이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내 주는 프로그램을 만들려고 합니다.
#프로그램은 콘솔에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다.
#사용자가 입력한 영어 단어가 정답이면 "맞았습니다!"라고 출력하고, 틀리면 "아쉽습니다. 정답은 OOO입니다."가 출력되어야 합니다.

with open('new_file2.txt', 'r') as f:

    while True:
        for line in f:
            quiz = line.strip().split(": ")

            answer = input("{}: ".format(quiz[1]))
            if answer == quiz[0]:
                print("맞았습니다!")
            else:
                print("아쉽습니다. 정답은 {}입니다.".format(quiz[0]))







