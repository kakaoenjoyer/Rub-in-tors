from cgitb import text
import os
from tkinter import *
from turtle import width
from bs4 import BeautifulSoup

import requests

import math
import os
import numpy as np


### funkcijas






WEBSITE = 'https://wise.com/gb/currency-converter/rub-to-eur-rate'

source = requests.get(WEBSITE).text

soup = BeautifulSoup(source, 'lxml')

rub = soup.find('span', class_='text-success')

r = rub.text

f = float(r)
b = 0.150*0.065
n = 0.157*0.069
da = os.getcwd()
ua = '\epik.gif'
ga = da+ua



print(ga)



def click():
    x = textentry.get()
    output.delete(0.0,END) 
    y = float(x)


    if textentry1.get() == '0':

           
        
        i = y/f
        i = round(i, 2)
        k = math.trunc(i/5)
        q = math.trunc(i/10)
        w = math.trunc(i/50)
        e = math.trunc(i/100)
        r = math.trunc(i/500)
        t = math.trunc(i/1000)
        u = math.trunc(i/5000)
        p = k*0.137*0.061
        o = q*b 
        a = w*b
        s = e*b
        d = r*b
        l = r*n
        g = u*n
        p = round(p, 3)
        o = round(o, 3)
        a = round(a, 3)
        s = round(s, 3)
        d = round(d, 3)
        l = round(l, 3)
        g = round(g, 3)

        output.insert(END,'tavi rubļi ')
        output.insert(END,i)
        output.insert(END,'\n')

        output.insert(END,'5 rubļu banknošu skaits ')
        output.insert(END,k)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,p)
        output.insert(END,'\n')

        output.insert(END,'10 rubļu banknošu skaits ')
        output.insert(END,q)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,o)
        output.insert(END,'\n')

        output.insert(END,'50 rubļu banknošu skaits ')
        output.insert(END,w)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,a)
        output.insert(END,'\n')

        output.insert(END,'100 rubļu banknošu skaits ')
        output.insert(END,e)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,s)
        output.insert(END,'\n')

        output.insert(END,'500 rubļu banknošu skaits ')
        output.insert(END,r)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,d)
        output.insert(END,'\n')

        output.insert(END,'1000 rubļu banknošu skaits ')
        output.insert(END,t)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,l)
        output.insert(END,'\n')

        output.insert(END,'5000 rubļu banknošu skaits   ')
        output.insert(END,u)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,g)
        output.insert(END,'\n')

   

    
    else: 
        lol = textentry1.get()
        output.delete(0.0,END)
          
        jap = lol
        start = 0
        stop = 5
        if len(lol) > stop :
            lol = lol[0: start:] + lol[stop + 1::]
        ne = lol
        web = 'https://www.exchangerates.org.uk/RUB-EUR-spot-exchange-rates-history-'

        ja = '.html'
        opa = web+ne+ja


        WEBSITE = opa
        source = requests.get(WEBSITE).text
        soup = BeautifulSoup(source, 'lxml')

