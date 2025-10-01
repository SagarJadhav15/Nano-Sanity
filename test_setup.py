import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("Testing Chrome setup...")

try:
    options = Options()
    options.add_experimental_option("detach", True)
    
    print("Creating Chrome driver...")
    driver = webdriver.Chrome(options=options)
    
    print("Chrome driver created successfully!")
    print("Navigating to test page...")
    
    driver.get("https://www.google.com")
    print("Successfully opened Google!")
    
    time.sleep(3)
    driver.quit()
    print("Test completed successfully!")
    
except Exception as e:
    print(f"Error occurred: {e}")
    print("Please check if Chrome browser and ChromeDriver are properly installed.")