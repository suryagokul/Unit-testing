from selenium import webdriver

# To get driver for browser 

# Goto https://www.selenium.dev/downloads/ and expand Browsers section then download.

#launching chrome browser

driver = webdriver.Chrome('C:\\Users\\SURYA\\Downloads\\installers\\chromedriver.exe')

# Opening url

driver.get("https://www.youtube.com")


# For Maximizing Window

driver.maximize_window()

# get title of website

print("Website title : ",driver.title)

# get current page url

print("Current page url is : ",driver.current_url)

driver.get("https://www.swarnandhra.ac.in")

print("opened new Website and title is : ",driver.title)

driver.back()

print("After backward Website title : ",driver.title)

# for refreshing the page

driver.refresh()

# getting again previous tab

driver.forward()

print("After forwarding Website title is : ",driver.title)

# close the opened tab not close entire chrome

driver.close()

# closes entire chrome and all tabs

driver.quit()
