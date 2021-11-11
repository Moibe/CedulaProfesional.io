# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:28:31 2021

@author: Moibe
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:11:02 2021

@author: mak
"""


import requests
from bs4 import BeautifulSoup
import csv
import time
import json
import openpyxl

#------------------------------------------------

OUTPUT_FILE = 'bigFile.csv'

"""
#Haz esto si tu archivo es online.
parametros_url = 'https://masternode.id/json/cedula.js'


res_param = requests.get(parametros_url)
js_param = json.loads(res_param.content)

"""

#Haz esto si tu archivo es local. 
with open('rango.json') as fp:
    js_param = json.load(fp)
    
    
for row in js_param: 
    
    inicio =  row['inicio']  
    fin = row['fin']
   

for i in range(inicio, fin):
    
    url = 'https://cedula.buholegal.com/'+str(i)+'/'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    try:
        name = soup.h3.text
        div = soup.find('div', class_='card-body')
        
        a1 = ''
        a2 = ''
        a3 = ''
        a4 = ''
        b1 = ''
        b2 = ''
        c1 = ''
        c2 = ''
        c3 = ''
        try:
            trs = div.find_all('tr')
            if len(trs) == 0:
                 with open(OUTPUT_FILE,'a',newline='',errors='ignore') as fd:
                    wr = csv.writer(fd, dialect='excel')
                    wr.writerow([i,'Skipped for trs'])
                 continue
        except:
            print(str(i)+': Skipped no read')
            time.sleep(5)
        
            with open(OUTPUT_FILE,'a',newline='',errors='ignore') as fd:
                wr = csv.writer(fd, dialect='excel')
                wr.writerow([i,'Skipped for other'])
                
            continue
        for tr in trs:
            # print(tr.text)
            # print('----')
        
            
            try:
                tr.text.index('Carrera')
                a1 = tr.text.replace('Carrera', '').strip()
            except:
                temp = ''
                
            try:
                tr.text.index('Universidad')
                a2 = tr.text.replace('Universidad', '').strip()
            except:
                temp = ''
            
            try:
                tr.text.index('Estado')
                a3 = tr.text.replace('Estado', '').strip()
            except:
                temp = ''
                
            try:
                tr.text.index('Año')
                a4 = tr.text.replace('Año', '').strip()
            except:
                temp = ''
                
            
            try:
                tr.text.index('Trabajo actual')
                b1 = tr.text.replace('Trabajo actual', '').strip()
            except:
                temp = ''
                
            try:
                tr.text.index('Experiencia')
                b2 = tr.text.replace('Experiencia', '').strip()
            except:
                temp = ''
                
            try:
                tr.text.index('Correo')
                c1 = tr.text.replace('Correo', '').strip()
            except:
                temp = ''
                
            try:
                tr.text.index('Teléfono')
                c2 = tr.text.replace('Teléfono', '').strip()
            except:
                temp = ''
            
        
        print(i)
        print(name)        
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(b1)
        print(b2)
        print(c1)
        print(c2)
        #print(c3)
        
        print('-----')
        
        #Escribe la fila en el excel. 
        with open(OUTPUT_FILE,'a',newline='',errors='ignore') as fd:
            wr = csv.writer(fd, dialect='excel')
            wr.writerow([i,name,a1,a2,a3,a4,b1,b2,c1,c2,c3])
            
       
 
            
        time.sleep(2)
    except:
        print(str(i)+': Skipped No Existe')
        time.sleep(5)
    
        with open(OUTPUT_FILE,'a',newline='',errors='ignore') as fd:
            wr = csv.writer(fd, dialect='excel')
            wr.writerow([i,'Skipped - corte a transmisión'])
            print("Se cortó la transmisión en....")
            print(i)
            time.sleep(50)
            print("Nos faltan otros 40 de descanso...")
            time.sleep(40)
            print("Terminó el descanso.")
            
        continue

print("Esto es el final final.......")
print("Y esto fue el último i: ")
print(i)
   

#Movimientos sobre JS_Param
for row in js_param:
    
    print("Con éste inicio el archivo originalmente: ")
    print(row['inicio'])
    
    inicio_temp = row['inicio']
    
    print("Y éste fue el último archivo que logro imprimir. ")
    print(i)
    time.sleep(100)
    
    #Crearemos el nuevo dataset:
    
    row['inicio'] = i
    row['fin'] = i + 10000
    #Incluso puedes escribir algo nuevo si así lo deseas.
    #row['algo_nuevo'] = 1984
    
    print("Y así queda nuestro nuevo set:")
    print(js_param)
        
    with open('rango.json', 'w', encoding='utf-8') as jsonf: 
        jsonf.write(json.dumps(js_param, indent=0)) 
         
        

    



        