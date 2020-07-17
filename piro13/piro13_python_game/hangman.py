import random
from time import sleep as s


def dice(turns):
    return random.randint(1, 6)


print("간단한 행맨 놀이를 해보실래요? 저는 당신이 맞춰야 할 단어 리스트를 가지고 있어요!")
s(1)
print("나머지는 쉬우니까, 그냥 해볼게요!\n")
s(1)

repeat = ""
fruits = [("apple"), ("watermelon"), ("avocado"), ("banana"), ("strawberry"), ("blueberry"), ("Grape"), ("cherry"),
          ("coconut"), ("cranberry"), ("pineapple"), ("mango"), ("peach"), ("grapefruit"), ("melon"), ("kiwi"),
          ("lemon"),
          ("lime"), ("mandarin"), ("pear"), ("orange"), ("papaya"), ("plum"), ("tangerine"), ("durian"),
          ("tomato")]
animals = [("elephant"), ("rhinoceros"), ("squirrel"), ("parrot"), ("dolphin"), ("shell"), ("octopus"), ("chimpanzee"),
           ("crocodile"), ("turtle"), ("kangaroo"), ("otter"), ("hamster"), ("mouse"), ("rabbit"), ("horse"),
           ("turkey"), ("penguin"), ("panda"), ("koala"), ("frog"), ("racoon"), ("giraffe"), ("monkey"), ("sheep"),
           ("rabbit"), ("alligator"), ("gorilla"), ("zebra"), ("gorilla")]
countries = [("Afghanistan"), ("Australia"), ("Austria"), ("Bangladesh"), ("Bhutan"), ("Brazil"), ("Bulgaria"),
             ("Cambodia"), ("Canada"), ("Chile"), ("China"), ("Columbia"), ("Congo"), ("Croatia"), ("Denmark"),
             ("Dominica"), ("Egypt"), ("Ethiopia"), ("Finland"), ("France"),
             ("Germany"), ("Ghana"), ("Greece"), ("Hungary"), ("India"), ("Indonesia"), ("Israel"), ("Italy"),
             ("Jamaica"), ("Japan"), ("Kazakstan"), ("Kenya"), ("Korea"), ("Malaysia"), ("Mexico"), ("Norway"),
             ("Philippines"), ("Poland"), ("Portugal"), ("Russia"),
             ("Singapore"), ("Slovakia"), ("Spain"), ("Taiwan"), ("Tanzania"), ("Thailand"), ("Turkey"), ("Uganda"),
             ("Uzbekistan"), ("Zimbabwe")]
themes = [fruits, animals, countries]

tick = 0
cross = 0



while repeat == "":
    try:
        r = int(
            input("게임에는 선택할 3가지 테마가 있어요. \n과일, 동물, 나라. 각 테마에 대해 각각 0,1,2를 선택해주세요:"))
        choice = themes[r]
    except IndexError:
        print("의욕이 과하시네요.  진정하시고 0에서 2까지만 선택해주세요.")
        repeat = ''
        continue

    i = random.choice(choice)
    word = i
    word = word.lower()
    s(1.5)
    print("\n단어들이 준비되었습니다!")

    n = input("r을 눌러 주사위를 돌려보세요!")

    while (n != "r"):
        n = input("r을 눌러주세요!!!")

    if n == "r":
        turns = int(dice(n))

    print('''
    □ □ □
    □''', end="")

    print("", turns, end="")

    print('''  □
    □ □ □ \n''')

    wrong = 0
    guess = ["-"] * len(word)
    letterss = "abcdefghijklmnopqrstuvwxyz"
    print("어떤 단어인지 눈치 채셨다면 단어 전체를 입력 해 보세요. \n단, 조심하세요! 틀리는 순간 게임은 끝나게 됩니다!")
    while wrong < turns:
        curr = ''
        if (wrong >= 1):
            print("틀린 횟수:", wrong)
            print("틀려도 너무 틀렸군. 다른 문자를 선택해보시게.", end='')
        print("당신은", turns - wrong, "번의 기회가 있습니다. \n추측 가능한 문자를 넣어보세요!")
        let = input(":")
        let = let.lower()
        print(let)
        s(1)
        if len(let) > 1:
            print("보아하니 당신은 그 단어를 추측하기로 결정한 것 같군")
            s(1)
            if let == word:
                print("추측했군!")
                break
            else:
                print("안타깝게도 추측의 기회가 이제 없군!")
                break
        if let.isalpha() == False:
            print("당신의 그 문자는 여기 없는게 확실하군.")
        elif len(let) > 1:
            print("미안하지만 내 게임은 아직 단어 전체를 추측하는 것을 지원하지 않으니 인내심을 가져라.")
        elif len(let) == 0:
            print("뭐 입력도 했어? 그건 정말 경솔한 짓이군.")
        else:
            if (let in word) and (let in letterss):
                print("그래! 그 문자는 있어!")
                letterss = letterss.replace(let, "")
                for count in range(len(word)):
                    if word[count] == let:
                        guess[count] = let
                s(1)
                print("바로 이 문자야!", end='')

                temp = 1
            else:
                print("그 문자는 없어")
                wrong += 1
                print("당신의 추측은 아직이군:", end='')
                temp = 2

            for l in guess:
                curr += l
            print(curr)

            if temp == 1:
                print("그래도 아직 단어 전체를 다 찾지는 못했군요.\n")
            elif temp == 2:
                print("좀 더 분발해보지 그래\n")

            if curr == word:
                print("추측했군!")
                tick += 1
                cross -= 1
                break

    cross += 1
    print("바로 이 단어야!", word)
    repeat = input("ENTER를 누르면 다른 라운드로 이동합니다. 종료를 하려면 다른 걸 치세요.")
print("이용해주셔서 감사합니다!")
s(1)
print("그리고 오 잠깐, 당신이 맞춘 단어와 그렇지 않은 단어들을 알아야 해. 여기 있단다:")
s(0.5)
print("맞춘 단어 개수:", tick)
print("cross 맞추지 못한 단어 개수 :", cross)