# OpenCVのライブラリをインポートする
import cv2

# 0番目のWebカメラを指定し、カメラキャプチャ用のオブジェクトを作成する
cap = cv2.VideoCapture(1)

# 直前の画像を保持するための変数を初期化する
img_last = None

# 矩形の線の色を定義する (RGB)
green = (0,255,0)

# 無限ループを開始する
while True:
    # Webカメラからフレームを読み込む
    _, frame = cap.read()
    
    # 画像をリサイズする
    frame = cv2.resize(frame, (600,400))
    
    # 画像をグレースケールに変換する
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # 画像にガウシアンフィルタを適用する
    gray = cv2.GaussianBlur(gray,(9,9),0)
    
    # 二値化処理を行い、白黒の画像に変換する
    img_b = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)[1]
    
    # 直前の画像が存在しない場合、直前の画像に現在の画像を代入して、次のループに移行する
    if img_last is None:
        img_last = img_b
        continue
    
    # 直前の画像と現在の画像の差分を計算する
    frame_diff = cv2.absdiff(img_last,img_b)
    
    # 差分画像から輪郭を検出する
    cnts,hierarchy = cv2.findContours(frame_diff,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    # 輪郭の座標を取得し、矩形を描画する
    for pt in cnts:
        x,y,w,h = cv2.boundingRect(pt)
        if w < 50 : continue
        # 矩形の線の色を定義する (RGB)
        cv2.rectangle(frame,(x,y),(x+w , y+h),green, 2)

    # 直前の画像を更新する
    img_last = img_b
    
    # 画像と差分画像を表示する
    cv2.imshow("Diff Camera", frame)
    cv2.imshow("gray Camera", gray)
    cv2.imshow("threshold Camera" , img_b)
    cv2.imshow("diff data" , frame_diff)
    
    
    # Enterキーが押された場合、ループを抜ける
    if cv2.waitKey(1) == 13:break

""" キャプチャの後始末 """
# Webカメラを解放する
cap.release()

# ウィンドウを閉じる
cv2.destroyAllWindows()


