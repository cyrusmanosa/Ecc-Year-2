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

    # 色空間をHSVに変換
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
    
    # HSVを色相(Hue),彩度(Saturation),明度(Value)に分割する 
    h,s,v = hsv[:,:,0]  ,hsv[:,:,1] ,hsv[:,:,2]

    """ 赤色っぽい色を持つ画素だけを抽出し表示 """
    # 空の画像データを生成
    img = np.zeros(h.shape,dtype=np.uint8)
    
    # boolインデックス参照を使用し、条件下の値を255(白)に変更
    img[((h<30)|(150<h)) & (s>80)] = 255
    
    # 抽出したフレームを表示する
    cv2.imshow('RED Camera',img)
    
    # Enterキーが押されたらループを終了する
    if cv2.waitKey(1) == 13 : break

""" キャプチャの後始末 """
# Webカメラを解放する
cap.release()

# ウィンドウを閉じる
cv2.destroyAllWindows()
