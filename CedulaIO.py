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

OUTPUT_FILE = '3000Results.csv'

for i in range(6267473, 6267573):
    
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
                    wr.writerow([i,'Skipped'])
                 continue
        except:
            print(str(i)+': Skipped')
            time.sleep(5)
        
            with open(OUTPUT_FILE,'a',newline='',errors='ignore') as fd:
                wr = csv.writer(fd, dialect='excel')
                wr.writerow([i,'Skipped'])
                
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
                
            try:
                tr.text.index('Página web')
                c3 = tr.text.replace('Página web', '').strip()
            except:
                temp = ''
                
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        print(b1)
        print(b2)
        print(c1)
        print(c2)
        print(c3)
        print(i)
        print('-----')
        
        with open(OUTPUT_FILE,'a',newline='',errors='ignore') as fd:
            wr = csv.writer(fd, dialect='excel')
            wr.writerow([i,name,a1,a2,a3,a4,b1,b2,c1,c2,c3])
            
        time.sleep(2)
    except:
        print(str(i)+': Skipped')
        time.sleep(5)
    
        with open(OUTPUT_FILE,'a',newline='',errors='ignore') as fd:
            wr = csv.writer(fd, dialect='excel')
            wr.writerow([i,'Skipped'])
            
        continue
