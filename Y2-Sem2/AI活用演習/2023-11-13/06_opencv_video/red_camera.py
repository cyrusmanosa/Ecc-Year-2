# OpenCVのcv2モジュールとnumpyをインポート
import cv2
import numpy as np

# カメラをキャプチャする
cap = cv2.VideoCapture(1)

# カメラからフレームを読み込む
_,frame = cap.read()

# 無限ループで続ける
while True:
    # カメラからフレームを読み込む
    _,frame = cap.read()
    # フレームのサイズを変更する
    frame = cv2.resize(frame,(600,400))
    # フレームの青色要素を0にする
    frame[:,:,0] = 0
    # フレームの緑色要素を0にする
    frame[:,:,1] = 0
    # フレームを表示する
    cv2.imshow('RED Camera',frame)
    # Enterキーが押されたらループを終了する
    if cv2.waitKey(1) == 13 : break

""" キャプチャの後始末 """
# Webカメラを解放する
cap.release()

# ウィンドウを閉じる
cv2.destroyAllWindows()
