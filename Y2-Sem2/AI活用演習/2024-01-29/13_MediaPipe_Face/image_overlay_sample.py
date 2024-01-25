import cv2                  # OpenCVライブラリのインポート
import mediapipe as mp     # MediaPipeライブラリのインポート
import numpy as np         # NumPyライブラリのインポート

# 鼻の上に表示する画像（クラウン等）のパスを定義
overlay_image_path = 'red_nose.png'


# 鼻の上に表示する画像を読み込む（透明度も含め）
original_overlay_image = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)

# MediaPipe Face Meshの初期化
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
    
# カメラのキャプチャを開始し、解像度を設定
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    # カメラから画像を読み込む
    success, face_image = cap.read()
    if not success:
        print("Ignoring empty camera frame.") # 読み込み失敗時のメッセージ
        continue
    
    # 画像をRGB色空間に変換
    face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
    
    # 顔のランドマークを検出
    results = face_mesh.process(face_image_rgb)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # 指定したランドマークの座標を取得する関数を定義
            coords = lambda landmark_id: (int(face_landmarks.landmark[landmark_id].x * face_image.shape[1]), int(face_landmarks.landmark[landmark_id].y * face_image.shape[0]))
            
            # 鼻と両目の座標を取得
            nose = coords(4)
            left_eye = coords(33)
            right_eye = coords(263)
            
            # オーバーレイ画像のサイズを計算
            overlay_width = int(np.linalg.norm(np.array(right_eye) - np.array(left_eye)) / 2)
            overlay_height = int(overlay_width * original_overlay_image.shape[0] / original_overlay_image.shape[1])
            
            # オーバーレイ画像をリサイズ
            overlay_image_resized = cv2.resize(original_overlay_image, (overlay_width, overlay_height))

            # アルファ（透明度）と色情報を抽出
            overlay_alpha = overlay_image_resized[:, :, 3:] / 255.0 # アルファチャンネル（透明度）を抽出し、255で割って0から1の範囲に正規化
            overlay_bgr = overlay_image_resized[:, :, :3]           # BGR色チャンネル（青、緑、赤）を抽出
            
            # オーバーレイ画像の開始と終了座標を計算
            start_x = max(nose[0] - overlay_width // 2, 0)
            start_y = max(nose[1] - overlay_height // 2, 0)
            end_x = min(start_x + overlay_width, face_image.shape[1])
            end_y = min(start_y + overlay_height, face_image.shape[0])
            
            # オーバーレイ画像を元の画像上に合成
            face_image[start_y:end_y, start_x:end_x] = (1.0 - overlay_alpha) * face_image[start_y:end_y, start_x:end_x] + overlay_alpha * overlay_bgr
            
    # 画像を表示
    cv2.imshow('MediaPipe FaceMesh with Overlay', face_image)

    # 'q'キーで終了
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# リソースを解放
cap.release()
cv2.destroyAllWindows()
