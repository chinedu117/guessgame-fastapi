from typing import Optional

from fastapi import FastAPI
import random
import math

app = FastAPI()


@app.get("/get_secret")
def secret_number():
    def isPrime(num):
        isPrime = True
        for divisor in range(2,num):
            if(num % divisor == 0):
                isPrime =  False
        return isPrime
    primes = [i for i in range(2,100) if isPrime(i)]
    answer = random.choice(primes)

    firstNumber = math.floor(answer/2)
    secondNumber = math.floor((answer - firstNumber)/2)
    thirdNumber = round((answer - firstNumber - secondNumber)/2)
    fourthNumber = answer - firstNumber - secondNumber - thirdNumber

    hints = [firstNumber,secondNumber,thirdNumber,fourthNumber]
    hints = ','.join(map(str,hints))
    return {"sum_clues": hints, "prime_secret_number": answer}