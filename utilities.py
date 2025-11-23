def clear():
    """
    画面を削除する
    """
    os.system("cls" if os.name == "nt" else "clear")

def sleep(ms: int):
    """
    プログラムを指定された時間だけ止める
    """
    time.sleep(ms/1000)

def separator():
    """
    区切り文字を表示する
    """
    print("-" * 50)


def ask_input() -> str:
    """
    ユーザから入力を受け取る
    """
    return input("# ")


def wait_input() -> None:
    """
    ユーザの入力を待つ
    """
    input("> ")

def verify_input(expect: list[int]) -> str:
    """
    入力を検証する
    """
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