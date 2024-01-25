import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# mediapipeのハンド検出モデルをロードします
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 画像の入力としてウェブカメラを使用します
cap = cv2.VideoCapture(1)

# MediaPipe Handsのインスタンスを生成します
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    # カメラの読み込み
    while cap.isOpened():
        success, image = cap.read()
        
        # カメラからの入力がない場合は処理をスキップします
        if not success:
            print("カメラフレームが空です。スキップします。")
            continue
    
        # ウェブカメラはデフォルトでBGRで画像を出力するので、RGBに変換します
        # また、画像が左右反転しているので、flip関数で正しい向きに戻します
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # 元の画像を変更しないように、flags.writeableをFalseに設定します
        image.flags.writeable = False
        
        # 手の検出を行います
        results = hands.process(image)
        
        # 画像を変更可能な状態に戻します
        image.flags.writeable = True
        
        # 手のランドマーク描画のため、BGRに変換します
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        

        # 手のランドマークが検出された場合
        if results.multi_hand_landmarks:
            # 検出された各手について
            for hand_landmarks in results.multi_hand_landmarks:
                # 手のランドマークとその接続線を描画します
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # 人差し指の先端の座標を取得します
                index_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
                index_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

                # スクリーンのサイズを取得します
                screen_width, screen_height = pyautogui.size()
                
                # 正規化された座標をスクリーンの座標に変換します
                x_screen = screen_width * index_x
                y_screen = screen_height * index_y

                # マウスカーソルを新しい位置に移動します
                pyautogui.moveTo(x_screen, y_screen)
                


        # 画像を表示します
        cv2.imshow('MediaPipe Hands', image)
        
        # qキーが押された場合、処理を終了します
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        
        

# カメラリソースを解放します
cap.release()
