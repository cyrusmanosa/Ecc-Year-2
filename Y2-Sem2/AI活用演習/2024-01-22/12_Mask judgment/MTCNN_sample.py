from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
import cv2

# 画像ファイルのパス（マスクをしている画像やしていない画像などを指定）
# image_path = "wear_mask_sample.png"
image_path = "no_mask_sample.png"

# MTCNNの顔検出モデルを初期化する
detector = MTCNN()

# 指定したパスから画像を読み込む
image = cv2.imread(image_path)

# OpenCVはBGR形式で画像を読み込むので、matplotlibで表示するためにRGB形式に変換する
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 顔を検出する（位置、目、鼻などの情報が含まれる）
faces = detector.detect_faces(image)

# 検出された各顔に対して、顔を囲む矩形と目・鼻の位置に円を描画する
for face in faces:
    label = "face"  # 表示するテキスト
    color = (200,50,255) 
    bounding_box = face['box'] # 顔を囲む矩形の位置とサイズ
    x,y,w,h= face['box'] # 顔を囲む矩形の位置とサイズ
    keypoints = face['keypoints'] # 目、鼻などの特徴点
    r = 4

    # cv2.rectangle関数を使用して画像上に矩形を描画します。
    # (x, y)は矩形の左上の座標、(x+w, y+h)は矩形の右下の座標です。
    # colorは矩形の色（RGB形式）で、2は矩形の線の太さです。
    cv2.rectangle(image,(x, y),(x+w, y+h),color,2)


    # 同様に、cv2.circle関数を使用して、特徴点の位置（目、鼻など）に円を描画します。
    # 各特徴点に対して、座標はkeypointsディクショナリから取得します。
    # ここでも、colorは円の色（RGB形式）で、2は円の半径です。
    cv2.circle(image,(keypoints['left_eye']), r, color, r)  # 左目
    cv2.circle(image,(keypoints['right_eye']), r, color, r)  # 右目
    cv2.circle(image,(keypoints['nose']), r, color, r)  # 鼻
    cv2.circle(image,(keypoints['mouth_left']), r, color, r)  # 口の左端
    cv2.circle(image,(keypoints['mouth_right']), r, color, r)  # 口の右端



    # cv2.putText関数を使用して画像上にテキスト（文字列）を描画します。
    # "label"は描画する文字列、(x, y - 10)はテキストの開始位置（左下隅）です。
    # cv2.FONT_HERSHEY_SIMPLEXは使用するフォントの種類、0.9はテキストのサイズ（スケール）です。
    # "color"はテキストの色（RGB形式）で、2はテキストの線の太さです。
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, r)
    
# 画像を表示する（軸は非表示）
plt.imshow(image)
plt.axis('off')
plt.show()

# 顔部分だけ切り取って画像を表示する（軸は非表示）
face_img = image[y:y + h, x:x + w]
plt.imshow(face_img)
plt.axis('off')
plt.show()