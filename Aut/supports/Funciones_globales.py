import time
import tempfile
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from colorama import  Fore
from selenium.webdriver.support.select import Select
from allure_commons.types import AttachmentType

class Funciones_Globales:

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t


    def Navegar(self, Url):
        self.driver.get(Url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)



    def selectoxpath(self, elemento):
        val = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def selectoid(self, elemento):
        val = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element(By.ID, elemento)
        return val         
                
    def Texto(self, tipo, selector, texto, tiempo):
        selectores = {
            "xpath": self.selectoxpath,
            "id": self.selectoid
        }
        
        selector_method = selectores.get(tipo)
        if selector_method:
            try:
                val = selector_method(selector)
                val.clear()
                val.send_keys(texto)
                print("-----Escribiendo en el campo {} el texto {}".format(selector,texto))
                time.sleep(tiempo)
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)
        else:
            print(Fore.RED+ "-----Tipo de selector no válido: " + tipo + Fore.RESET)


    def Click(self,tipo,selector,tiempo):
        if tipo=="xpath":
            try:
                val= self.selectoxpath(selector)
                val.click()
                print("-----Click en el campo {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)
        elif tipo=="id":
            try:
                val= self.selectoid(selector)
                val.click()
                print("-----Click en el campo {}".format(selector))
                t=time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)

    def Select(self,localizador,selector,Tipo,value,Tiempo):
        if localizador=="xpath":
            try:
                val=self.selectoxpath(selector)
                val=Select(val)
                if(Tipo=="text"):
                    val.select_by_visible_text(value)
                elif(Tipo=="value"):
                        val.select_by_value(value)
                elif(Tipo=="index"):
                            val.select_by_index(value)
                else:
                    print("--------------No esta bien el tipo de valor a seleccionar en el select")
                print("-----Select en el campo {}".format(selector))
                print("-----Select con el valor {}".format(value))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)
        elif localizador=="id":
            try:
                val=self.selectoid()
                val=Select(val)
                if(Tipo=="text"):
                    val.select_by_visible_text(value)
                elif(Tipo=="value"):
                        val.select_by_value(value)
                elif(Tipo=="index"):
                            val.select_by_index(value)
                else:
                    print("--------------No esta bien el tipo de valor a seleccionar en el select")
                print("-----Select en el campo {}".format(selector))
                print("-----Select con el valor {}".format(value))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)


    def Upload(self,localizador,selector,ruta,Tiempo):
        if localizador=="xpath":
            try:
                val=self.selectoxpath(selector)
                val.send_keys(ruta)
                print("-----Se carga la imagen {}".format(ruta))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)
        elif localizador=="id":
            try:
                val=self.selectoid()
                val.send_keys(ruta)
                print("-----Se carga la imagen {}".format(ruta))
                t=time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)

    def Check(self, localizador, selector, tiempo):
        if localizador == "id":
            try:
                val=WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.ID,selector)))
                val=self.driver.execute_script("arguments[0].scrollIntoView()",val)
                val=self.driver.find_element(By.ID,selector)
                print("-----Check en -- {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)

        elif localizador == "xpath":
            try:
                val = WebDriverWait(self.driver,4).until(EC.presence_of_element_located((By.XPATH,selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView()",val)
                val = self.driver.find_element(By.XPATH,selector)
                print("-----Elemento encontrado en -- {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(Fore.RED+ "-----No se encontro el elemento " + selector + Fore.RESET)

    def Check_varios_XPATH(self,tiempo,*args):
            try:
                for n in args:

                    val=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,n)))
                    val=self.driver.execute_script("arguments[0].scrollIntoView()",val)
                    val=self.driver.find_element(By.XPATH,n)
                    val.click()
                    print("-----Check en -- {}".format(n))
                    t=time.sleep(tiempo)
                    return t
            except TimeoutException as ex:
                for n in args:
                    print(Fore.RED + "-----No se encontro el elemento"+ n + Fore.RESET)

    def Existe(self, localizador, selector, tiempo):
        if(localizador=="xpath"):
            try:
                val=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,selector)))
                val=self.driver.execute_script("arguments[0].scrollIntoView()",val)
                val=self.driver.find_element(By.XPATH,selector)
                print("El elemento {} -> Aparecio".format(selector))
                t=time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(Fore.RED + "-----No se encontro el elemento"+ selector + Fore.RESET)
                return "No Existe"
        elif(localizador == "id"):
            try:
                val=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,selector)))
                val=self.driver.execute_script("arguments[0].scrollIntoView()",val)
                val=self.driver.find_element(By.ID,selector)
                print("El elemento {} -> existe".format(selector))
                t=time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(Fore.RED + "-----No se encontro el elemento"+ selector + Fore.RESET)
                return "No existe"
            
    def adjuntar_captura_de_pantalla_a_reporte(self):
             # Archivo temporal para guardar la captura de pantalla
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            self.driver.save_screenshot(temp_file.name)
            screenshot_path = temp_file.name
            
        # Captura de pantalla al reporte de Allure
        allure.attach.file(screenshot_path, name="Captura de pantalla", attachment_type=AttachmentType.PNG)
    

