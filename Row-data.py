





'''

driver.find_element(By.XPATH, "//button[normalize-space()='Start New Deal']").click()
time.sleep(3)


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
driver.implicitly_wait(20)

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file'][name='query'][accept='.pdf']")
driver.execute_script("arguments[0].removeAttribute('disabled')", file_input)
file_input.send_keys(r"C:\Users\denzo\OneDrive\Desktop\Nano Sanity\DAta\Deal10.pdf")

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
    r"C:\Users\denzo\OneDrive\Desktop\Nano Sanity\DAta\ProTemecula2024PL.pdf"
]

files_to_upload = "\n".join(pdf_files)
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
driver.execute_script("arguments[0].style.display = 'block';", file_input)
file_input.send_keys(files_to_upload)

driver.find_element(By.XPATH, "//button[normalize-space()='Upload']").click()
time.sleep(25)
driver.find_element(By.XPATH, "//button[normalize-space()='View Documents']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[normalize-space()='Confirm Documents']").click()
time.sleep(5)

#Move deal to next stage
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]").click()
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//button[normalize-space()='Assign']").click()
driver.implicitly_wait(20)



driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]").click()

#click on prescreeining page
actions = ActionChains(driver)

try:
    application_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]"))
    )
   button_to_click.click()
   

'''