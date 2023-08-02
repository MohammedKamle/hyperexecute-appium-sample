import traceback
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import time

caps = {
    "lt:options": {
        "w3c": True,
        "platformName": "Android",
        "allowInvisibleElements": True,
        "waitForQuiescence": True,
        "isRealMobile": True,
        "app": "<YOUR_APP_URL>",
        "devicelog": True,
        "build": "Hyperexecute_Appium",
        "visual": False,
        "video": True,
        "autoAcceptAlerts": True,
        "autoGrantPermissions": True,
        "appiumVersion": "latest",
        "idleTimeout": 600,
        "region": "us",
    },
}

username = "<YOUR_USERNAME>"
accessKey =  "<YOUR_ACCESSKEY"

def startingTest():
    driver = webdriver.Remote(
        command_executor="https://" + username + ":" + accessKey + "@mobile-hub.lambdatest.com/wd/hub",
        desired_capabilities=caps
    )
    try:
        print("driver created")
        time.sleep(10)
        for i in range(0, 50):
            driver.page_source
            driver.find_element(By.ID, "com.example.QAapp:id/webpage").click()
            driver.find_element(By.ID, "com.example.QAapp:id/websiteName").send_keys("Hello")
            driver.find_element(By.ID, "websiteName").clear()
            driver.find_element(By.ID, "com.example.QAapp:id/findButton")
            driver.current_context
            var = driver.session_id
            driver.is_keyboard_shown()
            driver.is_locked()
            driver.is_app_installed("com.example.QAapp")
        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


startingTest()