#tr
        tr = soup.find_all('tr',class_='colone')
        tr1 = soup.find_all('tr',class_='coltwo')
        for td in tr:
            to=td.find_all('td')[1]
            ao=td.find_all('a')
            for io in to:
                yo = io.text    
            for oo in ao:
                lo = oo.text
                mo = yo.replace('₽1 RUB = €','')
                ko = lo.replace('Russian Rouble Euro rate for ','')
                so = ','
                uo = mo+so+ko  
                uo = uo.split(',')
    
            for no in uo:
                if jap in no:
                    length = len(uo)

                    middle_index = length // 2

                    first_half = uo[:middle_index]
                    second_half = uo[middle_index:]

                    nauda = first_half
    #tr1
        for td1 in tr1:
            to1=td1.find_all('td')[1]
            ao1=td1.find_all('a')
            for io1 in to1:
                yo1 = io1.text    
            for oo1 in ao1:
                lo1 = oo1.text
                mo1 = yo1.replace('₽1 RUB = €','')
                ko1 = lo1.replace('Russian Rouble Euro rate for ','')
                so1 = ','
                uo1 = mo1+so1+ko1  
                uo1 = uo1.split(',')
    
            for no1 in uo1:
                if jap in no1:
                    length = len(uo1)

                    middle_index = length // 2

                    first_half = uo1[:middle_index]
                    second_half = uo1[middle_index:]

                    nauda = first_half
         
        nauda = ' '.join(map(str, nauda))
        nauda = float(nauda)
        
        yy = y/nauda

        yy = round(yy, 2)
        kk = math.trunc(yy/5)
        qq = math.trunc(yy/10)
        ww = math.trunc(yy/50)
        ee = math.trunc(yy/100)
        rr = math.trunc(yy/500)
        tt = math.trunc(yy/1000)
        uu = math.trunc(yy/5000)
        pp = round(kk*0.120*0.062, 3)
        oo = round(qq*0.127*0.067, 3)
        aa = round(ww*0.133*0.072, 3)
        ss = round(ee*0.140*0.077, 3)
        dd = round(rr*0.147*0.082, 3)
        ll = round(tt*0.153*0.082, 3)
        gg = round(uu*0.160*0.082, 3)

        output.insert(END,'tavi rubļi ') 
        output.insert(END,yy)
        output.insert(END,' datumā ')
        output.insert(END,jap)
        output.insert(END,' kurss ')
        output.insert(END,nauda)
        output.insert(END,'\n')

        output.insert(END,'5 rubļu banknošu skaits ')
        output.insert(END,kk)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,pp)
        output.insert(END,'\n')

        output.insert(END,'10 rubļu banknošu skaits  ')
        output.insert(END,qq)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,oo)
        output.insert(END,'\n')

        output.insert(END,'50 rubļu banknošu skaits  ')
        output.insert(END,ww)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,aa)
        output.insert(END,'\n')

        output.insert(END,'100 rubļu banknošu skaits ')
        output.insert(END,ee)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,ss)
        output.insert(END,'\n')

        output.insert(END,'500 rubļu banknošu skaits ')
        output.insert(END,rr)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,dd)
        output.insert(END,'\n')

        output.insert(END,'1000 rubļu banknošu skaits ')
        output.insert(END,tt)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,ll)
        output.insert(END,'\n')

        output.insert(END,'5000 rubļu banknošu skaits ')
        output.insert(END,uu)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,gg)
        output.insert(END,'\n') 
        
           
            

    
    

    

    


    





def clic():
    x = textentry.get()
    output.delete(0.0,END) 
    y = float(x)

    if textentry1.get() == '0':
        output.delete(0.0,END)
    

        p = round((y/(0.137*0.061)),2)
        o = round((y/b), 2) 
        a = round((y/b), 2)
        s = round((y/b), 2)
        d = round((y/b), 2)
        l = round((y/n), 2)
        g = round((y/n), 2)

        k = round((p*5*f),2)
        q = round((o*10*f),2)
        w = round((a*50*f),2)
        e = round((s*100*f),2)
        r = round((d*500*f),2)
        t = round((l*1000*f),2)
        u = round((g*5000*f),2)

    



    

        
    #1
        output.insert(END,'šodien ')
        
        output.insert(END,'5 rubļu banknošu skaits ')      
        output.insert(END,p)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,k) 
        output.insert(END,'\n')
        #2
        output.insert(END,'10 rubļu banknošu skaits ')
        output.insert(END,o)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,q)
        output.insert(END,'\n')
        #3
        output.insert(END,'50 rubļu banknošu skaits  ')
        output.insert(END,a)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,w)
        output.insert(END,'\n')
        #4
        output.insert(END,'100 rubļu banknošu skaits  ')
        output.insert(END,s)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,e)
        output.insert(END,'\n')
        #5
        output.insert(END,'500 rubļu banknošu skaits  ')
        output.insert(END,d)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,r)
        output.insert(END,'\n')
        #6
        output.insert(END,'1000 rubļu banknošu skaits  ')
        output.insert(END,l)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,t)
        output.insert(END,'\n')
        #7
        output.insert(END,'5000 rubļu banknošu skaits  ')
        output.insert(END,g)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,u)
        output.insert(END,'\n')
        output.insert(END,'jā tev būs jāgriež nauda')
    else:
        lol = textentry1.get()
        output.delete(0.0,END)
          
        jap = lol
        start = 0
        stop = 5
        if len(lol) > stop :
            lol = lol[0: start:] + lol[stop + 1::]
        ne = lol
        web = 'https://www.exchangerates.org.uk/RUB-EUR-spot-exchange-rates-history-'

        ja = '.html'
        opa = web+ne+ja


        WEBSITE = opa
        source = requests.get(WEBSITE).text
        soup = BeautifulSoup(source, 'lxml')

