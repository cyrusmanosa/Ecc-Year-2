import cv2
import numpy as np
from tkinter import Tk, Canvas, PhotoImage, NW
from PIL import Image, ImageTk
import mediapipe as mp
from ctypes import cdll
from copy import deepcopy

# ウィンドウのスタイルを変更する関数
def set_appwindow(root):
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080

    hwnd = cdll.user32.GetParent(root.winfo_id())
    style = cdll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    style = style & ~WS_EX_TOOLWINDOW
    style = style | WS_EX_APPWINDOW
    cdll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    root.wm_withdraw()
    root.after(3000, lambda: root.wm_deiconify())
    # この関数によって、ウィンドウはタスクバーに表示されるようになります

# アプリケーションを終了する関数
def desligar(event):
    global rodando
    rodando = False

# 最後のクリック位置を保存する関数
def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

# ドラッグ中にウィンドウ位置を更新する関数
def Dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))

# 特定の顔の部分の座標を計算する関数
def achar_pontos(pontos_da_parte):
    parte = []
    for point in pontos_da_parte:
        ponto_percentual = face_landmarks.landmark[point]
        y, x, z = frame.shape

        ponto_x = int(x * ponto_percentual.x)  # x座標を計算
        ponto_y = int(y * ponto_percentual.y)  # y座標を計算

        parte.append([ponto_x, ponto_y]) # 座標を部分リストに追加
    return parte
    # この関数は、引数として指定された顔の部分の座標を計算し、それらの座標のリストを返します


# セットアップ
# カメラを開始し、解像度を640x480に設定
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# カメラが正しく開かれていない場合、エラーメッセージを表示して終了
if not cap.isOpened():
    print("nao abriu")
    exit()

# MediaPipeのFace Meshモデルを初期化
face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
face = face_mesh.FaceMesh(static_image_mode=True,
                          max_num_faces=1,
                          refine_landmarks=True,
                          min_detection_confidence=0.5)

# Tkinterウィンドウの作成と設定
root = Tk()
root.title('Jarvis')
root.attributes('-transparent', True)  # 啟用透明背景
# root.wm_attributes('-alpha', 0.8)     # 設置背景透明度（0.0為完全透明，1.0為不透明）
canvas = Canvas(root, width=800, height=600)
canvas.pack()

sem_borda = True
if sem_borda:
    root.overrideredirect(True)  # タイトルバーを削除
    root.after(500, lambda: set_appwindow(root)) # タスクバーにアイコンを表示

# マウスイベントのバインディング
root.bind('<Button-3>', SaveLastClickPos)  # 右クリック位置を保存
root.bind('<B3-Motion>', Dragging)         # 右クリックドラッグでウィンドウを移動
root.bind("<ButtonRelease-2>", desligar)   # 中クリックで終了

# 初期画像を設定（黒い背景）
image_init = np.zeros((800, 600, 3), np.uint8)
image_init_tk = ImageTk.PhotoImage(image=Image.fromarray(image_init))
pose_container = canvas.create_image(0, 0, anchor=NW, image=image_init_tk) # キャンバスに画像を配置

windowName = "Imagem Mil Grau" # ウィンドウ名の設定（使用されていない可能性があります）

# グローバル変数の初期化
rodando = True  # メインループを制御
lastClickX = 0 # 最後のクリック位置を保存
lastClickY = 0

