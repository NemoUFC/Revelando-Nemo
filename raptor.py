import time
from selenium import webdriver
import numpy as np    
import pandas as pd


browser = webdriver.Chrome()

browser.get("https://transparencia.fortaleza.ce.gov.br/index.php/diarias/consultar?cboExercicio=&filtroPorOrgao=null&cboMes=&txtNome=")

rows = browser.find_elements_by_tag_name('tr')

#cells = browser.find_elements_by_tag_name('td')

#print(rows[1].text)

#i=0
#for row in rows:    
#    print('[ 0'+str(i)+' ]'+ row[1].text)
#    i=i+1

    

#cols = [row.text for row in rows]    
cols = [row.text.encode('utf-8') for row in rows]    
    
np.savetxt('desafio.csv', cols, delimiter=',', fmt='%10s')   

#pd.DataFrame(cols2).to_csv('Caminho')

 