#tr
        tr = soup.find_all('tr',class_='colone')
        tr1 = soup.find_all('tr',class_='coltwo')
        for td in tr:
            to=td.find_all('td')[1]
            ao=td.find_all('a')
            for io in to:
                yo = io.text    
            for oo in ao:
                lo = oo.text
                mo = yo.replace('₽1 RUB = €','')
                ko = lo.replace('Russian Rouble Euro rate for ','')
                so = ','
                uo = mo+so+ko  
                uo = uo.split(',')
    
            for no in uo:
                if jap in no:
                    length = len(uo)

                    middle_index = length // 2

                    first_half = uo[:middle_index]
                    

                    nauda = first_half
    #tr1
        for td1 in tr1:
            to1=td1.find_all('td')[1]
            ao1=td1.find_all('a')
            for io1 in to1:
                yo1 = io1.text    
            for oo1 in ao1:
                lo1 = oo1.text
                mo1 = yo1.replace('₽1 RUB = €','')
                ko1 = lo1.replace('Russian Rouble Euro rate for ','')
                so1 = ','
                uo1 = mo1+so1+ko1  
                uo1 = uo1.split(',')
    
            for no1 in uo1:
                if jap in no1:
                    length = len(uo1)

                    middle_index = length // 2

                    first_half = uo1[:middle_index]
                    

                    nauda = first_half
         
        nauda = ' '.join(map(str, nauda))
        nauda = float(nauda)
        
        

        pp = round((y/(0.137*0.061)),2)
        oo = round((y/b), 2) 
        aa= round((y/b), 2)
        ss = round((y/b), 2)
        dd = round((y/b), 2)
        ll = round((y/n), 2)
        gg = round((y/n), 2)

        kk = round((pp*5*nauda),2)
        qq = round((oo*10*nauda),2)
        ww = round((aa*50*nauda),2)
        ee = round((ss*100*nauda),2)
        rr = round((dd*500*nauda),2)
        tt = round((ll*1000*nauda),2)
        uu = round((gg*5000*nauda),2)

        output.insert(END,'m^2 cenas datumā ')
        output.insert(END,jap)
        output.insert(END,' kurss ')
        output.insert(END,nauda)
        output.insert(END,'\n')

        output.insert(END,'5 rubļu banknošu skaits ')   
        output.insert(END,pp)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,kk) 
        output.insert(END,'\n')
        #2
        output.insert(END,'10 rubļu banknošu skaits ')
        output.insert(END,oo)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,qq)
        output.insert(END,'\n')
        #3
        output.insert(END,'50 rubļu banknošu skaits  ')
        output.insert(END,aa)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,ww)
        output.insert(END,'\n')
        #4
        output.insert(END,'100 rubļu banknošu skaits  ')
        output.insert(END,ss)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,ee)
        output.insert(END,'\n')
        #5
        output.insert(END,'500 rubļu banknošu skaits  ')
        output.insert(END,dd)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,rr)
        output.insert(END,'\n')
        #6
        output.insert(END,'1000 rubļu banknošu skaits  ')
        output.insert(END,ll)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,tt)
        output.insert(END,'\n')
        #7
        output.insert(END,'5000 rubļu banknošu skaits  ')
        output.insert(END,gg)
        output.insert(END,'  ')
        output.insert(END,'eiro skaits  ')
        output.insert(END,uu)
        output.insert(END,'\n')
        output.insert(END,'jā tev būs jāgriež nauda')
        




