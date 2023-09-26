import pyautogui
import pandas as pd

def open_chrome_and_access_site(link):
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.write(link)
    pyautogui.press("enter")


def login(email, password):
    pyautogui.write(email)
    pyautogui.press("tab")
    pyautogui.write(password)
    pyautogui.press("enter")


def complete_form(codigo, marca, tipo, categoria, preco_unitario, custo, obs):
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    if not pd.isna(obs):
        pyautogui.write(str(obs))

