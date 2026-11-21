# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:03:56 2026

@author: sabin
"""

# current running bug: multiple yellows even if answer has only one
# example word = FUDGE if user inputs 'ENDER' both 'E's show up yellow

import requests
import random

url = "https://darkermango.github.io/5-Letter-words/words.json"
response = requests.get(url)
words = response.json()

count_of_words=len(words['words'])-1

def guessing():
    print('provide a five letter word! \n')

    guess = input()

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
    
    return guess

def mechanism(answer, n, word, word_end):
 
    if n == 1:
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        answer = ['\033[0m_','\033[0m_','\033[0m_','\033[0m_','\033[0m_']
        
        print(f'\033[0myou have {n} more try to guess the word!')
        guess=guessing().upper()
     
        for i in range(5):
            if guess[i] == word[i]:
                w = guess[i]
                w_green=f'\033[92m{w}'
                answer[i] = w_green
        
        alt_answer = ['_','_','_','_','_']
        
        for i in range(5):
            alt_answer[i]=answer[i]
            
        for i in range(5):
            for j in range(5):
                if guess[i] == word[j]:
                    if i == j or alt_answer[i] != '\033[0m_':
                        pass
                    #skips if already filltered, is green, so no overwriting
                    else:
                        w = guess[i]
                        w_yellow=f'\033[33m{w}'
                        alt_answer[i] = w_yellow
        
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
        
        print('\n'+interface_answer)
        if word_end == list(guess):
            print('\033[0myou won!')
        else:
            print('\033[0m\nyou lost!')
            print('the word was:')
            interface_word=word[0]+' '+word[1]+' '+word[2]+' '+word[3]+' '+word[4]
            print(interface_word)
                  
        
    else:
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        answer = ['\033[0m_','\033[0m_','\033[0m_','\033[0m_','\033[0m_']
        
        if n == 5:
            print(interface_answer)
            print(f'\nyou have {n} tries to guess the word!')
        else:
            print(f'\033[0myou have {n} more tries to guess the word!')
        guess=guessing().upper()
       
        for i in range(5):
            if guess[i] == word[i]:
                w = guess[i]
                w_green=f'\033[92m{w}'
                answer[i] = w_green
        
        alt_answer = ['_','_','_','_','_']
        
        for i in range(5):
            alt_answer[i]=answer[i]
            
        #locks in the green 
            
        for i in range(5):
            for j in range(5):
                if guess[i] == word[j]:
                    if i == j or alt_answer[i] != '\033[0m_':
                        pass
                    #skips if already filleTRId, is green, so no overwriting
                    else:
                        w = guess[i]
                        w_yellow=f'\033[33m{w}'
                        alt_answer[i] = w_yellow
                        
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
    

    

    
    
    