def cli():
    x = textentry.get()
    output.delete(0.0,END)
    
   
    y= float(x)
    if textentry1.get() == '0':
        output.delete(0.0,END)


        i = y*f

        i = round(i, 2)
        k = math.trunc(i/5)
        q = math.trunc(i/10)
        w = math.trunc(i/20)
        e = math.trunc(i/50)
        r = math.trunc(i/100)
        t = math.trunc(i/200)
        u = math.trunc(i/500)
        
        p = round(k*0.120*0.062, 3)
        o = round(q*0.127*0.067, 3)
        a = round(w*0.133*0.072, 3)
        s = round(e*0.140*0.077, 3)
        d = round(r*0.147*0.082, 3)
        l = round(t*0.153*0.082, 3)
        g = round(u*0.160*0.082, 3)    

        output.insert(END,'tavi euro šodien ')
        output.insert(END,i)
        output.insert(END,'\n')
        output.insert(END,'5 eur banknošu skaits  ')
        output.insert(END,k)
        output.insert(END,'  ')
        output.insert(END,'tapetes no 5 eur m^2  ')
        output.insert(END,'\n')
        output.insert(END,'10 eur banknošu skaits  ')
        output.insert(END,q)
        output.insert(END,'  ')
        output.insert(END,'tapetes no 10 eur m^2  ')
        output.insert(END,o)
        output.insert(END,'\n')
        output.insert(END,'20 eur banknošu skaits  ')
        output.insert(END,w)
        output.insert(END,'  ')
        output.insert(END,'tapetes no 20 eur m^2  ')
        output.insert(END,a)
        output.insert(END,'\n')
        output.insert(END,'50 eur banknošu skaits  ')
        output.insert(END,e)
        output.insert(END,'  ')
        output.insert(END,'tapetes no 50 eur m^2  ')
        output.insert(END,s)
        output.insert(END,'\n')
        output.insert(END,'100 eur banknošu skaits  ')
        output.insert(END,r)
        output.insert(END,'  ')
        output.insert(END,'tapetes no 100 eur m^2  ')
        output.insert(END,d)
        output.insert(END,'\n')
        output.insert(END,'200 eur banknošu skaits  ')
        output.insert(END,t)
        output.insert(END,'  ')
        output.insert(END,'tapetes no 200 eur m^2  ')
        output.insert(END,l)
        output.insert(END,'\n')
        output.insert(END,'500 eur banknošu skaits  ')
        output.insert(END,u)
        output.insert(END,'  ')
        output.insert(END,'tapetes no 500 eur m^2  ')
        output.insert(END,g)
        output.insert(END,'\n')
    else: 
        lol = textentry1.get()
        output.delete(0.0,END)
          
        jap = lol
        start = 0
        stop = 5
        if len(lol) > stop :
            lol = lol[0: start:] + lol[stop + 1::]
        ne = lol
        web = 'https://www.exchangerates.org.uk/RUB-EUR-spot-exchange-rates-history-'

        ja = '.html'
        opa = web+ne+ja


        WEBSITE = opa
        source = requests.get(WEBSITE).text
        soup = BeautifulSoup(source, 'lxml')

