from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import NanoSanityLocators

class NanoSanityAssertions:
    """Class containing all assertions used in the Nano Sanity application"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def assert_login_page_loaded(self):
        """Assert that the login page is loaded correctly"""
        try:
            login_text_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.LOGIN_TEXT)
            )
            assert "Use your Microsoft account to securely sign in and access your account." in login_text_element.text, "Login page not loaded"
            print("✓ Login page loaded successfully")
            return True
        except (TimeoutException, AssertionError) as e:
            print(f"✗ Login page assertion failed: {e}")
            return False
    
    def assert_home_page_loaded(self):
        """Assert that the home page is loaded correctly"""
        try:
            home_text_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.HOME_PAGE_TITLE)
            )
            assert "Commercial Loan Portfolio" in home_text_element.text, "Home page not loaded"
            print("✓ Home page loaded successfully")
            return True
        except (TimeoutException, AssertionError) as e:
            print(f"✗ Home page assertion failed: {e}")
            return False
    
    def assert_application_review_page_loaded(self):
        """Assert that the application review page is loaded correctly"""
        try:
            application_review_text_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.BASIC_INFORMATION)
            )
            # Note: Original assertion seems incorrect, checking for "Basic Information" instead
            assert "Basic Information" in application_review_text_element.text, "Application Review page not loaded"
            print("✓ Application Review page loaded successfully")
            return True
        except (TimeoutException, AssertionError) as e:
            print(f"✗ Application Review page assertion failed: {e}")
            return False
    
    def assert_application_summary_page_loaded(self):
        """Assert that the application summary page is loaded correctly"""
        try:
            application_summary_text_element = self.wait.until(
                EC.presence_of_element_located(NanoSanityLocators.ENTITY_PROFILE_OWNERSHIP)
            )
            assert "Entity Profile & Ownership" in application_summary_text_element.text, "Application Summary page not loaded"
            print("✓ Application Summary page loaded successfully")
            return True
        except (TimeoutException, AssertionError) as e:
            print(f"✗ Application Summary page assertion failed: {e}")
            return False
    
    def assert_financial_spreads_processing_page_loaded(self):
        """Assert that the Financial Spreads Processing page is loaded correctly"""
        try:
            financial_spreads_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(NanoSanityLocators.FINANCIAL_SPREADS_HEADER)
            )
            assert "Financial Spreads Processing" in financial_spreads_element.text, "Financial Spreads Processing header not found"
            print("✓ Financial Spreads Processing page loaded successfully")
            return True
        except (TimeoutException, AssertionError) as e:
            print(f"✗ Financial Spreads Processing page assertion failed: {e}")
            return False
    
    def assert_global_spread_button_visible(self):
        """Assert that the Global Spread button is present and visible"""
        try:
            global_spread_button = WebDriverWait(self.driver, 200).until(
                EC.presence_of_element_located(NanoSanityLocators.GLOBAL_SPREAD_BUTTON)
            )
            assert global_spread_button.is_displayed(), "Global Spread button not found or not visible"
            print("✓ Global Spread button is visible")
            return True
        except (TimeoutException, AssertionError) as e:
            print(f"✗ Global Spread button assertion failed: {e}")
            return False
    
    def assert_all_pages_in_sequence(self):
        """Run all page assertions in sequence for complete flow validation"""
        results = []
        results.append(("Login Page", self.assert_login_page_loaded()))
        results.append(("Home Page", self.assert_home_page_loaded()))
        results.append(("Application Review Page", self.assert_application_review_page_loaded()))
        results.append(("Application Summary Page", self.assert_application_summary_page_loaded()))
        results.append(("Financial Spreads Processing Page", self.assert_financial_spreads_processing_page_loaded()))
        results.append(("Global Spread Button", self.assert_global_spread_button_visible()))
        
        print("\n=== Assertion Summary ===")
        for page_name, result in results:
            status = "PASSED" if result else "FAILED"
            print(f"{page_name}: {status}")
        
        return all(result for _, result in results)