#automação de navegadores
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# analisar ou separar texto como HTML e, executar ações nele
from bs4 import BeautifulSoup


#Manipular tempo
import time

#Permite exportar os dados que coletamos em um arquivo CSV
import pandas as pd


#Instalar gerenciador de driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# URL dos Exoplanetas da NASA
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"


# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
    bright_star_table = soup.find("table")
            


