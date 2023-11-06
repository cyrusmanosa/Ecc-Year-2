# OpenCVとMatplotlibのインポート
import cv2
import matplotlib.pyplot as plt

# 郵便番号を検出する関数の定義
def detect_postcode(fname):
    
    # 画像の読み込み
    img = cv2.imread(fname)

    # 画像の高さと幅を取得し、1/2と1/3にリサイズ
    h, w = img.shape[:2]
    img = img[0:h//2, w//3:]

    # グレースケール変換、ガウシアンフィルタリング、二値化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # グレースケール変換
    gray = cv2.GaussianBlur(gray, (3, 3), 0)        # ガウシアンフィルタでぼかし処理
    im2 = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)[1]   # 二値化処理

    # 輪郭の検出
    cnts = cv2.findContours(im2,        # 画像
        cv2.RETR_LIST,                  # 全ての輪郭を摘出
        cv2.CHAIN_APPROX_SIMPLE)[0]     # 必要な点だけ摘出

    # 検出された輪郭の中から特定の幅のものを抽出し、座標を取得
    result = []
    for pt in cnts:
        x, y, w, h = cv2.boundingRect(pt)   # 各輪郭のx座標、y座標,横幅,縦幅を取得
        if not(50 < w < 70): continue       # 横幅が50以下または70以上の場合は何もしない
        result.append([x, y, w, h])         # 結果用のリストに輪郭情報を追加

    # 検出された座標をx軸方向にソート
    result = sorted(result, key=lambda x: x[0])

    # ソートされた座標の中から隣り合う座標間の距離が一定以上のものを抽出
    result2 = []    
    lastx = -100
    for x, y, w, h in result:
        if (x - lastx) < 10: continue
        result2.append([x, y, w, h])
        lastx = x

    # 抽出した座標に矩形を描画
    for x, y, w, h in result2:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # 結果を返す
    return result2, img

if __name__ == '__main__':
    # 郵便番号を検出し、画像に矩形を描画した結果を表示
    cnts, img = detect_postcode("./hagaki1.png")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.savefig("detect-postcode.png", dpi=200)
    plt.show()