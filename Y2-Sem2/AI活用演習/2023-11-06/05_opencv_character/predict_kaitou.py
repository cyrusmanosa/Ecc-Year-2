# detect_postcode.pyからdetect_postnoをインポート
from detect_kaitou import *
# プロットするためにmatplotlibをインポート
import matplotlib.pyplot as plt
# モデルの読み込み保存の為のライブラリ
import pickle

# 学習済み手書き数字のデータを読み込む
with open("digits.pkl", "rb") as fp:
    model = pickle.load(fp)
# 画像から領域を読み込む
cnts, img = detect_kaitou("./kaitou1.png")

# 回答内容を格納するリスト
ans = []

# 読み込んだデータをプロットするためのforループ
for i, pt in enumerate(cnts):
    # 領域の座標と大きさを取得
    x, y, w, h = pt

    # 画像の枠線の内側のデータを取り出す
    img_cut = img[(y + 8) : (y + h) - 8, (x + 8): (x + w) - 8]
    
    """ データを学習済みデータに合わせる """
    # グレースケールに変換
    img_cut = cv2.cvtColor(img_cut,cv2.COLOR_BGR2GRAY) 
    # リサイズ
    img_cut = cv2.resize(img_cut,(8,8))
    
    # 白黒反転
    img_cut = 15 - img_cut // 16 
    
    # 一次元に変換
    img_cut = img_cut.reshape((-1,64))
    
    # データ予測する
    res = model.predict(img_cut)
    
    # 画面に出力
    plt.show()

    # 回答番号をリストに追加
    ans.append(int(res))

# 予測結果を表示
correct = [1,2,3,4]
score = 0
for i in range(len(ans)):
    if correct[i] == ans[i]: 
        print(f"問{i+1} : 正解")
        score+=25
    else :
        print(f"問{i+1} : 不正解")
print(f"点数は{score}点です")
plt.show()
