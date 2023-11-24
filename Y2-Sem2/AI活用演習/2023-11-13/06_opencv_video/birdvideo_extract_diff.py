import cv2
import os

# 前回のフレームを保持する変数
img_last = None

# 保存する画像の枚数を保持する変数
no = 0

# 保存先ディレクトリのパス
save_dir = "./exbird"

# 保存先ディレクトリが存在しなければ作成する
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

# 動画ファイルを読み込むためのVideoCaptureオブジェクトを作成
cap = cv2.VideoCapture("bird.mp4")

# 無限ループでWebカメラからフレームを取得して動画ファイルに書き込む処理を繰り返す
while True:
    # フレームの取得が成功したかどうかのフラグと、取得したフレームの画像を取得
    ret, frame = cap.read()
    
    # フレームの取得に失敗した場合はループを終了する
    if not ret:
        break

    # フレームをリサイズする
    frame = cv2.resize(frame, (640, 360))

    # 画像をグレースケールに変換する
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 画像にガウシアンフィルタを適用する
    gray = cv2.GaussianBlur(gray, (9, 9), 0)
    
    # 二値化処理を行い、白黒の画像に変換する
    img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

    # 前回のフレームが存在する場合、フレーム間差分を計算して鳥の領域を検出する
    if not img_last is None:
        # 2つの画像の差分を計算する
        frame_diff = cv2.absdiff(img_last, img_b)
        # 輪郭を検出する
        cnts = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        
        # 鳥の領域を取り出して保存する
        for pt in cnts:
            x, y, w, h = cv2.boundingRect(pt)
            # 領域が小さすぎる、または大きすぎる場合は無視する
            if w < 30 or w > 300:
                continue
            """ 鳥の領域を切り出して保存する """
            # imgexには、画像中で検出された鳥の領域が含まれています。
            # yからy+h-1までの範囲と、xからx+w-1までの範囲を切り出します。
            imgex = frame[y:y+h, x:x+w]

            # outfile変数に保存するファイル名を設定します。
            outfile = f"{save_dir}/{str(no)}.png"

            # cv2.imwrite関数を使用して画像を保存します。
            cv2.imwrite(outfile, imgex)

            # no変数に1を追加して、次のフレームで使用するファイル名を作成するために使用します。
            no += 1

    # 前回のフレームを更新する
    img_last = img_b
    
# 動画ファイルを解放する
cap.release()

# 処理が終了したことを表示する
print("OK")
