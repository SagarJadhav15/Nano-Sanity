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
driver.get("https://nano-dev.uptiq.ai/")
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
driver.find_element(By.XPATH, "//span[normalize-space()='666331194941']").click()

driver.implicitly_wait(20)

driver.find_element(By.XPATH, "//div[contains(text(),'Draft')]").click()

time.sleep(3)
driver.implicitly_wait(20)
#clcik on prescreening page
driver.find_element(By.XPATH, "(//div[@class='text-xs font-medium whitespace-nowrap text-blue-700'])[1]").click()


#click on document

driver.find_element(By.XPATH, "//div[contains(text(),'Likeside Estate')]").click()
driver.implicitly_wait(20)

time.sleep(5)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

try:
    application_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@id=':r7:']/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div[2]/div"))
    )
    actions.move_to_element(application_element).perform()
    button_to_click = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Classification Review'])[1]/following::button[1]"))
    )
    button_to_click.click()
except (TimeoutException, NoSuchElementException) as e:
    print(f"Could not hover or click the target button: {e}")

#click on genrate spreads
driver.find_element(By.XPATH, "//button[normalize-space()='Generate Spreads']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "(//button[@class='inline-flex items-center justify-center cursor-pointer gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2'])[1]").click()

driver.implicitly_wait(200)


# assertion for Financial Spreads Processing page
try:
    financial_spreads_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Financial Spreads Processing']"))
    )
    assert "Financial Spreads Processing" in financial_spreads_element.text, "Financial Spreads Processing header not found"
except (TimeoutException, AssertionError):
    print("Financial Spreads Processing header not found or text mismatch!")


#click on start processing
driver.find_element(By.XPATH, "//button[normalize-space()='Start Processing']").click()
driver.implicitly_wait(200)



# assertion for Global Spread button presence
try:
    global_spread_button = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Global Spread']"))
    )
    assert global_spread_button.is_displayed(), "Global Spread button not found or not visible"
except (TimeoutException, AssertionError):
    print("Global Spread button not found or not visible!")


#move stage to LOI 
driver.find_element(By.XPATH, "(//button[@type='button'])[10]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'m9 14 2 2 ')]").click()
driver.implicitly_wait(20)





























