import pyautogui
from time import sleep
import pyperclip


pyautogui.PAUSE = 2
# attend = input('attend y/n: ')
# google_meet = input('google meet y/n: ')

attend = 'n'
google_meet = 'n'

sleep(5)


subject_type = 'лк'
subject = 'прога'
user = 'kolya'
num = 3  # nure account number at login

links = {'пз бжд': 'https://meet.google.com/twc-yfwc-psq',
         'лк прога': 'https://meet.google.com/yud-txfp-emg',
         'лк вм': 'https://meet.google.com/hjj-jmuu-ovx'}
users = {'kolya': 'mykola.hryshyn%40nure.ua'}

subject_attend = {'лк прога': 'https://dl.nure.ua/mod/attendance/view.php?id=192974',
                  'лк вм': 'https://dl.nure.ua/mod/attendance/view.php?id=192206'}
subject_num = {'бжд': 1}
screenWidth, screenHeight = pyautogui.size()

# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)




# enter to a nure account
if attend == 'y':
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write('https://dl.nure.ua/my/')
    pyautogui.press('enter')
    pyautogui.click(1793, 118)
    pyautogui.click(1192, 686)
    pyautogui.press(['tab' for i in range(num+1)])
    pyautogui.press('enter')


    # attend on dl
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write(subject_attend[subject_type + ' ' + subject])
    pyautogui.click(1850, 484)
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('отправить')
    pyautogui.hotkey('ctrl', 'v')
    color = False
    x = 1612
    y = 601
    while not color:
        color = pyautogui.pixelMatchesColor(x, y, (120, 204, 102))
        y += 2

    pyautogui.click(x, y)


# enter to a google meet
if google_meet == 'y':
    pyautogui.hotkey('ctrl', 't')
    pyautogui.write(links[subject_type + ' ' + subject] + '?authuser=' + users[user])
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'd')
    pyautogui.hotkey('ctrl', 'e')
    pyautogui.press(['tab' for i in range(8)])
    pyautogui.press('enter')
