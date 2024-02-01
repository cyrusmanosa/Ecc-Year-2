import cv2
from mtcnn.mtcnn import MTCNN
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# MTCNNの顔検出器を作成
detector = MTCNN()

# モデルのロード
model = load_model('./mask_model.keras') # 保存されたモデルのパスを指定

# カメラのキャプチャ開始
cap = cv2.VideoCapture(1)

while True:
    # カメラからフレームを読み込む
    ret, frame = cap.read()

    # 顔を検出
    faces = detector.detect_faces(frame)
    for face in faces:
        color = (200,50,255) 
        x,y,w,h= face['box']
        face_img = frame[y:y + h,x:x + w]
        r = 4
        # モデルの入力サイズに合わせて画像をリサイズ
        resized_face = cv2.resize(face_img,(224,224))
        resized_face = np.expand_dims(resized_face,axis=0)
        
        # 予測
        predictions = model.predict(resized_face)
        predicted_class = np.argmax(predictions)

        # 顔周りに四角を描画
        cv2.rectangle(frame,(x, y),(x+w, y+h),color,2)

        # 予測ラベルを描画
        # label = 'mask'
        cv2.putText(frame, 'mask', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # 画像を表示
    cv2.imshow('Face Mask Detection', frame)

    # 'q'キーが押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
