from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

service=Service(ChromeDriverManager().install())
options=webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://e-exam.igdtuw.ac.in/exam/login/index.php")
username=driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/form[1]/div[2]/div/input')
username.send_keys("") #enrollment number


password=driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/form[1]/div[3]/div/input')
password.send_keys("") #passowrd



login_button=driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div/form[1]/div[5]/input')
login_button.click()
# Your code

input("Press Enter to close the browser...")


