from typing import Optional

from fastapi import FastAPI
import random
import math
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/get_secret")
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