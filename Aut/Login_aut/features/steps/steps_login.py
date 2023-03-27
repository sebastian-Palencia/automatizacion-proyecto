
from behave import *

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Aut.supports.Funciones_globales import Funciones_Globales



t = 0.5


def ingresar_credenciales(usuario, clave):
    f.Texto("id", "email", usuario, t)
    f.Texto("id", "password", clave, t)


def obtener_mensaje_error(xpath, error_message):
    for i in range(10):
        e1 = f.selectoxpath(xpath)
        if e1.text == error_message:
            return
        else:
            time.sleep(1)
    f.adjuntar_captura_de_pantalla_a_reporte()
    raise AssertionError("El mensaje de error no coincide")



@given(u'I am on the login page')
def step_impl(context):
    global driver, f
    service = Service(r"C:\Repo\Selenium\Drivers\chromedriver.exe")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=service)#options=chrome_options)
    f =Funciones_Globales(driver)
    f.Navegar("https://yellowpush.b2clogin.com/yellowpush.onmicrosoft.com/b2c_1_signin/oauth2/v2.0/authorize?client_id=87a9c1f5-2d71-4c36-8357-4f25c438d63b&scope=openid%20profile%20offline_access&redirect_uri=http%3A%2F%2Flocalhost%3A3000&client-request-id=8847b488-bc43-4592-9f26-ba05cbdfd3b9&response_mode=fragment&response_type=code&x-client-SKU=msal.js.browser&x-client-VER=2.16.1&x-client-OS=&x-client-CPU=&client_info=1&code_challenge=LxaDiShX-8Wd0KQbB-xDGx8g-2FsVH426bmhEmEr7qc&code_challenge_method=S256&nonce=98d4d9dc-9dcb-4a23-95e9-41b9b9287831&state=eyJpZCI6IjhiYmZiMGY3LWNjZmEtNGFiYS1hYTdhLWMwOTMzOWE3ZjlhZCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D")

@when(u'I enter my valid username and password')
def step_impl(context):
    usuario = context.config.userdata['usuario_registrado']
    clave = context.config.userdata['clave_registrado']
    ingresar_credenciales(usuario,clave)

@then(u'I should see my personal dashboard')
def step_impl(context):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/section/section/header/div/div[1]/div/img")))


@when(u'I enter an invalid username and password')
def step_impl(context):
    usuario = context.config.userdata['usuario_invalido']
    clave = context.config.userdata['clave_invalido']
    ingresar_credenciales(usuario,clave)

@when(u'I click on the login button')
def step_impl(context):
    f.Click("id", "next", t)

@then(u'I should see an error message "Please enter a valid email address." indicating that the credentials are incorrect')
def step_impl(context): 
    error_message = context.config.userdata['error_message1']  
    obtener_mensaje_error("//*[@id='localAccountForm']/div[3]/div[1]/div/p",error_message)
    
@when(u'I enter my valid username and an invalid password')
def step_impl(context):
    usuario = context.config.userdata['usuario_registrado']
    clave = context.config.userdata['clave_invalido']
    ingresar_credenciales(usuario,clave)

@then(u'I should see an error message We can´t seem to find your account indicating that the user account was not found')
def step_impl(context):
    error_message = context.config.userdata['error_message2']  
    obtener_mensaje_error("//*[@id='localAccountForm']/div[2]",error_message)

@then(u'I should see an error message Your password is incorrect indicating that the your password is incorrect')
def step_impl(context):
    error_message = context.config.userdata['error_message3']  
    obtener_mensaje_error("//*[@id='localAccountForm']/div[2]",error_message)
    
@when(u'I enter an invalid username and a valid password')
def step_impl(context):
    usuario = context.config.userdata['usuario_sinregistro']
    clave = context.config.userdata['clave_registrado']
    ingresar_credenciales(usuario,clave)