#tr
        tr = soup.find_all('tr',class_='colone')
        tr1 = soup.find_all('tr',class_='coltwo')
        for td in tr:
            to=td.find_all('td')[1]
            ao=td.find_all('a')
            for io in to:
                yo = io.text    
            for oo in ao:
                lo = oo.text
                mo = yo.replace('₽1 RUB = €','')
                ko = lo.replace('Russian Rouble Euro rate for ','')
                so = ','
                uo = mo+so+ko  
                uo = uo.split(',')
    
            for no in uo:
                if jap in no:
                    length = len(uo)

                    middle_index = length // 2

                    first_half = uo[:middle_index]
                    second_half = uo[middle_index:]

                    nauda = first_half
    #tr1
        for td1 in tr1:
            to1=td1.find_all('td')[1]
            ao1=td1.find_all('a')
            for io1 in to1:
                yo1 = io1.text    
            for oo1 in ao1:
                lo1 = oo1.text
                mo1 = yo1.replace('₽1 RUB = €','')
                ko1 = lo1.replace('Russian Rouble Euro rate for ','')
                so1 = ','
                uo1 = mo1+so1+ko1  
                uo1 = uo1.split(',')
    
            for no1 in uo1:
                if jap in no1:
                    length = len(uo1)

                    middle_index = length // 2

                    first_half = uo1[:middle_index]
                    second_half = uo1[middle_index:]

                    nauda = first_half
         
        nauda = ' '.join(map(str, nauda))
        nauda = float(nauda)
        
        yy = y*nauda

        yy = round(yy, 2)
        kk = math.trunc(yy/5)
        qq = math.trunc(yy/10)
        ww = math.trunc(yy/20)
        ee = math.trunc(yy/50)
        rr = math.trunc(yy/100)
        tt = math.trunc(yy/200)
        uu = math.trunc(yy/500)
        
        pp = round(kk*0.120*0.062, 3)
        oo = round(qq*0.127*0.067, 3)
        aa = round(ww*0.133*0.072, 3)
        ss = round(ee*0.140*0.077, 3)
        dd = round(rr*0.147*0.082, 3)
        ll = round(tt*0.153*0.082, 3)
        gg = round(uu*0.160*0.082, 3)

        output.insert(END,'tavi euro ')
        output.insert(END,jap)
        output.insert(END,' datumā ')
        output.insert(END,yy)
        output.insert(END,' kurss ')
        output.insert(END,nauda)
        output.insert(END,'\n')

        output.insert(END,'5 eur banknošu skaits  ')
        output.insert(END,kk)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,pp)
        output.insert(END,'\n')

        output.insert(END,'10 eur banknošu skaits  ')
        output.insert(END,qq)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,oo)
        output.insert(END,'\n')

        output.insert(END,'20 eur banknošu skaits  ')
        output.insert(END,ww)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,aa)
        output.insert(END,'\n')

        output.insert(END,'50 eur banknošu skaits  ')
        output.insert(END,ee)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,ss)
        output.insert(END,'\n')

        output.insert(END,'100 eur banknošu skaits ')
        output.insert(END,rr)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,dd)
        output.insert(END,'\n')

        output.insert(END,'200 eur banknošu skaits  ')
        output.insert(END,tt)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,ll)
        output.insert(END,'\n')

        output.insert(END,'500 eur banknošu skaits  ')
        output.insert(END,uu)
        output.insert(END,'  ')
        output.insert(END,'cik m^2 tev būs ')
        output.insert(END,gg)
        output.insert(END,'\n')

