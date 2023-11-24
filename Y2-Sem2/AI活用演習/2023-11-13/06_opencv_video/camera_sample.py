import cv2
import numpy as np

# Webカメラを開くためにcapオブジェクトを作成する
cap = cv2.VideoCapture(1)

while True:
    # カメラから1フレームずつ画像を読み込む
    # _は読み込んだ結果がTrueかFalseを返すので、使わない
    _, frame = cap.read()
    
    # 画像サイズを変更する
    frame = cv2.resize(frame,(600,400))
    
    # 画像を表示する
    cv2.imshow('camera',frame)
    
    # キーボードの入力を待つ
    k = cv2.waitKey(1)
    
    # もしESC(27)またはEnter(13)が入力されたら、ループを終了する
    if k == 27 or k == 13 : break

# Webカメラを解放する
cap.release()

# ウィンドウを閉じる
cv2.destroyAllWindows()
