import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# Import our custom classes
from locators import NanoSanityLocators
from assertions import NanoSanityAssertions

class NanoSanityTestRunner:
    """Main test runner class for Nano Sanity application"""
    
    def __init__(self):
        self.driver = None
        self.wait = None
        self.assertions = None
        self.setup_driver()
    
    def setup_driver(self):
        """Initialize the Chrome driver with options"""
        options = Options()
        options.add_experimental_option("detach", True)  # Keep browser open
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://nano-demo.uptiq.ai/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        self.wait = WebDriverWait(self.driver, 10)
        self.assertions = NanoSanityAssertions(self.driver)
    
    def login_process(self):
        """Handle the complete login process"""
        print("Starting login process...")
        
        # Assert login page is loaded
        self.assertions.assert_login_page_loaded()
        
        # Click login button
        self.driver.find_element(*NanoSanityLocators.LOGIN_BUTTON).click()
        self.driver.find_element(*NanoSanityLocators.CONTINUE_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        # Enter email
        self.driver.find_element(*NanoSanityLocators.EMAIL_INPUT).send_keys("nanobancrm1@gmail.com")
        self.driver.find_element(*NanoSanityLocators.NEXT_BUTTON_EMAIL).click()
        self.driver.implicitly_wait(20)
        
        # Handle password entry
        password = "Password@nano123"
        try:
            use_password_link = self.driver.find_element(*NanoSanityLocators.USE_PASSWORD_LINK)
            use_password_link.click()
            time.sleep(1)
            self.driver.find_element(*NanoSanityLocators.PASSWORD_INPUT).send_keys(password)
        except NoSuchElementException:
            self.driver.find_element(*NanoSanityLocators.PASSWORD_INPUT).send_keys(password)
        
        self.driver.find_element(*NanoSanityLocators.NEXT_BUTTON_PASSWORD).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*NanoSanityLocators.NO_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        print("Login process completed")
    
    def home_page_process(self):
        """Handle home page interactions"""
        print("Processing home page...")
        
        # Assert home page is loaded
        self.assertions.assert_home_page_loaded()
        
        # Start new deal
        self.driver.find_element(*NanoSanityLocators.START_NEW_DEAL_BUTTON).click()
        time.sleep(3)
        
        print("Home page process completed")
    
    def upload_document_process(self):
        """Handle document upload process"""
        print("Starting document upload process...")
        
        try:
            upload_loan_form = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.UPLOAD_LOAN_FORM)
            )
            upload_loan_form.click()
        except TimeoutException:
            try:
                start_new_deal = self.wait.until(
                    EC.element_to_be_clickable(NanoSanityLocators.START_NEW_DEAL_ALT)
                )
                start_new_deal.click()
                svg_submit = self.wait.until(
                    EC.element_to_be_clickable(NanoSanityLocators.SVG_SUBMIT)
                )
                svg_submit.click()
            except TimeoutException:
                print("Alternate flow elements not found!")
        
        self.driver.find_element(*NanoSanityLocators.UPLOAD_LOAN_FORM).click()
        self.driver.implicitly_wait(60)
        
        # Upload file
        file_input = self.driver.find_element(*NanoSanityLocators.FILE_INPUT)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", file_input)
        file_input.send_keys(r"C:\Users\denzo\OneDrive\Documents\Lakeside\Lakeside Estate App .pdf")
        
        self.driver.find_element(*NanoSanityLocators.SVG_SUBMIT).click()
        self.driver.implicitly_wait(100)
        
        print("Document upload process completed")
    
    def application_review_process(self):
        """Handle application review process"""
        print("Processing application review...")
        
        # Assert application review page is loaded
        self.assertions.assert_application_review_page_loaded()
        
        self.driver.find_element(*NanoSanityLocators.REVIEW_BUTTON).click()
        self.driver.find_element(*NanoSanityLocators.TABLE_BUTTON).click()
        self.driver.find_element(*NanoSanityLocators.SAVE_APPLICATION_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        self.driver.find_element(*NanoSanityLocators.NOTE_INPUT).send_keys("Confirm Extraction")
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.CONFIRM_WITHOUT_NOTE).click()
        
        print("Application review process completed")
    
    def application_summary_process(self):
        """Handle application summary and document upload"""
        print("Processing application summary...")
        
        # Assert application summary page is loaded
        self.assertions.assert_application_summary_page_loaded()
        
        actions = ActionChains(self.driver)
        
        try:
            application_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.APPLICATION_ELEMENT)
            )
            actions.move_to_element(application_element).perform()
            button_to_click = self.wait.until(
                EC.element_to_be_clickable(NanoSanityLocators.BLUE_TEXT_BUTTON)
            )
            button_to_click.click()
        except TimeoutException:
            print("Could not hover or click the target button!")
        
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.UPLOAD_DOCUMENTS_BUTTON).click()
        self.driver.implicitly_wait(10)
        time.sleep(3)
        
        # Upload additional documents
        pdf_files = [
            r"C:\Users\denzo\OneDrive\Documents\Lakeside\Lakeside 2024 P&L- Flagstar- Final.xlsx"
        ]
        
        files_to_upload = "\n".join(pdf_files)
        file_input = self.driver.find_element(*NanoSanityLocators.FILE_INPUT_UPLOAD)
        self.driver.execute_script("arguments[0].style.display = 'block';", file_input)
        file_input.send_keys(files_to_upload)
        
        self.driver.find_element(*NanoSanityLocators.UPLOAD_BUTTON).click()
        time.sleep(70)
        self.driver.find_element(*NanoSanityLocators.VIEW_DOCUMENTS_BUTTON).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*NanoSanityLocators.CONFIRM_DOCUMENTS_BUTTON).click()
        time.sleep(5)
        
        # Move deal to next stage
        self.driver.find_element(*NanoSanityLocators.MOVE_STAGE_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.ASSIGN_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        print("Application summary process completed")
    
    def prescreening_process(self):
        """Handle prescreening process"""
        print("Processing prescreening...")
        
        time.sleep(5)
        # Click on prescreening page
        self.driver.find_element(*NanoSanityLocators.BLUE_TEXT_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        # Click on document
        self.driver.find_element(*NanoSanityLocators.LIKESIDE_ESTATE_DOC).click()
        self.driver.implicitly_wait(20)
        self.driver.refresh()
        
        self.driver.find_element(*NanoSanityLocators.LIKESIDE_ESTATE_DOC).click()
        time.sleep(10)
        
        actions = ActionChains(self.driver)
        
        try:
            application_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.BLUE_TEXT_BUTTON)
            )
            actions.move_to_element(application_element).perform()
            button_to_click = self.wait.until(
                EC.element_to_be_clickable(NanoSanityLocators.GENERATE_SPREADS_HOVER)
            )
            button_to_click.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Could not hover or click the target button: {e}")
        
        self.driver.implicitly_wait(20)
        
        print("Prescreening process completed")
    
    def financial_spreads_process(self):
        """Handle financial spreads generation and processing"""
        print("Processing financial spreads...")
        
        # Click on generate spreads
        self.driver.find_element(*NanoSanityLocators.GENERATE_SPREADS_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        # Click on continue
        self.driver.find_element(*NanoSanityLocators.CONTINUE_BUTTON).click()
        self.driver.implicitly_wait(200)
        
        # Assert Financial Spreads Processing page
        self.assertions.assert_financial_spreads_processing_page_loaded()
        
        # Click on start processing
        self.driver.find_element(*NanoSanityLocators.START_PROCESSING_BUTTON).click()
        time.sleep(20)
        
        # Assert Global Spread button presence
        self.assertions.assert_global_spread_button_visible()
        
        print("Financial spreads process completed")
    
    def loi_process(self):
        """Handle Letter of Intent (LOI) process"""
        print("Processing LOI...")
        
        # Move stage to LOI
        self.driver.find_element(*NanoSanityLocators.MOVE_STAGE_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.ASSIGN_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        # Click on LOI details
        actions = ActionChains(self.driver)
        
        try:
            application_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.BLUE_TEXT_BUTTON)
            )
            actions.move_to_element(application_element).perform()
            button_to_click = self.wait.until(
                EC.element_to_be_clickable(NanoSanityLocators.LOI_HOVER_BUTTON)
            )
            button_to_click.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Could not hover or click the target button: {e}")
        
        self.driver.implicitly_wait(20)
        
        self.driver.find_element(*NanoSanityLocators.LOI_DETAILS_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.INTERNAL_LOAN_DOCS_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.ENTER_LOI_DETAILS_BUTTON).click()
        
        time.sleep(3)
        self.driver.find_element(*NanoSanityLocators.LOI_CLOSE_BUTTON).click()
        time.sleep(3)
        
        # Fill LOI details
        self.driver.find_element(*NanoSanityLocators.LOAN_COMMITMENT_INPUT).send_keys("30000")
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.LOAN_PURPOSE_INPUT).send_keys("Business Expansion")
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.MATURITY_DATE_SPAN).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.DATE_10_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.SAVE_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.INTEREST_RATE_INPUT).send_keys("5")
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.SAVE_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.LOI_SVG_CLOSE).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.LOI_STAGE_MOVE).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.ASSIGN_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        print("LOI process completed")
    
    def credit_memo_process(self):
        """Handle credit memo generation"""
        print("Processing credit memo...")
        
        actions = ActionChains(self.driver)
        
        try:
            application_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.BLUE_TEXT_BUTTON)
            )
            actions.move_to_element(application_element).perform()
            button_to_click = self.wait.until(
                EC.element_to_be_clickable(NanoSanityLocators.CREDIT_MEMO_HOVER)
            )
            button_to_click.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Could not hover or click the target button: {e}")
        
        self.driver.implicitly_wait(20)
        
        # Click credit memo
        self.driver.find_element(*NanoSanityLocators.CREDIT_MEMO_BUTTON).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(*NanoSanityLocators.GENERATE_CREDIT_MEMO_BUTTON).click()
        self.driver.implicitly_wait(20)
        
        time.sleep(5)
        print("Credit memo process completed")
    
    def run_complete_test(self):
        """Run the complete test suite"""
        print("=" * 50)
        print("Starting Nano Sanity Complete Test Suite")
        print("=" * 50)
        
        try:
            self.login_process()
            self.home_page_process()
            self.upload_document_process()
            self.application_review_process()
            self.application_summary_process()
            self.prescreening_process()
            self.financial_spreads_process()
            self.loi_process()
            self.credit_memo_process()
            
            print("=" * 50)
            print("✓ Complete test suite executed successfully!")
            print("=" * 50)
            
        except Exception as e:
            print(f"✗ Test suite failed with error: {e}")
            print("=" * 50)
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            self.driver.quit()

# Main execution
if __name__ == "__main__":
    test_runner = NanoSanityTestRunner()
    try:
        test_runner.run_complete_test()
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    finally:
        # Comment out the cleanup if you want to keep the browser open
        # test_runner.cleanup()
        pass