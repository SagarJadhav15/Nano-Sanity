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

driver.find_element(By.XPATH, "//button[normalize-space()='Start New Deal']").click()
time.sleep(3)

#upload Document
wait = WebDriverWait(driver, 10)

try:
    upload_loan_form = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Upload a Loan Application Form']"))
    )
    upload_loan_form.click()
except TimeoutException:
        try:
            start_new_deal = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Start a new deal']"))
            )
            start_new_deal.click()
            svg_submit = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']//*[name()='svg']"))
            )
            svg_submit.click()
        except TimeoutException:
            print("Alternate flow elements not found!")

driver.find_element(By.XPATH, "//div[normalize-space()='Upload a Loan Application Form']").click()
driver.implicitly_wait(60)

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file'][name='query'][accept='.pdf']")
driver.execute_script("arguments[0].removeAttribute('disabled')", file_input)
file_input.send_keys(r"C:\Users\denzo\OneDrive\Documents\Lakeside\Lakeside Estate App .pdf")

driver.find_element(By.XPATH, "//button[@type='submit']//*[name()='svg']").click()
driver.implicitly_wait(100)

#assertion for application review page
try:
    application_review_text_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h4[normalize-space()='Basic Information']") )
    )
    assert "Application Review" in application_review_text_element.text, "Application Review page not loaded"
except (TimeoutException, AssertionError):
    print("Application Review page not loaded or text not found!")  
    driver.implicitly_wait(20)

driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/button[1]").click()
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/button[1]").click()

driver.find_element(By.XPATH, "//button[normalize-space()='Save Application']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//input[@placeholder='Add a note...']").send_keys("Confirm Extraction")
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Confirm without note']").click()

#assertion for application summary page
try:
    application_summary_text_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Entity Profile & Ownership']") ) 
    )   
    assert "Entity Profile & Ownership" in application_summary_text_element.text, "Application Summary page not loaded"
except (TimeoutException, AssertionError):
    print("Application Summary page not loaded or text not found!") 
driver.implicitly_wait(20)


actions = ActionChains(driver)

try:
    application_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]"))
    )
    actions.move_to_element(application_element).perform()
    button_to_click = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='text-xs font-medium whitespace-nowrap text-blue-700'])[1]"))
    )
    button_to_click.click()
except TimeoutException:
    print("Could not hover or click the target button!")

driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Upload Documents']").click()
driver.implicitly_wait(10)
time.sleep(3)

pdf_files = [
    r"C:\Users\denzo\OneDrive\Documents\Lakeside\Lakeside 2024 P&L- Flagstar- Final.xlsx"
]

files_to_upload = "\n".join(pdf_files)
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
driver.execute_script("arguments[0].style.display = 'block';", file_input)
file_input.send_keys(files_to_upload)

driver.find_element(By.XPATH, "//button[normalize-space()='Upload']").click()
time.sleep(70)
driver.find_element(By.XPATH, "//button[normalize-space()='View Documents']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Documents']").click()
time.sleep(5)

#Move deal to next stage
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()
driver.implicitly_wait(20)

time.sleep(5)
#clickon prescreeining page
driver.find_element(By.XPATH, "(//div[@class='text-xs font-medium whitespace-nowrap text-blue-700'])[1]").click()
driver.implicitly_wait(20)



#click on document

driver.find_element(By.XPATH, "//div[contains(text(),'Likeside Estate')]").click()
driver.implicitly_wait(20)
driver.refresh()

driver.find_element(By.XPATH, "//div[contains(text(),'Likeside Estate')]").click()
time.sleep(10)
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

#click on genrate spreads
driver.find_element(By.XPATH, "//button[normalize-space()='Generate Spreads']").click()
driver.implicitly_wait(20)

#clcik on continue
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
driver.implicitly_wait(200)
#driver.find_element(By.XPATH, "(//button[@class='inline-flex items-center justify-center cursor-pointer gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2'])[1]").click()


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
time.sleep(20)



# assertion for Global Spread button presence
try:
    global_spread_button = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Global Spread']"))
    )
    assert global_spread_button.is_displayed(), "Global Spread button not found or not visible"
except (TimeoutException, AssertionError):
    print("Global Spread button not found or not visible!")


#move stage to LOI 
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()
driver.implicitly_wait(20)
#driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'m9 14 2 2 ')]").click()
#driver.implicitly_wait(20)


#move stage to LOI 
#driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]").click()
#driver.implicitly_wait(20)
#driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()
#driver.implicitly_wait(20)
#driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]").click()
#driver.implicitly_wait(20)


#click on LOI details
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)

try:
    application_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//div[@class='text-xs font-medium whitespace-nowrap text-blue-700'])[1]"))
    )
    actions.move_to_element(application_element).perform()
    button_to_click = wait.until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]"))
    )
    button_to_click.click()
except (TimeoutException, NoSuchElementException) as e:
    print(f"Could not hover or click the target button: {e}")
driver.implicitly_wait(20)

driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Internal Loan Documents']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Enter LOI Details']").click()

time.sleep(3)
driver.find_element(By.XPATH, "//body[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "(//input[@placeholder='Enter loan commitment amount'])[1]").send_keys("30000")
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//input[@placeholder='Enter loan purpose or use of funds']").send_keys("Business Expansion")
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//span[normalize-space()='Enter maturity date']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='10']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//input[@placeholder='Enter interest rate']").send_keys("5")
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/button[1]/*[name()='svg'][1]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//body//div//div[@data-panel-group-direction='horizontal']//div//div//div//div//div//div//div//div[2]//button[2]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()


driver.implicitly_wait(20)

#Credit memo

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