# -*- coding: utf-8 -*-
from bs4 import *
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from urllib.request import Request
from termcolor import colored as cl
import random as rn
import wikipedia as wiki

#Function to scrape and pull the word of the day from Dictionary.com
def wordADay():
    
    nary = "https://www.dictionary.com/e/word-of-the-day/"
    naryClient = req(nary)
    site_parse_nary = soup(naryClient.read(), "lxml") 
    naryClient.close()
    
    #Pull from 'Word of the Day' wrapper
    wordDayCase = site_parse_nary.find("div", {"class": "wotd-item-wrapper"})
    #Pull the word itself
    wordDay = wordDayCase.find("div", {"class": "wotd-item-headword__word"}).text.strip()
    #Pull the pronunciation 
    wordSpeak = wordDayCase.find("div", {"class": "wotd-item-headword__pronunciation"}).text.strip()
    #Pull the definition 
    wordMean = wordDayCase.find("div", {"class": "wotd-item-headword__pos-blocks"})
    wordType = wordMean.find("span").text.strip()
    wordDef = wordMean.findAll("p")[1].text.strip()
    
    print(cl(wordDay, "blue"))
    print(cl(wordSpeak, "red"))
    print(cl("----------------------", "grey"))
    print(cl("Word type: " + wordType, "cyan"))
    print(cl(wordDef, "blue"))
    
#    tab1_layout = [
#            [sg.T(wordDay)],
#            [sg.T(wordSpeak)],
#            [sg.T('---------')],
#            [sg.T('Word type: ' + wordType)],
#            [sg.T(wordDef)]
#            ]
#    
#    return tab1_layout

#Function to pull a random quote from the GoodReads popular quotes page
def quoteADay():
    
    goodReads = "https://www.goodreads.com/quotes"
    goodClient = req(goodReads)
    site_parse_quote = soup(goodClient.read(), "lxml")
    goodClient.close()
    
    #Pull from the left container 
    quotesOnly = site_parse_quote.find("div", {"class": "leftContainer"})
    #Randomly choose a quote from the front page
    ranQuote = quotesOnly.find("div", {"class": "quotes"}).findAll("div", {"class": "quote"})[rn.randrange(30)]
    #Pull info from ranQuote
    sourceQuote = ranQuote.find("span").text.strip()
    quote = ranQuote.find("div", {"class": "quoteText"}).text.strip().split('\n')[0]
    #Give a little background info about the author of the quote
    authorInfo = wiki.summary(sourceQuote, sentences=1)
    
    print(cl(quote, "green"))
    print(cl('~'+'\033[1m'+sourceQuote+'~', "magenta"))
    print(cl(authorInfo, "magenta"))
    
#    tab2_layout = [
#            [sg.T(quote)],
#            [sg.T('~'+sourceQuote+'~')],
#            [sg.T(authorInfo)]
#            ]
#
#    return tab2_layout

#Function to pull a random word from dict.tu 
def deustchesWort():
    
    dicttu = "https://dict.tu-chemnitz.de/dings.cgi?o=3020;service=deen;random=en"
    dictClient = req(dicttu)
    site_parse_deutsch = soup(dictClient.read(), "lxml")
    dictClient.close()
    
    #Pull a subject in order to find a word
    subDeutsch = site_parse_deutsch.find("div", {"class": "result"}).find("table", {"id": "result"})
    wortAlles = subDeutsch.find("tbody", {"id": "h1"}).find("tr", {"class": "s1"}).text.strip()
    wort = wortAlles.split('\n')[0]
    wortDef = wortAlles.split('\n')[1]
        
    print(cl("Deutsches Wort: ", "yellow"))
    print(cl(wort, "blue"))
    print(cl("auf Englisch: " + wortDef, "red"))
    #In case a search is incomplete or not found
    try:
        wortInfo = wiki.summary(wortDef,sentences=2, auto_suggest=False)
    except:
        print("Page not found for English entry")
    else:
        print(cl(wortInfo, "green"))


def main():
    
    print(cl("~~~~~~~~~~~~~~~Word of the Day~~~~~~~~~~~~~~~~", "grey"))
    wordADay()
    print(cl("~~~~~~~~~~~~~~~Quote for the Day~~~~~~~~~~~~~~", "grey"))
    quoteADay()
    print(cl("~~~~~~~~~~~~~German Word of the Day~~~~~~~~~~~~~", "grey"))
    deustchesWort()

    
#    sg.theme('Dark Blue 3')  
#    
#    layout = [[
#            sg.TabGroup([
#                    [sg.Tab('Word of the Day', wordADay()),
#                     sg.Tab('Quote for the Day', quoteADay())]
#                    ])
#            ]]
#    
#    window = sg.Window('Start New', layout, 
#                       grab_anywhere=True, finalize=True)
  
    
if __name__ == "__main__":
    main()
    
    
    
    
    



    

    
    
    
    