import cv2
import pickle
# scikit-learnライブラリからdatasetsをインポート
import sklearn.datasets  
# matplotlibライブラリからpyplotをインポート
import matplotlib.pyplot as plt

# 手書き数字を予測する関数
def predict_digit(target_filename):
    # digits.pklというファイルからモデルを読み込む
    with open("digits.pkl","rb") as fp: model = pickle.load(fp)
    
    # 画像を読み込んで前処理をする
    target_image = cv2.imread(target_filename)  # 画像を読み込む
    target_image = cv2.cvtColor(target_image,cv2.COLOR_BGR2GRAY)  # グレースケールに変換する
    target_image = cv2.resize(target_image,(8,8))  # サイズを8x8に縮小する
    target_image = 15 - target_image // 16  # 白黒反転して、輝度を0~15の範囲に調整する
    
    print(target_image)  # 変換後の画像を表示する
    target_image = target_image.reshape((-1,64))  # 画像を1次元配列に変換する

    # digitsデータセットをロード
    digits = sklearn.datasets.load_digits()  
    # digitsの画像データの0番目のデータをグレースケールで表示
    plt.imshow(digits.images[0],cmap="gray")
    plt.show()

    # モデルで予測する
    res = model.predict(target_image)
    
    return res[0]   # 予測結果を返す

# ファイル名を指定して数字を予測する
filename = "./Test1.png"
n = predict_digit(filename)
print(f"{filename}は = 数字の{n}ですね！")