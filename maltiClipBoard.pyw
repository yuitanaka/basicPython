#! /usr/bin/env python3
# クリップボードのテキストを保存・復元
# Usage:
# ./maltiClipBoard.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
# ./maltiClipBoard.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# ./maltiClipBoard.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

#コマンドライン引数があるかどうか
if len(sys.argv) == 1:
    print('''以下の引数の指定方法を再度ご確認ください。
        ./maltiClipBoard.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
        ./maltiClipBoard.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
        ./maltiClipBoard.pyw list - 全キーワードをクリップボードにコピー''')
else:
    #クリップボードの内容を保存
    if sys.argv[1] == 'save' and len(sys.argv) == 3:
        mcb_shelf[str(sys.argv[2])] = pyperclip.paste()
        print('保存しました')
    #キーワード一覧の読み込み
    elif sys.argv[1] == 'list':
        keys = list(mcb_shelf)
        printKeys = ''
        for k in keys:
            printKeys += str(k) + '\n'
        pyperclip.copy(printKeys)
        print('キーワード一覧をコピーしました')
    #キーワードの読み込み
    elif len(sys.argv) == 2:
        keys = list(mcb_shelf.keys())
        if sys.argv[1] in keys:
            val = mcb_shelf[str(sys.argv[1])]
            pyperclip.copy(val)
            print('キーワードに紐づいたテキストをコピーしました')
        else:
            print('キーワードがありません')
    else:
        print('''以下の引数の指定方法を再度ご確認ください。
            ./maltiClipBoard.pyw save <keyword> - クリップボードをキーワードに紐づけて保存
            ./maltiClipBoard.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
            ./maltiClipBoard.pyw list - 全キーワードをクリップボードにコピー''')
mcb_shelf.close()