# カメラから画像を取得して処理を行い、結果を表示するためのメインループ
while rodando:
    ret, original_frame = cap.read()  # カメラからフレームを読み取る
    frame = deepcopy(original_frame)  # 元のフレームをコピー

    if not ret:
        print("nao tem frame")  # エラーメッセージを表示して終了
        break

    # フレームの処理と結果の表示に関するコード
    frame_shape = frame.shape
    image = np.zeros((frame_shape[0], frame_shape[1], 3), np.uint8)  # 処理用の画像を作成

    results = face.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))  # 顔のランドマークを検出


    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # 下唇のランドマークインデックス
            mouth_points_1 = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291]

            # 上唇のランドマークインデックス
            mouth_points_2 = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]

            # 内側の下唇のランドマークインデックス
            mouth_points_3 = [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308]

            # 内側の上唇のランドマークインデックス
            mouth_points_4 = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308]

            # 左目の虹彩のランドマークインデックス
            iris_left = [474, 475, 476, 477]

            # 右目の虹彩のランドマークインデックス
            iris_right = [469, 470, 471, 472]

            # 鼻の一部のランドマークインデックス
            nose_points_1 = [168, 6, 197, 195, 5, 4, 1, 19, 94, 2]
            nose_points_2 = [98, 97, 2, 326, 327, 294, 278, 344, 440, 275, 4, 45, 220, 115, 48, 64, 98]

            # 顔の外側の輪郭のランドマークインデックス
            face_oval_points = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288,
                         397, 365, 379, 378, 400, 377, 152, 148, 176, 149,
                         150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54,
                         103, 67, 109, 10]

            boca_points = mouth_points_1 + mouth_points_2[::-1]  # 口のランドマークを結合（下唇 + 上唇の逆順）
            boca_points_up = mouth_points_2 + mouth_points_4[::-1]  # 上側の口のランドマークを結合（上唇 + 内側の上唇の逆順）
            boca_points_down = mouth_points_1 + mouth_points_3[::-1]  # 下側の口のランドマークを結合（下唇 + 内側の下唇の逆順）
            iris_points_left = iris_left  # 左目の虹彩のランドマーク

            boca = achar_pontos(boca_points)  # 口の座標を取得
            boca_u = achar_pontos(boca_points_up)  # 上側の口の座標を取得
            boca_d = achar_pontos(boca_points_down)  # 下側の口の座標を取得
            iris_l = achar_pontos(iris_left)  # 左目の虹彩の座標を取得
            iris_r = achar_pontos(iris_right)  # 右目の虹彩の座標を取得
            nose1 = achar_pontos(nose_points_1)  # 鼻の一部の座標を取得
            nose2 = achar_pontos(nose_points_2)  # 鼻の他の部分の座標を取得
            face_oval = achar_pontos(face_oval_points)  # 顔の外側の輪郭の座標を取得

            # boca_pointsに基づいて顔の口の部分に点を描画
            for point in boca_points:
                ponto_percentual = face_landmarks.landmark[point]
                y, x, z = frame.shape

                ponto_x = int(x * ponto_percentual.x)
                ponto_y = int(y * ponto_percentual.y)

                # 描画する座標に変換（ここでは使用されていないためコメントアウト）
                #boca.append([ponto_x, ponto_y])

                frame = cv2.circle(frame, (ponto_x, ponto_y), 1, (255, 0, 0), 3)  # 口の点を描画

            # 全顔を描画するかどうかのオプション
            rosto_todo = True
            if rosto_todo:
                # 顔のランドマークと輪郭を描画
                mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=face_mesh.FACEMESH_TESSELATION,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style(),
                landmark_drawing_spec=None)

                mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=face_mesh.FACEMESH_CONTOURS,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style(),
                    landmark_drawing_spec=None)

            # 各特徴を異なる色で描画
            cv2.fillPoly(image, pts=np.array([face_oval]), color=(255, 255, 255)) # 顔の外郭
            cv2.fillPoly(image, pts=np.array([boca]), color=(255, 0, 0)) # 口
            cv2.fillPoly(image, pts=np.array([boca_d]), color=(0, 255, 0)) # 下側の口
            cv2.fillPoly(image, pts=np.array([boca_u]), color=(0, 255, 0)) # 上側の口
            cv2.fillPoly(image, pts=np.array([iris_l]), color=(255, 255, 0)) # 左目の虹彩
            cv2.fillPoly(image, pts=np.array([iris_r]), color=(255, 255, 0)) # 右目の虹彩
            cv2.fillPoly(image, pts=np.array([nose1]), color=(0, 0, 255)) # 鼻の一部（BGRカラー）
            cv2.fillPoly(image, pts=np.array([nose2]), color=(0, 0, 255)) # 鼻の他の部分（BGRカラー）


    # 透明度の処理
    tmp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(tmp, 0, 125, cv2.THRESH_BINARY)
    b, g, r = cv2.split(image)
    image_transparency = cv2.merge([b, g, r, alpha], 4)  # 透明度を含む画像を作成
    image_transparency_tk = ImageTk.PhotoImage(image=Image.fromarray(image_transparency))
    canvas.itemconfig(pose_container, image=image_transparency_tk)
    root.update()  # GUIを更新

    aumento = 1.4
    image = cv2.resize(image, (int(frame_shape[1] * aumento), int(frame_shape[0] * aumento)))  # 画像をリサイズ

    # ウィンドウに画像を表示
    cv2.imshow('MediaPipe FaceMesh', original_frame)
    # 'q'キーでループから抜ける
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
print("Encerrou")
