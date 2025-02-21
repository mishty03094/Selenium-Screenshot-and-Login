from selenium import webdriver
from PIL import Image
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab
import datetime
import os


def screenshot(save_path):
    screenshot = ImageGrab.grab()

    # Save the screenshot to the specified path
    screenshot.save(save_path)
    print(f"Screenshot saved at {save_path}")

options=webdriver.ChromeOptions()
service=webdriver.ChromeService()
options.add_argument("--start-maximized")
Driver=webdriver.Chrome(service=service, options=options)
Driver.get('https://www.pinterest.com/')

#login_link=Driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[2]/button/div')
#login
login_link=WebDriverWait(Driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/button/div'))
)
login_link.click()


email_box=WebDriverWait(Driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[1]/form/div[2]/div/span/div/input'))
)
email_box.click()
email_box.send_keys("mishtyverma9@gmail.com")


password_box=WebDriverWait(Driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[1]/form/div[4]/div/span/div/input'))
)
password_box.click()
password_box.send_keys("9873314709Mm")

final_login=WebDriverWait(Driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[1]/form/div[7]/button/div'))
)
final_login.click()
to_ss=[]
to_ss.append('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/div/img')
to_ss.append('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/div/img')
to_ss.append('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[3]/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/div/img')
for i in range(len(to_ss)):
    picture1=WebDriverWait(Driver, 10).until(
        EC.presence_of_element_located((By.XPATH, to_ss[i])
                                    )
    )
    picture1.click()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    save_path = os.path.expanduser(f"~/Desktop/screenshot_{timestamp}.png")
    time.sleep(1)


    screenshot(save_path)

    back=WebDriverWait(Driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/button/div/div')
                                    )
    )
    back.click()


input()
