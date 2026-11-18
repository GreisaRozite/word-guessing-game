# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:03:56 2026

@author: sabin
"""

w = 'GRACE'

def word_generator():
    pass

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
        return guess
    
    return guess


def mechanism(answer, n, word, word_end):
 
    if n == 1:
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        
        print(f'you have {n} more try to guess the word!')
        guess=guessing()
     
        for i in range(5):
            if guess[i] == word[i]:
                w = guess[i]
                w_color=f'\033[92m{w}'
                answer[i] = w_color
        
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        print('\n'+interface_answer)
        if word_end == list(guess):
            print('you won!')
        else:
            print('\nyou lost!')
            print('the word was:')
            interface_word=word[0]+' '+word[1]+' '+word[2]+' '+word[3]+' '+word[4]
            print(interface_word)
                  
        
    else:
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
    
        if n == 5:
            print(interface_answer)
            print(f'\nyou have {n} tries to guess the word!')
        else:
            print(f'\033[0myou have {n} more tries to guess the word!')
        guess=guessing().upper()
        
       
        for i in range(5):
            if guess[i] == word[i]:
                w = guess[i]
                w_color=f'\033[92m{w}'
                answer[i] = w_color
        
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        
        print('\n'+interface_answer+'\n')
        return answer
    
def wordle():
    #first guess initialization:
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
    

    

    
    
    