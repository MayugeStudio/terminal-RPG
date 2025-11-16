import os
import time

TITLE_STR = """
 ███████████          █                               █        
    █    ██           █    █                          ██       
     ████         ██████████         █████       ████████████  
  ███████████         █  ██        ██ ██  ██         ████      
  █   ██   ██         █ ██        █   ██   ██      ██ ██ ██    
  ███████████   ██████████████   ██   ██    █    ███  ██   ██  
  █   ██   ██        ██          █    █     ██   █ █  █   █    
  ███████████       ████████     █    █     ██     █      █    
      █           ███      █     █   ██     █   ██████████████ 
 ████████████   ██ ██      █     █   █     ██     ██     ███   
      █     █      █████████     ██ ██     ██     ████   ███   
     ██     █      ██      █      ███    ███     █ █ ██ █ █ █  
   ███     ██      █████████           ███      ██ █  ██  █  █ 
 ███    ████               █                       █      █    
                                                               
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def sleep(ms: int):
    time.sleep(ms/1000)

def separator():
    print("-" * 50)


def ask_input() -> str:
    return input("# ")


def wait_input() -> None:
    input("> ")

def verify_input(expect: list[int]) -> str:
    choice = ask_input()
    while choice not in expect:
        print("-- 入力が間違っているわ。")
        choice = ask_input()
    return choice

def dev_assertion(function_name: str) -> None:
    """
    開発者用のアサーション関数

    絶対に起きない処理に使ってください。
    """
    print(f"ERROR: Unexpected behavior in {function_name}()")
    exit(1)

def dialogue(prefix: str, message: str) -> None:
    """
    通常速度でダイアログを表示
    """
    print(prefix + " " +message)

def dialogue_slow(prefix: str, message: str) -> None:
    """
    ゆっくりダイアログを表示
    """
    print(prefix + " ", end="")
    for c in message:
        print(c, end="", flush=True)
        sleep(60)
    # 改行
    print()

def home_scene() -> None:
    clear()
    dialogue_slow("--", "ここは村の近くの森よ")
    dialogue_slow("--", "とはいえ、いつ何が襲ってくるかわからないから気を付けて。")
    print()
    wait_input()

    while True:
        clear()
        separator()
        dialogue("--", "どうするか選んで。")
        separator()
        # TODO: [COST]を何かしらのオブジェクトで管理
        print("1. 森の奥へ進む [1日]")
        print("2. 村の方へ引き返す [2日]")
        print("3. 休憩する [1日]")
        separator()
        choice = verify_input(["1", "2", "3"])

        if choice == "1":
            wait_input()
        elif choice == "2":
            dialogue_slow("--", "村に引き返すのね。")
            dialogue_slow("[ナレーション]", "：家に帰って休んだ！")
            wait_input()
        elif choice == "3":
            dialogue("--", "心の底から休んでね。")
            for i in range(3):
                print("", ".")
                sleep(300)
            # TODO: 成功と失敗がほしい
            dialogue_slow("[ナレーション]", "：心の底から休んだ！")
            wait_input()

        else:
            dev_assertion("home_scene")



def battle_scene() -> None:
    pass


def start_game() -> None:
    clear()
    # 名前を聞く
    ask_name = True
    print("-- あなたの名前を教えて。")
    name = ask_input()
    while len(name) == 0:
        print("-- 入力が間違っているわ。")
        name = ask_input()

    dialogue_slow("--", f" こんにちは、{name}")
    dialogue_slow("--", "この村はこのままでは、ドラゴンに襲撃されて皆殺しにあってしまうの。")
    dialogue_slow("--", "皆、ドラゴンのことを邪悪な生物と、恐れているわ。")
    dialogue_slow("--", "あなたの目標はそのドラゴンを倒すことよ。まだ子供だけど、あなたならできるはずよ。")
    dialogue_slow("--", "それじゃあ、よろしくね。")
    wait_input()

    game_play = True
    scene = "home"

    while game_play:
        if scene == "home":
            home_scene()
        elif scene == "battle":
            battle_scene()


def main() -> None:
    clear()

    print(TITLE_STR)

    separator()
    print("1. ゲームを始める")
    print("2. ゲームをやめる")
    separator()

    ok = False
    while not ok:
        choice = ask_input()
        if choice == "1":
            ok = True
        elif choice == "2":
            print("ばいばーい")
            exit(0)
        else:
            print("数字が間違ってるよ。")
            print("もう一度入力してね。")

    # ゲームスタート
    start_game()



if __name__ == "__main__":
    main()
