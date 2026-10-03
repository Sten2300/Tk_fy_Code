#Tower of Hanoi

def bricklek(f: str, t: str, h: str, n: int) -> list[str]:
    """Exc7: Returns a list of string instructions for how to move the tiles"""
    #Goal: move n-1 to h, move bottom plate to t, move n-1 to t.
    if n==1: # bas move, från current pos till current goal
        print(f'{f}->{t}')
        return
    bricklek(f,h,t,n-1) # flyttar n-1 diskar till hjälp stav som mål
    print(f'{f}->{t}') # flyttar bottenplattan till målet
    bricklek(h,t,f,n-1)  # flyttar n-1 diskar till orginal mål stav.

    
    
