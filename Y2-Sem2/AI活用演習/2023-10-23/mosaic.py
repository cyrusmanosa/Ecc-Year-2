import cv2

print(f"実行時の値：__name__={__name__}")

def mosaic(img, rect, size):
    # rect: (x1, y1, x2, y2)
    # rectから矩形領域を切り抜き、サイズを縮小してモザイクをかける
    (x1, y1, x2, y2) = rect
    w = x2 - x1  # 矩形領域の幅
    h = y2 - y1  # 矩形領域の高さ
    i_rect = img[y1:y2, x1:x2]  # 矩形領域を切り抜く

    i_small = cv2.resize(i_rect, (size, size))  # 縮小処理
    i_mos = cv2.resize(i_small, (w, h), interpolation=cv2.INTER_AREA)  # 拡大処理

    # モザイク処理後の画像をコピーし、元の画像に切り抜いた矩形領域を置換する
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2

