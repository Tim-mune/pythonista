import requests
import bs4
from random import choice
from time import sleep
list_quotes=[]
base_url="http://quotes.toscrape.com/"
url="/page/1"
while url:
    res=requests.get(f'{base_url}{url}')
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    quotes=soup.find_all(class_='quote')
    for quote in quotes:
        quotes_text=quote.find(class_='text').get_text()
        author=quote.find(class_='author').get_text()
        bio=quote.find('a')['href']
        list_quotes.append({
            "text":quotes_text,
            "author":author,
            "bio":bio,
        })
    next_btn=soup.find(class_='next')    
    url=(next_btn.find('a')['href']) if next_btn else None
    # sleep(2)
def startGame():
        
    quote=choice(list_quotes)
    num_guesses=4
    print(quote['text'])
    print(quote['author'])
    guess=''
    while guess.lower()!= quote['author'].lower():
        if guess.lower()== quote['author'].lower():
            print('damn you got it right')
            break;
        guess=input('whos the author??')
        print(f'{num_guesses} trials remaining')
        num_guesses-=1
        if num_guesses==3:
            res=requests.get(f"{base_url}{quote['bio']}")
            soup=bs4.BeautifulSoup(res.text,'html.parser')
            birth_date=soup.find(class_='author-born-date').get_text()
            birth_place=soup.find(class_='author-born-location').get_text()
            print(f"heres a hint author was born on {birth_date}  {birth_place}")
        elif num_guesses==2:
            print(f'another hint: the authors name starts with{quote["author"][0]}')
        elif num_guesses==1:
            last_name=quote['author'].split(' ')[1]
            print(f'another hint: the authors last name starts with {last_name}')
        else:
            print(f'you ran out of guesses the answer is {quote["author"]}')  
            break; 
    play_again=''       
    while play_again.lower() not in ('y','yes','n','no'):
        print('invalid response please try again')
        play_again=input('would you like to play again?? (y/n)?')
    if play_again.lower() in ('yes','y'):
        return startGame()
    else:
        print('okay logged out')    
                
       
startGame()    


    

