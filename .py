import requests
from bs4 import BeautifulSoup

def preco_produto_simples():
  
    url="https://www.amazon.com.br/Novo-Echo-Dot-Max-Preto/dp/B0DKLNNYY4/ref=sr_1_4?crid=3W08TMXHDNFMQ&dib=eyJ2IjoiMSJ9.1qsSQOGLfycFErhYvbnGRYZZuSW1jRR3vwLi93TipE0_IfP-SSsUQZpeDkqjqBm_b5tpR-1zRbfcUsSsGeFRz00kYLk3kQPdlY63HKXle2Hztc2NYqMkjFrwyVMVu7taqeLin3mWNVYaaMD60vbgDwqQ-zUKvFtGGzxfssyVvZB0Em9kEGauls7Qzve9oJF4A2EqwVU7adtNqis6fjeY_vPSv6QU1bn8zAzD7PZtQRBMJ1cDwe36LUqZ1Z9wTmz5AiavB0kBrzzASvfI7dKDnJDpFPORZLhYJtm8QtUEh8c.1jKP1_TQm-vBd2EuCnqT-h88ExlJTh0KoBOZP4yxmB8&dib_tag=se&keywords=echo%2Bdot&qid=1762178887&sprefix=ech%2Caps%2C234&sr=8-4&ufe=app_do%3Aamzn1.fos.95de73c3-5dda-43a7-bd1f-63af03b14751&th=1"
    try:
    
        response = requests.get(url)
        soup=BeautifulSoup(response.content, 'html.parser')




        # nome=soup.find('div', class_=' ')
        preco=soup.find('span', class_='a-price-whole')




        if preco:
            # print(f"Nome: {nome.text.strip()}")
            print(f"Preco: {preco.text.strip()}")
        else:
            print(f"🔎 Produto não encontrado")
   
    except Exception as e:
        print(f"❌ Erro {e}")






preco_produto_simples()