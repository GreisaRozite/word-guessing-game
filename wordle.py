# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:03:56 2026

@author: sabin
"""

w = 'HELLO'

def word_generator():
    pass

def guessing():
    print('provide a five letter word! \n')

    guess = input()

    if len(guess) != 5:
        if len(guess) > 5:
            print('not accepted, too long')
            guessing()
        if len(guess) < 5:
            print('not accepted, too short')
            guessing()
    else:
        return guess


def mechanism(answer, n, word):
 
    if n == 1:
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        
        print(f'you have {n} more try to guess the word!')
        guess=guessing().upper()
        
        for i in range(5):
            if guess[i] == word[i]:
                answer[i] = guess[i]
        
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        print('\n'+interface_answer)
        if word == list(guess):
            print('you won!')
        else:
            print('\nyou lost!')
            print(f'the word was:')
            interface_word=word[0]+' '+word[1]+' '+word[2]+' '+word[3]+' '+word[4]
            print(interface_word)
                  
        
    else:
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
    
        if n == 5:
            print(interface_answer)
            print(f'\nyou have {n} tries to guess the word!')
        else:
            print(f'you have {n} more tries to guess the word!')
        guess=guessing().upper()
        
        for i in range(5):
            if guess[i] == word[i]:
                answer[i] = guess[i]
        
        interface_answer=answer[0]+' '+answer[1]+' '+answer[2]+' '+answer[3]+' '+answer[4]
        
        print('\n'+interface_answer+'\n')
        return answer
    
def wordle():
    #first guess initialization:
    n=5
    answer = ['_','_','_','_','_']
    word = [w[0], w[1], w[2], w[3], w[4]]
    
    while n != 0:
        current = mechanism(answer, n, word)
        answer = current
        n=n-1
        if current == word:
            print('you won!')
            break 
        
wordle()
    

    

    
    
    