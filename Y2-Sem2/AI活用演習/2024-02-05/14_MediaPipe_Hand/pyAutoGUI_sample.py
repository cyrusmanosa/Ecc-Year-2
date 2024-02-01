import pyautogui
import time
from pynput.mouse import Button, Controller

mouse = Controller()

# commandキーを押してスタートメニューを開く
pyautogui.press('command')

# 少し待つ
time.sleep(1)

# 'Paint'と入力
pyautogui.typewrite('Paint')

# 少し待つ
time.sleep(1)


# Enterキーを押してPaintを開く
pyautogui.press('enter')

# Paintが開くまで少し待つ
time.sleep(2)


# キャンバスの上にマウスを移動
pyautogui.moveTo(1200, 600)# PC環境に合わせて変えること


# 渦巻を描く（マウスを動かす）
mt=0.1  # 各ドラッグ操作の移動時間を設定
distance=100  # 渦巻き描画の初期距離
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=mt)  # 右にドラッグ
    distance -= 10  # 渦巻きの距離を減少
    pyautogui.dragRel(0, distance, duration=mt)  # 下にドラッグ
    pyautogui.dragRel(-distance, 0, duration=mt)  # 左にドラッグ
    distance -= 10  # 再度距離を減少
    pyautogui.dragRel(0, -distance, duration=mt)  # 上にドラッグ
    mouse.release(Button.left)  # 釋放滑鼠左鍵
    distance -= 10  # 減少螺旋距離
    


# 画面のスクリーンショットを撮ります
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')
