"""
Solutions to module 1
Student: Hugo Jonsson
E-mail: Hugo8jonsson@gmail.com
Reviewed by:Shengkai
Review date: 2026-09-07
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have test code running at the top level (i.e. outside the main function),
you have to remove it before uploading your code into Studium!
Also remove any trace and debugging printouts!

You may not import any packages other than time and math. These may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documentation and and don't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    """Exc1: Computes m*n using additions"""
    if n==0:
        return 0
    elif n>0:
        return m + multiply(m,n-1)
    else:
        return -m + multiply(m,n+1)

def harmonic(n: int) -> float:              
    """Exc2: Computes and returns the harmonic sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n==0:
        return 0
    elif n>0:
        return 1/n + harmonic(n-1)
    else:
        return 1/n + harmonic(n+1)


def get_binary(x: int) -> str:              
    """Exc3: Returns the binary representation of x"""
    if x == 0: # 
        return '0'
    elif x == 1:
        return '1'
    elif x<0: # om negativt minus och kör pos uträkning
        return "-" + get_binary(abs(x)) 
    else:
        return get_binary(x//2) + str(x%2) 
    # modulo ger sista siffrans värde i basen, trunkerar i basen för nästa anrop (samma metod oavsett bas)
        



def reverse_string(s: str) -> str:        
    """Exc4: Returns the string s reversed """
    if len(s) <=1:
            return s
    else:
        return reverse_string(s[1:]) + s[0] 


def largest(a: list):
    """Exc5: Returns the largest element in a"""
    if len(a) == 1:
        return a[0]
    #jämför index 0 och 1 och skickar listan utan den minsta
    if a[0]>a[1]: 
        return largest([a[0]]+a[2:])
    else:
        return largest(a[1:])
        

def count(x, s: list) -> int:                
    """Exc6: Counts the number of occurences of x on all levels in s"""
    if s == []: # om tom lista return 0
        return 0

    cur = s[0]
    match = 1 if cur == x else 0 # kollar om första element är match
    nested = count(x, cur) if type(cur) == list else 0 # öppnar om typ av cur == lista

    return match + nested + count(x, s[1:]) #skickar allt + resten av orginal listan


def bricklek(f: str, t: str, h: str, n: int) -> list[str]:
    """Exc7: Returns a list of string instructions for how to move the tiles"""
    if n==0:
        return []
    return bricklek(f,h,t,n-1) + [f'{f}->{t}'] + bricklek(h,t,f,n-1)
    # hela djupet körs klart iom rekursion och fortsätter sedan åt höger.
    # vid basfallet vilket sker vid n=1 blir bara andra termen i uttrycket.
    # Tänk: varje 2 diskar är egentligen bara en basförflyttning + bottenplatta sen tillbaka men med olika mål. 

        

def fib(n: int) -> int:
    """For Exc9: Returns the n:th Fibonacci number"""
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n):
    memory = {0:0, 1:1}

    def _fib_mem(n):
        if n not in memory:
            memory[n] = _fib_mem(n-1) + _fib_mem(n-2)
        return memory[n]
    
    return _fib_mem(n)

def main():
    print('\nCode that demonstrates my implementations\n')

    print('\n\nCode for analysing fib and fib_mem\n')
    prev_time = None
    print("fib time for n and growth for subsequent n (no memory)")
    for i in range(34,41):
        tstart = time.perf_counter()
        fib(i)
        tstop = time.perf_counter()
        time_diff = tstop-tstart
        if prev_time is not None:
            print(f'n input:{i}   Time: {round(time_diff,3)} s  Growth: {round(time_diff/prev_time,5)}')
        prev_time = time_diff

    print("fib_mem time and number:")
    tstart = time.perf_counter()
    out = fib_mem(100)
    tstop = time.perf_counter()
    print(f'total time for fib_mem(100) is: {round(tstop-tstart,5)} and the number is: {out}')

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the non-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  Från exemplet i uppgiften får vi t(n) = 1 + 2t(n-1) vilket med teleskopering med basfall t(1)=1 ger den geometriska summan 2^i från i=0 till n-1 vilket är lika med 2^n-1. vilket är tidskomplexitet theta(2^n).
  För n=50 ger det t(50) = 2^50 - 1 vilket är ungefär, 36 miljoner år
  
  
  Exercise 9: Time for Fibonacci:
  a) vid högre n ligger tillväxten mycket nära 1.618 för n från n-1
  b) Från a får vi att tiden för n=40 är ca 13 sek, vi vet även att t(n) = c * 1.618^n, från uppgblad, vilket är proportionellt mot 1.618 vid stora n.
     Det ger att t(m)/t(n) = 1.618^(m-n).
     vilket ger t(50) = t(40)*1.618^10 = 13*1.618^10 = 1600 sek = 27 min
     Vidare blir t(100) = t(40)*1.618^60 = 13*1.618^60 = 1,4 miljoner år
     (OBS, alla = ska egentligen vara ungefär lika med, då t(n) går mot 1,618^n)
  
  Exercise 10: Time for fib_mem:
  total tid var en bråkdel av en sekund ( ofta <miljontedel) och talet var 354224848179261915075.
  
  
  
  Exercise 11: Comparison sorting methods:
  insertion_sort har en t(n) = n(n-1)/2 om t(1000) = 1 sek ger det t(10^6) = t(1000)*10^6(10^6-1)/(1000(1000-1)) = 1001000 sek, vilket är 11,6 dagar.  
  på samma sätt kan t(10^9) skrivas som t(10^9) = 1 * 10^18/10^6=10^12 vilket är ungefär 32000 år.
  Merge_sort har t(n) = nt(1) + dnlog(n) vilket vid stora n går mot c*n*log(n). Vi vet att t(1000) = 1 sek.
  Det ger för t(10^6) får vi c*10^6*log(10^6)/(c*10^3*log(10^3)) = 10^(6) * 6/ (10^(3) * 3) = 2*10^3 = 2000 sek = 33 min (där vi bakade in log_2 till log_10 i basen c som förkortas bort.)
  På samma sätt för t(10^9) = 9*10^9/(3*10^3)=3*10^6= 3000000 sek = 35 dagar.
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  A: t(n) = n
  B: t(n) = cnlog(n)
  Vi vet att vid B t(10) = 1 sek, det ger t(10) = c10log(10) vilket get c = 1/(10log(10)) --> c = 1/10 (vid log_10)
  t_B(n) > n 
  1/10n log(n) > n
  log(n)>10
  n>10^10   
  alltså mycket stora n (n > 10 miljarder). 
"""
