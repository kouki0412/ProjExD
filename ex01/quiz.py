import random
import datetime

def main():
    start_time = datetime.datetime.now()
    Q_number = shutudai()
    kaitou(Q_number)
    end_time = datetime.datetime.now()
    print(f"あなたが解答するのにかかった時間は、{(end_time-start_time).seconds}秒です。")

def shutudai():
    Q_number = random.randint(0,2)
    print(quesions[Q_number])
    return Q_number

def kaitou(Q_number):
    player_input = input()
    if player_input in answers[Q_number]:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    quesions = ["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    answers = [{"ますお","マスオ"},{"わかめ","ワカメ"},{"甥","おい","甥っ子","おいっこ"}]
    main()