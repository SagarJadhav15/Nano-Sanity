import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_experimental_option("detach", True)  # Keep browser open
driver = webdriver.Chrome(options=options)
driver.get("https://nano-demo.uptiq.ai/")
driver.maximize_window()
#login page assertion
try:
    login_text_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Use your Microsoft account to securely sign in and')]")
    ))
    assert "Use your Microsoft account to securely sign in and access your account." in login_text_element.text, "Login page not loaded"
except (TimeoutException, AssertionError):
    print("Login page not loaded or text not found!")

driver.implicitly_wait(50)

driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]").click()
driver.find_element(By.XPATH, "//button[@type='button']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "(//input[@id='i0116'])[1]").send_keys("nanobancrm1@gmail.com")
driver.find_element(By.XPATH, "(//input[@id='idSIButton9'])[1]").click()
driver.implicitly_wait(20)

password = "Password@nano123"

try:
    use_password_link = driver.find_element(By.XPATH, "//span[@role='button' and normalize-space()='Use your password']")
    use_password_link.click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='passwordEntry']").send_keys(password)
except NoSuchElementException:
    driver.find_element(By.XPATH, "//input[@id='passwordEntry']").send_keys(password)

driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[normalize-space()='No']").click()
driver.implicitly_wait(20)

#home page assertion
try:
    home_text_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Commercial Loan Portfolio']") )
    )
    assert "Commercial Loan Portfolio" in home_text_element.text, "Home page not loaded"
except (TimeoutException, AssertionError):
    print("Home page not loaded or text not found!")
driver.implicitly_wait(20)  


#click on Deal


driver.find_element(By.XPATH, "//p[normalize-space()='Applications']").click()
driver.implicitly_wait(20)

#select Deal
driver.find_element(By.XPATH, "//span[normalize-space()='316917766324']").click()

driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//div[contains(text(),'Draft')]").click()
'''
time.sleep(3)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

try:
    application_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='text-xs font-medium whitespace-nowrap text-blue-700'])[1]"))
    )
    actions.move_to_element(application_element).perform()
    button_to_click = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/button[4]"))
    )
    button_to_click.click()
except (TimeoutException, NoSuchElementException) as e:
    print(f"Could not hover or click the target button: {e}")
driver.implicitly_wait(20)



#move stage to LOI 
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]").click()
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()
driver.implicitly_wait(20)
'''
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

try:
    application_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='text-xs font-medium whitespace-nowrap text-blue-700'])[1]"))
    )
    actions.move_to_element(application_element).perform()
    button_to_click = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/button[4]"))
    )
    button_to_click.click()
except (TimeoutException, NoSuchElementException) as e:
    print(f"Could not hover or click the target button: {e}")
driver.implicitly_wait(20)



#click credit memo
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Generate Credit Memo']").click()
driver.implicitly_wait(20)

time.sleep(5)


