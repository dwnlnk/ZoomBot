import os, schedule, time, pyautogui

for i in range(3):
    os.chdir("..")

def openZoom():
    os.chdir("AppData/Roaming/Zoom/bin") #enter the path of zoom.exe
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 500)
    time.sleep(0.5)
    pyautogui.typewrite('*********') #enter the call "code"
    pyautogui.moveTo(950, 700)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1000, 800)
    pyautogui.click()
    time.sleep(3)
    pyautogui.keyDown('altleft')
    pyautogui.press('h')
    pyautogui.keyUp('altleft')
    time.sleep(0.5)
    pyautogui.moveTo(1800, 900)
    pyautogui.typewrite("Jordan's ZoomBot: Good day! Jordan will be here shortly. Thank you for your patience!") #enter your name
    time.sleep(1)
    pyautogui.press('enter')

schedule.every().day.at("08:00").do(openZoom) #enter what time you want it to start
#schedule.every(0.5).minutes.do(openZoom)

while True:
    schedule.run_pending()
    time.sleep(1)
