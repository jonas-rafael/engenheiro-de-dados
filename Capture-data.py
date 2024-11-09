from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import csv
from time import sleep

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=opts)

driver.get("https://steamdb.info/sales/")
driver.implicitly_wait(3)

def extrair_dados():
    dados = driver.find_elements(By.CLASS_NAME, "app")
    dados_formatados = []

    for dado in dados:
        linhas = dado.text.split("\n")
        dados_formatados.append(linhas)

    return dados_formatados

todos_os_dados = []

todos_os_dados.extend(extrair_dados())

while True:
    try:
        next_button = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[1]/div[2]/div[4]/div/div[3]/div[2]/nav/button[8]").click()
        sleep(3)
        todos_os_dados.extend(extrair_dados())
    except:
        break

with open('dados_steam_organizados.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Descrição", "Preço Baixo", "Preço Atual"])
    for linha in todos_os_dados:
        writer.writerow(linha + [""] * (4 - len(linha)))

print("Dados exportados para 'dados_steam_organizados.csv' com sucesso.")

driver.quit()
