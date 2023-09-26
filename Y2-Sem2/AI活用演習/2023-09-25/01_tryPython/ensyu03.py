'''
次の入力された文字列(左)に応じて、挨拶(右)を表示する
それ以外の場合は「どうされました？」と表示する
入力は無限に繰り返し行えること

入力された文字          返答
----------------------------------
こんにちは              ようこそ！
景気は                  ぼちぼちです
さようなら              お元気で


【実行結果】
please input data >>こんにちは
ようこそ！
please input data >>景気は
ぼちぼちです
please input data >>さようなら
お元気で
please input data >>ただいま
どうされました？

'''

# 無限ループ
while True:
    data = input("please input data >>")
    if data == "こんにちは" :
        print("ようこそ！")
    elif data == "景気は" :
        print("ぼちぼちです")
    elif data == "さようなら" :
        print("お元気で")
    elif data == "ただいま" :
        print("どうされました？")