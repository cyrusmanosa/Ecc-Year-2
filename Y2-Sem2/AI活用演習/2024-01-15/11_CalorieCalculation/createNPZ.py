# 必要なモジュールをインポートする
import numpy as np            # 数学的な操作や配列を扱うためのモジュール
from PIL import Image         # 画像を操作するためのモジュール
import glob                   # ディレクトリの中のファイル一覧を取得するためのモジュール

# データを保存するファイル名
outfile = "image/photos.npz"
# 取得する最大の画像数
max_photo = 40
# 画像のサイズ（一辺のピクセル数）
photo_size = 128
# 画像データを保持するためのリスト
x = []
# ラベルデータ（何の画像かを表すデータ）を保持するためのリスト
y = []


# 画像を読み込んでリストに追加する関数
def load_images(path, label):
    # 指定したパスの画像ファイル一覧を取得します
    files = glob.glob(f"{path}/*.jpg")

    # 画像を一つずつ処理します
    for i, file_path in enumerate(files):
        # 最大画像数に達したら終了します
        if i >= max_photo:
            break
        img = Image.open(file_path)# 画像を開きます
        img = img.convert("RGB")# 画像をRGB（赤、緑、青）モードに変換します
        img = img.resize((photo_size, photo_size))# 画像のサイズを指定したサイズに変更します
        img_array = np.asarray(img)# 画像をNumPy配列（行列）に変換します

        # 配列とラベルをリストに追加します
        x.append(img_array)
        y.append(label)

# このスクリプトが直接実行された時にmain関数を実行します
if __name__ == '__main__':
    # sushiの画像を読み込み、それらにラベル0を付ける
    load_images("./image/sushi", 0)
    # saladの画像を読み込み、それらにラベル1を付ける
    load_images("./image/salad", 1)
    # saladの画像を読み込み、それらにラベル1を付ける
    load_images("./image/pork", 2)

    # 画像とラベルデータをファイルに保存します
    np.savez(outfile, x=x, y=y)
    print(f"保存しました：{outfile} {len(x)} 枚の画像")