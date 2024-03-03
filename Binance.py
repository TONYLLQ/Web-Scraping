from selenium import webdriver
from datetime import datetime
import pandas as pd
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://www.binance.com/es-LA/futures/BTCUSDT")

def scraping_binance(Fecha_Hora):
    list_sales , list_shopping ,list_market_price = [], [], []

    Ejecutando  = True
    
    fecha_final = datetime.strptime(Fecha_Hora, "%Y-%m-%d %H:%M:%S")


    while Ejecutando:
        time.sleep(1)
        sales = driver.find_element(By.XPATH, '//*[@id="futuresOrderbook"]/div[3]/div[1]/div[1]/div/div/div[1]/div/div[1]').text
        shopping = driver.find_element(By.XPATH, '//*[@id="futuresOrderbook"]/div[3]/div[3]/div[1]/div/div/div[1]/div/div[1]').text
        market_price = driver.find_element(By.XPATH, '//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]').text
        list_sales.append(sales)
        list_shopping.append(shopping)
        list_market_price.append(market_price)

        
        fecha_actual = datetime.now()
        print(fecha_actual)

        if fecha_actual >= fecha_final:
            Ejecutando=False




    df = pd.DataFrame({"Sale":list_sales,"Shopping":list_shopping,"Market_price":list_market_price})
    df.to_csv("Binance.csv", index=False , sep=",")

        

scraping_binance("2024-03-03 00:50:59")
driver.quit()