def cl():
    x = textentry.get()
    output.delete(0.0,END)
  
    y= float(x)
    if textentry1.get() == '0':

        p = round((y/(0.120*0.062)),2)
        o = round((y/(0.127*0.067)), 2) 
        a = round((y/(0.133*0.072)), 2)
        s = round((y/(0.140*0.077)), 2)
        d = round((y/(0.147*0.082)), 2)
        l = round((y/(0.153*0.082)), 2)
        g = round((y/(0.160*0.082)), 2)

        k = round((p*5/f),2)
        q = round((o*10/f),2)
        w = round((a*20/f),2)
        e = round((s*50/f),2)
        r = round((d*100/f),2)
        t = round((l*200/f),2)
        u = round((g*500/f),2)
        
    #1

        output.insert(END,'5 eur banknošu skaits  ')
        output.insert(END,p)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits')
        output.insert(END,k) 
        output.insert(END,'\n')
        #2
        output.insert(END,'10 eur banknošu skaits ')
        output.insert(END,o)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,q)
        output.insert(END,'\n')
        #3
        output.insert(END,'20 eur banknošu skaits  ')
        output.insert(END,a)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,w)
        output.insert(END,'\n')
        #4
        output.insert(END,'50 eur banknošu skaits  ')
        output.insert(END,s)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,e)
        output.insert(END,'\n')
        #5
        output.insert(END,'100 eur banknošu skaits  ')
        output.insert(END,d)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,r)
        output.insert(END,'\n')
        #6
        output.insert(END,'200 eur banknošu skaits  ')
        output.insert(END,l)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,t)
        output.insert(END,'\n')
        #7
        output.insert(END,'500 eur banknošu skaits  ')
        output.insert(END,g)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,u)
        output.insert(END,'\n')
        output.insert(END,'jā tev būs jāgriež nauda')
    else:
        lol = textentry1.get()
        output.delete(0.0,END)
          
        jap = lol
        start = 0
        stop = 5
        if len(lol) > stop :
            lol = lol[0: start:] + lol[stop + 1::]
        ne = lol
        web = 'https://www.exchangerates.org.uk/RUB-EUR-spot-exchange-rates-history-'

        ja = '.html'
        opa = web+ne+ja


        WEBSITE = opa
        source = requests.get(WEBSITE).text
        soup = BeautifulSoup(source, 'lxml')

#tr
        tr = soup.find_all('tr',class_='colone')
        tr1 = soup.find_all('tr',class_='coltwo')
        for td in tr:
            to=td.find_all('td')[1]
            ao=td.find_all('a')
            for io in to:
                yo = io.text    
            for oo in ao:
                lo = oo.text
                mo = yo.replace('₽1 RUB = €','')
                ko = lo.replace('Russian Rouble Euro rate for ','')
                so = ','
                uo = mo+so+ko  
                uo = uo.split(',')
    
            for no in uo:
                if jap in no:
                    length = len(uo)

                    middle_index = length // 2

                    first_half = uo[:middle_index]
                    

                    nauda = first_half
    #tr1
        for td1 in tr1:
            to1=td1.find_all('td')[1]
            ao1=td1.find_all('a')
            for io1 in to1:
                yo1 = io1.text    
            for oo1 in ao1:
                lo1 = oo1.text
                mo1 = yo1.replace('₽1 RUB = €','')
                ko1 = lo1.replace('Russian Rouble Euro rate for ','')
                so1 = ','
                uo1 = mo1+so1+ko1  
                uo1 = uo1.split(',')
    
            for no1 in uo1:
                if jap in no1:
                    length = len(uo1)

                    middle_index = length // 2

                    first_half = uo1[:middle_index]
                    

                    nauda = first_half
         
        nauda = ' '.join(map(str, nauda))
        nauda = float(nauda)
        
        

        pp = round((y/(0.120*0.062)),2)
        oo = round((y/(0.127*0.067)), 2) 
        aa = round((y/(0.133*0.072)), 2)
        ss= round((y/(0.140*0.077)), 2)
        dd = round((y/(0.147*0.082)), 2)
        ll = round((y/(0.153*0.082)), 2)
        gg = round((y/(0.160*0.082)), 2)

        kk = round((pp*5/nauda),2)
        qq = round((oo*10/nauda),2)
        ww = round((aa*20/nauda),2)
        ee = round((ss*50/nauda),2)
        rr = round((dd*100/nauda),2)
        tt = round((ll*200/nauda),2)
        uu = round((gg*500/nauda),2)

        output.insert(END,'m^2 cenas datumā ')
        output.insert(END,jap)
        output.insert(END,'kurss ')
        output.insert(END,nauda)
        output.insert(END,'\n')

        output.insert(END,'5 eiro banknošu skaits ')              
        output.insert(END,pp)
        output.insert(END,' rubļu skaits  ')
        output.insert(END,kk) 
        output.insert(END,'\n')
        #2
        output.insert(END,'10 eiro banknošu skaits ')
        output.insert(END,oo)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,qq)
        output.insert(END,'\n')
        #3
        output.insert(END,'20 eiro banknošu skaits  ')
        output.insert(END,aa)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,ww)
        output.insert(END,'\n')
        #4
        output.insert(END,'50 eiro rubļu banknošu skaits  ')
        output.insert(END,ss)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits skaits  ')
        output.insert(END,ee)
        output.insert(END,'\n')
        #5
        output.insert(END,'100 eiro banknošu skaits  ')
        output.insert(END,dd)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,rr)
        output.insert(END,'\n')
        #6
        output.insert(END,'200 eiro banknošu skaits  ')
        output.insert(END,ll)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,tt)
        output.insert(END,'\n')
        #7
        output.insert(END,'500  eiro banknošu skaits  ')
        output.insert(END,gg)
        output.insert(END,'  ')
        output.insert(END,'rubļu skaits  ')
        output.insert(END,uu)
        output.insert(END,'\n')
        output.insert(END,'jā tev būs jāgriež nauda')


