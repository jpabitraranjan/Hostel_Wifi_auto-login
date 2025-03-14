from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://10.20.184.1:2280/cportal/ip/user_login.php?url=http://www.gstatic.com/generate_204")  # Replace with the actual login page URL

driver.find_element(By.ID, "usrname").send_keys(*FILL YOUR USERNAME HERE*)
driver.find_element(By.ID, "newpasswd").send_keys(*FILL YOUR PASSWORD HERE*)

driver.find_element(By.ID, "terms").click()

driver.find_element(By.ID, "update_btn").click()

driver.implicitly_wait(5)

driver.quit()
