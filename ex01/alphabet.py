import random
import datetime

t_number = 0
d_number = 0
counter = 5

def main():
    global t_number,d_number,counter
    start_time = datetime.datetime.now()
    t_number = random.randint(2,26)
    d_number = random.randint(1,t_number-1)
    while(counter>0):
        counter -= 1
        result = game()
        if result:
            print("おめでとうございます！全て正解しました！")
            break
        else:
            print("不正解です。初めからやり直してください")
            print("-"*50)
    else:
        print("既定の回数以上間違えたので失敗です")
        print("Game Over")
    end_time = datetime.datetime.now()
    print(f"あなたがゲームをするのにかかった時間は、{(end_time-start_time).seconds}秒です。")

def game():
    alphabets = [chr(i+ord('A')) for i in range(26)]
    random.shuffle(alphabets)
    target = alphabets[:t_number]
    random.shuffle(target)
    question = target[:d_number]
    defect = target[d_number:]
    random.shuffle(target)
    print("対象文字")
    print(target)
    print("表示文字")
    print(question)
    user_input = int(input("欠損文字は何文字でしょうか？"))
    if user_input == t_number - d_number:
        print("正解です。それでは具体的に何が欠損したかを教えてください。")
        correct_number = 0
        for i in range(1,user_input+1):
            input_chr = input(f"{i}文字目を入力してください:")
            if input_chr in defect:
                correct_number += 1
                del defect[defect.index(input_chr)]
        if correct_number == user_input:
            return True

if __name__ == "__main__":
    main()