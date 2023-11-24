import cv2
import os
import glob
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# 画像サイズを指定
image_size = (64,32)

# スクリプトが実行されているディレクトリのパスを取得
path = os.path.dirname(os.path.abspath(__file__))

# "bird"と"nobird"ディレクトリのパスを設定
path_bird = path + '\\bird'
path_nobird = path + '\\nobird'

# 特徴量と正解ラベルを格納するリストを定義
x = []  # 特徴量
y = []  # 正解ラベル

# 指定したディレクトリ内の画像を読み込み、特徴量と正解ラベルをリストに追加する関数
def read_dir(target_path, label):
    # ディレクトリ内の全ての.pngファイルを取得
    files = glob.glob(f"{target_path}/*.png")
    
    # 各ファイルを読み込み、特徴量と正解ラベルをリストに追加
    for f in files:
        # 画像を読み込む
        img = cv2.imread(f)
        
        # 画像サイズを指定したサイズにリサイズする
        img = cv2.resize(img, (64,32))
        
        # 画像を1次元配列に変換する
        img_data = img.reshape(-1,)
        
        # 特徴量をリストに追加する
        x.append(img_data)
        
        # 正解ラベルをリストに追加する
        y.append(label)

# "nobird"ディレクトリ内の画像を読み込み、正解ラベル0としてリストに追加する
read_dir('./nobird', 0)

# "bird"ディレクトリ内の画像を読み込み、正解ラベル1としてリストに追加する
read_dir('./bird', 1)

# 学習用データとテスト用データに分割する
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# サポートベクターマシン(SVM)のSVCモデルを準備

model = SVC()

# 学習データを用いて学習する
model.fit(x_train, y_train)

# テスト用データに対する正解率を計算して表示する
print(model.score(x_test, y_test))

# 学習済みモデルをファイルに保存する
with open("bird.pkl", "wb") as fp:
    pickle.dump(model, fp)