###galvenais
window = Tk()
window.title('bistami.exe')
window.configure(background ='black')
## bilde
photo = PhotoImage(file = ga)
Label (window, image=photo, bg = 'white').grid(row = 0 , column = 0, sticky = W)
## label
Label (window, text = 'pašreizējais rubļa  kurss', bg= 'black', fg = 'white', font = 'font.ttf',).grid(row = 1, column= 0, sticky=W)
Label (window, text = 'ievadi datumu formātā DD/MM/GGGG,', bg= 'black', fg = 'white', font = 'font.ttf',).grid(row = 1, column= 1, sticky=W)

Label (window, text = 'ja vēlies šodienas datumu ievadi 0', bg= 'black', fg = 'white', font = 'font.ttf',).grid(row = 2, column= 1, sticky=W)
Label (window, text = 'mazākais datums ir 01/01/2010', bg= 'black', fg = 'white', font = 'font.ttf',).grid(row = 3, column= 1, sticky=W)
Label (window, text = f, bg= 'black', fg = 'white', font = 'font.ttf',).grid(row = 2, column= 0, sticky=W)
Label (window, text = 'ievadi skaitli ieteicams ne lielāku par 1000000', bg= 'black', fg = 'white', font = 'font.ttf',).grid(row = 3, column= 0, sticky=W)
##textbox
textentry = Entry(window, width = 20, bg = 'white')
textentry.grid(row = 4, column = 0, sticky = W )
textentry1 = Entry(window, width = 20, bg = 'white')
textentry1.grid(row = 4, column = 1, sticky = W )



## pogas
Button (window, text = 'rubļu tapetes' ,width= 17, command = click).grid(row = 8, column = 0 , sticky= W)
Button (window, text = 'ievadi m^2 un nospied' ,width= 17, command = clic).grid(row = 10, column = 0 , sticky= W)
Button (window, text = 'euro tapetes' ,width= 17, command = cli).grid(row = 8, column = 1 , sticky= W)
Button (window, text = 'ievadi m^2 un nospied' ,width= 17, command = cl).grid(row = 10, column = 1 , sticky= W)
## velviens label
Label (window, text = 'rezultāts', bg= 'black', fg = 'white', font = 'font.ttf',).grid(row = 20, column= 0, sticky=W)
#velviens textbox
output = Text(window, width=100, height = 10, wrap = WORD, background = 'white')
output.grid(row = 50, column = 0, columnspan = 2, sticky=W)
window.mainloop()