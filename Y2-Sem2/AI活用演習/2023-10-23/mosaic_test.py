import matplotlib.pyplot as plt  # matplotlibからpyplotをインポート
import cv2  # OpenCVをインポート
from mosaic import mosaic as mosaic  # 自作のmosaic関数をインポート

img = cv2.imread("./04_opencv_face/cat.png")  # 画像を読み込み
mos = mosaic(img,(150 , 150 , 650 , 450),10)  # mosaic関数を用いてモザイク処理を行う mosaic(画像,(始点x軸 , 始点y軸 , 終点x軸 , 終点y軸))

cv2.imwrite("./04_opencv_face/cat_mosaic.png",mos)  # モザイク処理を施した画像を保存
plt.imshow(cv2.cvtColor(mos,cv2.COLOR_BGR2RGB))  # matplotlibで画像を表示するためにRGBに変換してからimshowで表示
plt.show()  # 表示