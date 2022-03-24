import re

def is_strong_password(password):
    # 8文字以上、大文字小文字を1文字以上、１つ以上の数字を使用
    strong_password1 = re.compile(r'[a-z]+')
    strong_password2 = re.compile(r'[A-Z]+')
    strong_password3 = re.compile(r'[0-9]+')
    # スペースが使用されていないか確認
    regex_space = re.compile(r'\s+')
    if len(password) >= 8:
        is_space = regex_space.findall(password)
        if len(is_space) != 0:
            print('パスワードにスペースを含めないでください。')
            return False
        is_strong1 = strong_password1.findall(password)
        is_strong2 = strong_password2.findall(password)
        is_strong3 = strong_password3.findall(password)
        return is_strong1 != [] and is_strong2 != [] and is_strong3 != []
    else:
        return False

while(True):
    print('パスワードを入力してください')
    input_password = input()
    if(is_strong_password(input_password)):
        print('強力なパスワードです。')
        break
    else:
        print('脆弱なパスワードです。パスワードは8文字以上、大文字小文字を1文字以上、１つ以上の数字を使用してください。')
