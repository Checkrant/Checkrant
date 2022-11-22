from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Cadastro

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://checkrant.herokuapp.com/")
driver.find_element(By.XPATH,'//input[@id="id_first_name"]').send_keys("test")
driver.find_element(By.XPATH,'//input[@id="id_username"]').send_keys("test")
driver.find_element(By.XPATH,'//input[@id="id_email"]').send_keys("test@test.com")
driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys("test123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
# Login

driver.find_element(By.XPATH,"/html/body/form/a").click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/form/input[2]').send_keys("test")
driver.find_element(By.XPATH,'/html/body/form/input[3]').send_keys("test123")
driver.find_element(By.XPATH,'/html/body/form/button').submit()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/ul/li[1]/a').click()
time.sleep(1)
assert 'test' in driver.page_source


driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/div/button[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="id_writer"]').send_keys("test")
driver.find_element(By.XPATH,'//*[@id="id_stars"]').send_keys("2")
driver.find_element(By.XPATH,'//*[@id="id_detail"]').send_keys("very nice")
driver.find_element(By.XPATH,'/html/body/div[2]/form[1]/button').submit()
time.sleep(2)
driver.back()
driver.back()
driver.back()
time.sleep(2)

driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/ul/li[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="id_nomeRant"]').send_keys("test restaurant")
driver.find_element(By.XPATH,'//*[@id="id_endereco"]').send_keys("test")
driver.find_element(By.XPATH,'//*[@id="id_horarioInicio"]').send_keys("11:00")
driver.find_element(By.XPATH,'//*[@id="id_horarioFinal"]').send_keys("22:00")
driver.find_element(By.XPATH,'//*[@id="id_tipo"]').send_keys("test")
driver.find_element(By.XPATH,'//*[@id="id_email"]').send_keys("test@test.com")
driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys("test123")
driver.find_element(By.XPATH,'//input[@value="Submit"]').click()
time.sleep(2)

driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/ul/li[3]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="id_data"]').send_keys("11/20/2022")
driver.find_element(By.XPATH,'//*[@id="id_content"]').send_keys("test")
driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/input[2]').click()
time.sleep(2)
# Alterar perfil

driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/ul/li[4]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="id_first_name"]').clear()
driver.find_element(By.XPATH,'//*[@id="id_first_name"]').send_keys("test alterado")
driver.find_element(By.XPATH,'//*[@id="id_username"]').clear()
driver.find_element(By.XPATH,'//*[@id="id_username"]').send_keys("test")
driver.find_element(By.XPATH,'//*[@id="id_email"]').clear()
driver.find_element(By.XPATH,'//*[@id="id_email"]').send_keys("test@test.com")
time.sleep(2)
driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/button[1]').click()
assert 'test alterado' in driver.page_source

driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/ul/li[5]/a').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/form[1]/button[1]').click()
driver.find_element(By.XPATH,"//a[normalize-space()='Voltar para home']").click()
driver.find_element(By.XPATH,'/html/body/ul/li[5]/a').click()
time.sleep(1)
assert 'Dislike' in driver.page_source
driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/form[1]/button[1]').click()
driver.find_element(By.XPATH,"//a[normalize-space()='Voltar para home']").click()
driver.find_element(By.XPATH,'/html/body/ul/li[5]/a').click()
time.sleep(1)
driver.back()

driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/ul/li[6]/a').click()
assert 'test restaurant' in driver.page_source
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Favorite").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Voltar para home']").click()
driver.find_element(By.XPATH,'/html[1]/body[1]/ul[1]/li[7]/a[1]').click()
assert 'test restaurant' in driver.page_source
time.sleep(2)
driver.back()
driver.find_element(By.XPATH,'/html[1]/body[1]/a[1]').click()