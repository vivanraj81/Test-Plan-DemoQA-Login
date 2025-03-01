import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_valid_credentials(driver):
    driver.get("https://demoqa.com/login")
    driver.find_element(By.ID, "userName").send_keys("test_user")
    driver.find_element(By.ID, "password").send_keys("P@ssw0rd123")
    driver.find_element(By.ID, "login").click()
    assert "profile" in driver.current_url

def test_login_invalid_password(driver):
    driver.get("https://demoqa.com/login")
    driver.find_element(By.ID, "userName").send_keys("test_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login").click()
    error = driver.find_element(By.ID, "name")
    assert "Invalid username or password" in error.text