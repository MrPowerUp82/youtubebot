import socket
import time
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
print("As proxies devem estar assim na lista -> 192.168.1.1:8080") 
print("A url deve ser inserida dentro do script")
file=input("Lista das proxies-> ")
arq=open("{}".format(file), 'r').readlines()
file2=input("Nome da lista de saida-> ")
arq2=open("{}".format(file2),'w')
openproxy=[]
for line in arq:
    l=line.strip()
    l=str(l)
    ipon=l
    l=l.split(':')
    ip=str(l[0])
    port=int(l[1])
    try:
        time.sleep(0.5)
        ps=socket.socket()
        ps.connect((ip,port))
        print(ip,port,"ON")
        openproxy.append(ipon)
        ps.close()
        http="https://www.youtube.com/watch?v=cPvw_pkFLlI"
        #prox = Proxy()
        print(l)
        PROXY=ipon
        #prox.proxy_type = ProxyType.MANUAL
        #prox.http_proxy = l
        #prox.socks_proxy = "ip_addr:port"
        #prox.ssl_proxy = "ip_addr:port"

        #capabilities = webdriver.DesiredCapabilities.CHROME
        #prox.add_to_capabilities(capabilities)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome(options=chrome_options, executable_path='chromedriver.exe')
        #driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path='chromedriver.exe')
        driver.get(http)
        time.sleep(20)
        select=driver.find_element_by_xpath('//*[@id="movie_player"]/div[4]/button')
        select.click()
        time.sleep(65)
        driver.close()
    except socket.error:
        print(ip,port,"OFF")

for line in openproxy:
    arq2.write("{}\n".format(line))

arq2.close()
