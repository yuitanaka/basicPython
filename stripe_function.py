import re

def stripe_function(string, delete_str):
    if(delete_str == ''):
        #入力された文字列の前後の空白を削除
        regex_before = re.compile(r'^\s')
        regex_end = re.compile(r'\s$')
    else:
        #入力された文字列からdelete_strで指定された単語を削除
        regex_before = re.compile(r'^' + delete_str)
        regex_end = re.compile(delete_str + r'$')
    deleted_str = regex_before.sub(r'', string)
    deleted_str = regex_end.sub(r'', deleted_str)
    return deleted_str
print('指定した文字列の前後の空白/文字を削除します。文字列を入力してください')
input_text = input()
print('削除したい文字を入力してください。ない場合は空白を削除します。Enterを押してください')
input_delete_text = input()
print('X' + stripe_function(input_text, input_delete_text) + 'X')
