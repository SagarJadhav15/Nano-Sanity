from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assumes 'driver' is your active WebDriver instance
wait = WebDriverWait(driver, 30)  # Adjust timeout as needed

# Wait for loader to finish (example: wait for loader to disappear)
try:
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loader")))  # Update selector for your loader
except Exception:
    pass  # Loader may already be gone

# Wait for the button with the SVG path to appear
svg_path_xpath = "//*[name()='path' and contains(@d,'M20 13c0 5')]"
wait.until(EC.presence_of_element_located((By.XPATH, svg_path_xpath)))

# Click the 9th button of type 'button'
ninth_button_xpath = "(//button[@type='button'])[9]"
wait.until(EC.element_to_be_clickable((By.XPATH, ninth_button_xpath))).click()
