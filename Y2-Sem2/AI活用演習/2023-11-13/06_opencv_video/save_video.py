import cv2
import numpy as np

# WebカメラをキャプチャするためのVideoCaptureオブジェクトを作成
cap = cv2.VideoCapture(1)

""" フレームを動画ファイルに書き込むためのVideoWriterオブジェクトを作成 """
# fmtは書き込む動画ファイルのコーデックを指定
fmt = cv2.VideoWriter_fourcc('H','2','6','5')

# 書き込む動画のフレームレートを指定
fps = 20.0

# 書き込む動画の解像度を指定
size = (600,385)

# 書き込み用のオブジェクトを生成
writer = cv2.VideoWriter('test.mp4',fmt,fps,size)

# 無限ループでWebカメラからフレームを取得して動画ファイルに書き込む処理を繰り返す
while True:
    # retはフレームの取得が成功したかどうかのフラグ
    # frameには取得したフレームの画像が格納される
    ret, frame = cap.read()
    
    # 取得したフレームをリサイズ
    frame = cv2.resize(frame,size)
    
    # 取得したフレームを動画ファイルに書き込む
    writer.write(frame)
    
    # 取得したフレームを表示する
    cv2.imshow('frame',frame)
    
    # キーボード入力を1ms待って、Enterキーが押されたら無限ループを抜ける
    if cv2.waitKey(1) == 13: # 13はEnterキーのキーコード
        break

# 動画ファイルを書き込み終了する
writer.release()

""" キャプチャの後始末 """
# Webカメラを解放する
cap.release()
# 表示していたウィンドウを閉じる
cv2.destroyAllWindows()

