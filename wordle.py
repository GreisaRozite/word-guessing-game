# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:03:56 2026

@author: sabin
"""
# add a timeout and try/except on requests. get

import requests
import random

url = "https://darkermango.github.io/5-Letter-words/words.json"
response = requests.get(url)
words = response.json()

count_of_words=len(words['words'])

def guessing():
    print('provide a five letter word! \n')

    guess_case_ignore = input()
    guess=guess_case_ignore.lower()

    if len(guess) != 5:
        if len(guess) > 5:
            print('\nnot accepted, too long')
        if len(guess) < 5:
            print('\nnot accepted, too short')
        return guessing()
    else:
        if guess in words['words']:
            return guess
        else:
            print('not a valid word')
            return guessing()

def mechanism(answer, n, word, word_end):
 
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        answer = ['\033[0m_','\033[0m_','\033[0m_','\033[0m_','\033[0m_']
    
        if n == 1:
            print(f'\033[0myou have {n} more try to guess the word!')
        elif n == 5:
            print(interface_answer)
            print(f'\nyou have {n} tries to guess the word!')
        else:
            print(f'\033[0myou have {n} more tries to guess the word!')       
     
        guess=guessing().upper()
        
#greens:
        for i in range(5):
            if guess[i] == word[i]:
                w = guess[i]
                w_green=f'\033[92m{w}'
                answer[i] = w_green
        
        alt_answer = ['_','_','_','_','_']
        
        for i in range(5):
            alt_answer[i]=answer[i]
        
#yellows:
        yellow_d = {}
        #dictionary of yellow letters and counts of occurances
        
        for i in range(5):
            for j in range(5):
                if guess[i] == word[j]:
                    if i == j or alt_answer[i] != '\033[0m_':
                        pass
                    #skips if already filltered, is green, so no overwriting
                    else:
                        letter = word[j]
                        count = word.count(letter) #amount of times yellow letter in word
                        letter_yellow=f'\033[33m{letter}'
                        alt_answer[i] = letter_yellow
                        if letter_yellow in yellow_d:
                            pass
                        else:
                            yellow_d[letter_yellow]=count
                            
        for i in yellow_d:
            letter = i[-1:]
            count = yellow_d[i]
            tracker = 0
            bare_letter = letter[-1:]
            red = f'\033[91m{bare_letter}'
            for j, k in enumerate(alt_answer):
                if k[-1:] == letter:
                    if tracker == count:
                        alt_answer[j]=red
                    else:
                        tracker+=1
                else:
                    pass #because isnt yellow
                    
#reds:              
        for i in range(5):
            v=0
            for j in range(5):
                if guess[i] == word[j]:
                        v=1
            if v==0:
                w=guess[i]
                w_red=f'\033[91m{w}'
                alt_answer[i]=w_red
        
        interface_answer=alt_answer[0]+' '+alt_answer[1]+' '+alt_answer[2]+' '+alt_answer[3]+' '+alt_answer[4]
        
#last answer checker
        if n == 1:
            print('\n'+interface_answer)
            if word == list(guess):
                print('\033[0myou won!')
            else:
                print('\033[0m\nyou lost!')
                print('the word was:')
                interface_word=word[0]+' '+word[1]+' '+word[2]+' '+word[3]+' '+word[4]
                print(interface_word)
                 
        else:
            print('\n'+interface_answer+'\n')
            return answer
    
def wordle():
    #first guess initialization:
    number=random.randrange(count_of_words)
    w=words['words'][number]
    w=w.upper()
    
    n=5
    answer = ['\033[0m_','\033[0m_','\033[0m_','\033[0m_','\033[0m_']
    word = [w[0],w[1],w[2],w[3],w[4]]
    word_end = [f'\033[92m{w[0]}', f'\033[92m{w[1]}', f'\033[92m{w[2]}', f'\033[92m{w[3]}', f'\033[92m{w[4]}']

    while n != 0:
        current = mechanism(answer, n, word, word_end)
        answer = current
        n=n-1
        if current == word_end :
            print('\033[00myou won!')
            break 
        
wordle()
    

    

    
    
    