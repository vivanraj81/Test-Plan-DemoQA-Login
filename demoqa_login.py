from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login():
    # Initialize ChromeDriver with the correct path
    chrome_driver_path ="C:\Users\ASUS\Downloads\chromedriver-win64\chromedriver.exe" 
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://demoqa.com/login")
    
    # Find elements
    username = driver.find_element(By.ID, "userName")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login")
    
    # Input credentials
    username.send_keys("test_user")
    password.send_keys("P@ssw0rd123")
    login_btn.click()
    
    # Wait for profile page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/profile")
    )
    assert "profile" in driver.current_url
    
    driver.quit()

if __name__ == "__main__":
    test_valid_login()