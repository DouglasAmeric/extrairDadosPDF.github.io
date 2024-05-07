import PyPDF2
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('teste2.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    numeroPGS = len(reader.pages)  
    print(numeroPGS)

    palavraExpecifica = 'assim'
    for numPGS in range(numeroPGS):
        pagina = reader.pages[numPGS]
        texto = pagina.extract_text()  

        if palavraExpecifica in texto:
            word_found = palavraExpecifica
            break

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/extrairDadosPDF/")

input_element = driver.find_element(By.XPATH, "//input[@id='DADO']")
input_element.send_keys(word_found)
time.sleep(3)
print("colocou o valor no input")
driver.find_element(By.XPATH, "//button[@id='enviar']").click()
print("clokou no BTN")

input()
