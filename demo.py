from selenium import webdriver


PATH = "C:\\Users\henri\\OneDrive\\Documentos\\Programas\\Python\\WebScraping\\ChromeDrive\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = "https://learn.microsoft.com/pt-br/dotnet/core/get-started"

driver.get(url)
print(driver.title)
driver.quit()