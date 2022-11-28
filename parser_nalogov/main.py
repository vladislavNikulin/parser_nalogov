##########################################################
#                                                        #
#  Автор кода: Nikulin Vlad                              #
#                                                        #
#  Цель задачи:                                          #
#  нужно спарсить ссылку с оф. сайта налоговой службы,   #
#  далее скачать файл, после чего вывести след. данные:  #
#  1) Название файла                                     #
#  2) Путь к фалй                                        #
#  3) Время загрузки                                     #
#                                                        #
#  Код создан для портфолио kwork                        #
#                                                        #
#  Нужные модули:                                        #
#  pip3 install BeautifulSoup4 requests lxml wget        #
#                                                        #
##########################################################


from bs4 import BeautifulSoup as BS
import requests
import lxml
import wget
from datetime import datetime as dt
import os
import shutil

url = 'https://www.nalog.gov.ru/opendata/7707329152-masaddress/'

def pars(url):
	html = requests.get(url).text
	soup = BS(html, 'lxml')
	download_csv(soup.find('table', class_='border_table').find_all('tr')[8].find_all('td')[2].find('a').get('href'))

def download_csv(url):
	global name_file
	wget.download(url)
	name_file = url.split('/')[-1]
	create_dir(dt.now().year, dt.now().month, dt.now().day, dt.now().hour, dt.now().minute, dt.now().second)

def create_dir(y, mn, d, h, m, s):
	global dir_name
	dir_name = f'Result_{y}_{mn}_{d}__{h}_{m}_{s}'
	os.mkdir(f'{os.getcwd()}/{dir_name}')
	shutil.copy(f'{os.getcwd()}/{name_file}', f'{os.getcwd()}/{dir_name}')
	os.remove(f'{os.getcwd()}/{name_file}')
	
def main():
	pars(url)
	print(f'File name: {name_file}')
	print(f'Way to file: {os.getcwd()}\\{dir_name}\\{name_file}')
	print(f'Download time: {dt.now().hour}:{dt.now().minute}:{dt.now().second}')

if __name__ == '__main__':
	main()