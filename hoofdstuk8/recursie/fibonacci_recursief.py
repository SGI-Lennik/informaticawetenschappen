import time

def fibonacci(index):
    # aandachtspunt 2: stop de recursie
    if index == 1 or index == 2:
        return 1
    else:
        # aandachtspunt 1: roep de functie op met andere argumenten
        return fibonacci(index-1) + fibonacci(index-2)

start = time.perf_counter()
print(fibonacci(20))
stop = time.perf_counter()
print("De berekening duurde: ", stop-start, "seconden")
