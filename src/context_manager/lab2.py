# lab2
# Zadanie polega wykorzystaniu context managera jako timera. Tak uzupełnij poniższa klasę aby przeszedł test
# /tests/context_manager/test_lab2.py
import time


class Timer:

     def __enter__(self):
         self.time = time.perf_counter()
         return self

     def __exit__(self, exc_type, exc_val, exc_tb):
         self.time = round(time.perf_counter() - self.time,0)





