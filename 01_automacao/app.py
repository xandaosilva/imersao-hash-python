import pyautogui
import time
import pandas as pd
from functions import complete_form, open_chrome_and_access_site, login

pyautogui.PAUSE = 0.5

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
open_chrome_and_access_site(link)

time.sleep(3)

pyautogui.click(x = 543, y = 396)

email = "emailteste@email.com"
password = "minhasenhaparateste"
login(email, password)

time.sleep(3)

table = pd.read_csv("produtos.csv")

for i in table.index:
    pyautogui.click(x = 564, y = 280)    
    complete_form(table.loc[i, "codigo"], table.loc[i, "marca"], table.loc[i, "tipo"], table.loc[i, "categoria"], table.loc[i, "preco_unitario"], table.loc[i, "custo"], obs = table.loc[i, "obs"])
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)

