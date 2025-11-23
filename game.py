import os
import time
import random
from .constants import TITLE_STR
from utilities import *

def game() -> None:
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
                    rand = random.randint(1, 2)
                    if rand == 1:
                        scene = "battle"
                    else:
                        dialogue_slow("--", "何かの気配がするわ。")
                        dialogue_slow("--", "気を付けて進みましょう。")

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
                    dev_assertion("home")

        elif scene == "battle":
            battle_scene()


def main() -> None:
    """
    メイン関数 （エントリーポイント）
    """
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
    game()



if __name__ == "__main__":
    main()
