# coding: utf-8
# 
# =====================================================
# これは「ス×□ソ」（すばつしかくそ）
# コンソールで遊べる数字当てゲームである。
# 決して「ヌメ〇ン」ではない。ええ、決して。
# =====================================================
#


import random
import math
import re

number_list = [0,1,2,3,4,5,6,7,8,9]
subatsusikakuso = []

NUMBERS = 3

#入力値判定用の正規表現
input_style = r'^[0-9] [0-9] [0-9]$'


#初期化
def init():
    for i in range(NUMBERS):
        _chosen_number = math.floor(random.random()*len(number_list))
        subatsusikakuso.append(number_list[_chosen_number])
        number_list.remove(number_list[_chosen_number])

#あたり判定をする   
def get_result(subatsusikakuso,selected_numbers):
    _eat_count = 0
    _bite_count = 0
    for i in range(NUMBERS):
        _num = int(i)
        #eatを確かめる
        if int(selected_numbers[_num]) == subatsusikakuso[_num]:
            _eat_count += 1
            continue
        #biteを確かめる
        if int(selected_numbers[_num]) in subatsusikakuso:
            _bite_count += 1
            
    return _eat_count, _bite_count
    
#######MAIN#######
#初期化
init()

#loop
while(True):

    #input
    print("[数字 数字 数字]の型で入力してください。")
    print("諦める場合は[exit]と入力してください。")
    call_number = input(">> ")
    
    #諦めたか判定
    if call_number == "exit":
        print("残念でした。")
        break

    #入力値の判定
    isMatched = re.match(input_style,call_number)
    if not isMatched:
        print("型が違います。もう一度入力してください。")
        continue

    #選択した数字を配列で保持
    selected_numbers = call_number.split(" ")

    #あたり判定
    bite_count = 0
    eat_count = 0
    (eat_count, bite_count)= get_result(subatsusikakuso,selected_numbers)
   
    #bite,eat数を表示
    print(str(bite_count) + " bite")
    print(str(eat_count) + " eat")
    
    #正解判定
    if eat_count < NUMBERS:
        continue
    if eat_count == NUMBERS:
        print("正解です！")
        break

#終了
print("答えは" + str(subatsusikakuso) + "でした")
print("お疲れ様でした。")
