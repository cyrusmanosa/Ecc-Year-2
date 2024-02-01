import cv2
import mediapipe as mp
import numpy as np
try:
    # 適用する画像のパスを定義
    overlay_image_path_right = 'kirakira_right.png'
    overlay_image_path_left = 'kirakira_left.png'

    # 鼻の上に表示する画像を読み込む（透明度も含め）
    original_overlay_right = cv2.imread(overlay_image_path_right, cv2.IMREAD_UNCHANGED)
    original_overlay_left = cv2.imread(overlay_image_path_left, cv2.IMREAD_UNCHANGED)

    # MediaPipe Face Meshの初期化
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    # カメラのキャプチャを開始し、解像度を設定
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while cap.isOpened():
        success, face_image = cap.read() # カメラから画像を読み込む
        if not success:
            print("Ignoring empty camera frame.") # 読み込み失敗時のメッセージ
            continue

        # 画像をRGB色空間に変換
        face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

        # 顔のランドマークを検出
        results = face_mesh.process(face_image_rgb) 

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # 指定したランドマークの座標を取得する関数
                coords = lambda landmark_id: (int(face_landmarks.landmark[landmark_id].x * face_image.shape[1]), int(face_landmarks.landmark[landmark_id].y * face_image.shape[0]))

                # 左目と右目のランドマーク インデックスを定義(左、上、右、下)
                nose = coords(4)
                left_eye = coords(33)
                right_eye = coords(263)

                # オーバーレイ画像の幅を調整
                overlay_width = int(np.linalg.norm(np.array(right_eye) - np.array(left_eye)) / 2)
                overlay_height = int(overlay_width * original_overlay_right.shape[0] / original_overlay_right.shape[1])

                # それぞれのオーバーレイ画像をリサイズ
                overlay_image_resized_r = cv2.resize(original_overlay_right, (overlay_width, overlay_height))
                overlay_image_resized_l = cv2.resize(original_overlay_left, (overlay_width, overlay_height))

                # アルファ（透明度）と色情報を抽出
                overlay_alpha = overlay_image_resized_r[:, :, 3:] / 255.0 # アルファチャンネル（透明度）を抽出し、255で割って0から1の範囲に正規化
                overlay_bgr = overlay_image_resized_r[:, :, :3]           # BGR色チャンネル（青、緑、赤）を抽出

                
                # オーバーレイ画像の開始と終了座標を計算
                l_start_x = max(left_eye[0] - overlay_width // 2, 0)
                l_start_y = max(left_eye[1] - overlay_height // 2, 0)
                l_end_x = min(l_start_x + overlay_width, face_image.shape[1])
                l_end_y = min(l_start_y + overlay_height, face_image.shape[0])
                
                r_start_x = max(right_eye[0] - overlay_width // 2, 0)
                r_start_y = max(right_eye[1] - overlay_height // 2, 0)
                r_end_x = min(r_start_x + overlay_width, face_image.shape[1])
                r_end_y = min(r_start_y + overlay_height, face_image.shape[0])

                # オーバーレイ画像を元の画像上に合成
                face_image[l_start_y:l_end_y, l_start_x:l_end_x] = (1.0 - overlay_alpha) * face_image[l_start_y:l_end_y, l_start_x:l_end_x] + overlay_alpha * overlay_bgr
                face_image[r_start_y:r_end_y, r_start_x:r_end_x] = (1.0 - overlay_alpha) * face_image[r_start_y:r_end_y, r_start_x:r_end_x] + overlay_alpha * overlay_bgr

        # 画像を表示
        cv2.imshow('MediaPipe FaceMesh with Overlay', face_image)

        # 'q'キーで終了
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"エラーが発生しました: {e}")
finally:
    # リソースを解放
    cap.release()
    cv2.destroyAllWindows()
