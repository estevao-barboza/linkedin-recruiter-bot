from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlencode
from selenium.common.exceptions import NoSuchElementException
from credenciais import login,senha


service = Service(r'.\chromedriver.exe')
browser = webdriver.Chrome(service=service)
pagina=1
url = f"https://linkedin.com/search/results/people/?keywords=tech%20recruiter&page={pagina}"
browser.get(url)



input_email = browser.find_element(By.ID,("username"))
input_email.send_keys(login)
input_senha=browser.find_element(By.ID,"password")
input_senha.send_keys(senha)
button_login = browser.find_element(By.XPATH, "//button[@type='submit']")
time.sleep(2)
button_login.click()

time.sleep(10)
# Começa na página 1
pagina = 1

while True:
    url = f"https://linkedin.com/search/results/people/?keywords=tech%20recruiter&page={pagina}"
    browser.get(url)
    time.sleep(5)

    try:
        while True:
            time.sleep(7)
            botao_conectar = browser.find_element(By.XPATH, "//span[text()='Conectar']")
            time.sleep(7)
            botao_conectar.click()
            time.sleep(7)
            botao_enviar_sem_nota = browser.find_element(By.XPATH, "//span[text()='Enviar sem nota']")
            time.sleep(7)
            botao_enviar_sem_nota.click()
            print("Conexão enviada com sucesso.")
            time.sleep(7)
    except NoSuchElementException:
        print(f"Botão 'Conectar' não encontrado na página {pagina}. Indo para a próxima...")
        pagina += 1
        continue
    except Exception as e:
        print(f"Erro inesperado: {e}")
        break



input("")