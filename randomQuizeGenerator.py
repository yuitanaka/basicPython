#! python3
#ランダムに問題と答えを並べ問題集と解答を作る

import shelve
import random
import os

def initQuizFilePath():
    if os.path.isdir(quizPathDir) == False:
        os.makedirs(quizPathDir)
    if os.path.isdir(answerPathDir) == False:
        os.makedirs(answerPathDir)

def generateRandomQuiz():
    # TODO: 問題集を読み込む
    shelve_data = shelve.open('/Users/yui/Documents/python/quizData')
    quizData = shelve_data['capitals']

    for quiz_num in range(studentNum):
        quizPath = quizPathDir + 'student' + str(quiz_num + 1) + '.txt'
        answerPath = answerPathDir + 'student' + str(quiz_num + 1) + '.txt'
        try:
            # 問題集と解答集のファイルを作成する
            quizFile = open(quizPath, 'w')
            answerFile = open(answerPath, 'w')
            # 問題集のヘッダーを書く
            quizFile.write('以下の都道府県の県庁所在地を答えよ\n')
            answerFile.write('県庁所在地答え\n')
            # 都道府県の順番をシャッフルする
            temp = list(quizData.keys())
            random.shuffle(temp)
            # 47都道府県をループして、それぞれ問題、解答を作成する
            num = 1;
            for capital in temp:
                quizFile.write(str(num) + ': ' + capital + ' A: ________\n')
                answerFile.write(str(num) + ': ' + capital + ' A: ' + str(quizData[capital]) + '\n')
                num += 1
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            # ファイルを閉じる
            quizFile.close()
            answerFile.close()

studentNum = 35
quizPathDir = '/Users/yui/Documents/python/quizFile/'
answerPathDir = '/Users/yui/Documents/python/answerFile/'
initQuizFilePath()
generateRandomQuiz()
