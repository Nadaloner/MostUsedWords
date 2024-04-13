import requests
import re
from bs4 import BeautifulSoup
import click

def get_html_of(url):
    resp=requests.get(url)
    if resp.status_code!=200:
        print(f"codice errore {resp.status_code}")
    return resp.content.decode()
    
def get_all_words_from(url):
   html=get_html_of(url)
   soup=BeautifulSoup(html,'html.parser')
   raw_text=soup.get_text()
   return re.findall(r'\w+', raw_text) 

def conta_parole_in(word_list,min_lenght):
    word_count={}
    for word in word_list:
        if len(word)<min_lenght:
            continue
        elif word not in word_count:
            word_count[word]=1
        else:
            current_count=word_count.get(word)
            word_count[word]=current_count+1
    return word_count

def get_top_words_from(all_words,min_lenght):
    occurrences=conta_parole_in(all_words,min_lenght)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)
@click.command()
@click.option('--target', '-u',prompt='web URL',help='url of the page that you want to scan')
@click.option('--min_lenght', '-l',prompt='word lenght',default=0,help='minimun word lenght,default 0 ->    no limit')
def main(target,min_lenght):
    #implementezione funzioni di controllo
    all_words=get_all_words_from(target)
    top_words=get_top_words_from(all_words,min_lenght)

    for i in range(10):
        print(top_words[i][0])
    
if __name__ == '__main__':
    main()
    
  

 
   
    