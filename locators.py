from selenium.webdriver.common.by import By

class NanoSanityLocators:
    """Class containing all locators used in the Nano Sanity application"""
    
    # Login Page Locators
    LOGIN_TEXT = (By.XPATH, "//p[contains(text(),'Use your Microsoft account to securely sign in and')]")
    LOGIN_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]")
    CONTINUE_BUTTON = (By.XPATH, "//button[@type='button']")
    EMAIL_INPUT = (By.XPATH, "(//input[@id='i0116'])[1]")
    NEXT_BUTTON_EMAIL = (By.XPATH, "(//input[@id='idSIButton9'])[1]")
    USE_PASSWORD_LINK = (By.XPATH, "//span[@role='button' and normalize-space()='Use your password']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='passwordEntry']")
    NEXT_BUTTON_PASSWORD = (By.XPATH, "//button[normalize-space()='Next']")
    NO_BUTTON = (By.XPATH, "//button[normalize-space()='No']")
    
    # Home Page Locators
    HOME_PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Commercial Loan Portfolio']")
    START_NEW_DEAL_BUTTON = (By.XPATH, "//button[normalize-space()='Start New Deal']")
    
    # Upload Document Locators
    UPLOAD_LOAN_FORM = (By.XPATH, "//div[normalize-space()='Upload a Loan Application Form']")
    START_NEW_DEAL_ALT = (By.XPATH, "//button[normalize-space()='Start a new deal']")
    SVG_SUBMIT = (By.XPATH, "//button[@type='submit']//*[name()='svg']")
    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file'][name='query'][accept='.pdf']")
    
    # Application Review Page Locators
    BASIC_INFORMATION = (By.XPATH, "//h4[normalize-space()='Basic Information']")
    REVIEW_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/button[1]")
    TABLE_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/button[1]")
    SAVE_APPLICATION_BUTTON = (By.XPATH, "//button[normalize-space()='Save Application']")
    NOTE_INPUT = (By.XPATH, "//input[@placeholder='Add a note...']")
    CONFIRM_WITHOUT_NOTE = (By.XPATH, "//button[normalize-space()='Confirm without note']")
    
    # Application Summary Page Locators
    ENTITY_PROFILE_OWNERSHIP = (By.XPATH, "//h3[normalize-space()='Entity Profile & Ownership']")
    APPLICATION_ELEMENT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]")
    BLUE_TEXT_BUTTON = (By.XPATH, "(//div[@class='text-xs font-medium whitespace-nowrap text-blue-700'])[1]")
    UPLOAD_DOCUMENTS_BUTTON = (By.XPATH, "//button[normalize-space()='Upload Documents']")
    FILE_INPUT_UPLOAD = (By.XPATH, "//input[@type='file']")
    UPLOAD_BUTTON = (By.XPATH, "//button[normalize-space()='Upload']")
    VIEW_DOCUMENTS_BUTTON = (By.XPATH, "//button[normalize-space()='View Documents']")
    CONFIRM_DOCUMENTS_BUTTON = (By.XPATH, "//button[normalize-space()='Confirm Documents']")
    
    # Stage Management Locators
    MOVE_STAGE_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]")
    ASSIGN_BUTTON = (By.XPATH, "//button[normalize-space()='Assign']")
    
    # Document Locators
    LIKESIDE_ESTATE_DOC = (By.XPATH, "//div[contains(text(),'Likeside Estate')]")
    GENERATE_SPREADS_HOVER = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/button[4]")
    GENERATE_SPREADS_BUTTON = (By.XPATH, "//button[normalize-space()='Generate Spreads']")
    CONTINUE_BUTTON = (By.XPATH, "//button[normalize-space()='Continue']")
    
    # Financial Spreads Processing Locators
    FINANCIAL_SPREADS_HEADER = (By.XPATH, "//h2[normalize-space()='Financial Spreads Processing']")
    START_PROCESSING_BUTTON = (By.XPATH, "//button[normalize-space()='Start Processing']")
    GLOBAL_SPREAD_BUTTON = (By.XPATH, "//button[normalize-space()='Global Spread']")
    
    # LOI Details Locators
    LOI_HOVER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/button[2]")
    LOI_DETAILS_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]")
    INTERNAL_LOAN_DOCS_BUTTON = (By.XPATH, "//button[normalize-space()='Internal Loan Documents']")
    ENTER_LOI_DETAILS_BUTTON = (By.XPATH, "//button[normalize-space()='Enter LOI Details']")
    LOI_CLOSE_BUTTON = (By.XPATH, "//body[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
    LOAN_COMMITMENT_INPUT = (By.XPATH, "(//input[@placeholder='Enter loan commitment amount'])[1]")
    LOAN_PURPOSE_INPUT = (By.XPATH, "//input[@placeholder='Enter loan purpose or use of funds']")
    MATURITY_DATE_SPAN = (By.XPATH, "//span[normalize-space()='Enter maturity date']")
    DATE_10_BUTTON = (By.XPATH, "//button[normalize-space()='10']")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    INTEREST_RATE_INPUT = (By.XPATH, "//input[@placeholder='Enter interest rate']")
    LOI_SVG_CLOSE = (By.XPATH, "/html[1]/body[1]/div[4]/button[1]/*[name()='svg'][1]")
    LOI_STAGE_MOVE = (By.XPATH, "//body//div//div[@data-panel-group-direction='horizontal']//div//div//div//div//div//div//div//div[2]//button[2]")
    
    # Credit Memo Locators
    CREDIT_MEMO_HOVER = (By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[2]/button[4]")
    CREDIT_MEMO_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]")
    GENERATE_CREDIT_MEMO_BUTTON = (By.XPATH, "//button[normalize-space()='Generate Credit Memo']")
    
    # Additional Miscellaneous Locators (if needed for alternative flows)
    # These are commented out locators from the original script that might be used in future versions
    # SVG_PATH_ELEMENT = (By.XPATH, "//*[name()='path' and contains(@d,'m9 14 2 2 ')]")
    # COMPLEX_BUTTON_CLASS = (By.XPATH, "(//button[@class='inline-flex items-center justify-center cursor-pointer gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 bg-primary text-primary-foreground hover:bg-primary/90 h-10 px-4 py-2'])[1]")