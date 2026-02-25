import time

def fibonacci(index):
    fibo_vorig = 1
    fibo_huidig = 1
    if index == 1 or index == 2:
        return fibo_huidig
    for n in range(3, index+1):
        # bereken de volgende term
        fibo_volgend = fibo_vorig + fibo_huidig
        # vorige twee termen schuiven een plaats op
        fibo_vorig = fibo_huidig
        fibo_huidig = fibo_volgend
    return fibo_volgend

start = time.perf_counter()
print(fibonacci(20))
stop = time.perf_counter()
print("De berekening duurde: ", stop-start, "seconden")