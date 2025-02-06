from selenium import webdriver

from selenium.webdriver.common.by import By



# Initialize WebDriver

driver = webdriver.Chrome() 



# Navigate to the webpage

driver.get("https://gyanibrocricketchannel.github.io/astro/")



# Switch to the iframe using its ID

iframe_element = driver.find_element(By.ID, "myIframe") 

driver.switch_to.frame(iframe_element)  



# Interact with elements inside the iframe

input_field = driver.find_element(By.NAME, "username") 

input_field.send_keys("your_username") 



# Switch back to the main page

driver.switch_to.default_content() 
