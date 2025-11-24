from myheapq import MyHeapQ, my_tri_tas
import numpy as np
import time
import matplotlib.pyplot as plt
import heapq
from typing import List

def tri_tas(tas: List[int]) -> List[int]:
  """Sort a list using the built-in heapq module"""
  h: List[int] = []
  for value in tas:
    heapq.heappush(h, value)
  return [heapq.heappop(h) for _ in range(len(h))]

def tests(nb_tests: int = 10) -> None:
  """Run tests to verify heap operations"""
  for _ in range(nb_tests):
    my_list = np.random.randint(0, 100, size=1000).tolist()
    MyHeapQ.heapify(my_list)
    assert MyHeapQ.check_heap(my_list), "The list is not a valid heap after heapify."
    value_to_push = 5
    MyHeapQ.heappush(my_list, value_to_push)
    assert MyHeapQ.check_heap(my_list), "The list is not a valid heap after heappush."
    MyHeapQ.heappop(my_list)
    assert MyHeapQ.check_heap(my_list), "The list is not a valid heap after heappop."

def compare_sorting_algorithms():
  """Compare the performance of the two heap sort implementations"""
  listen = [10, 20, 50, 100, 200, 500, 1_000, 10_000]
  chrono = {}
  chrono["tri_tas"] = np.zeros(len(listen))
  chrono["my_tri_tas"] = np.zeros(len(listen))

  for k, n in enumerate(listen):
      tab = np.random.randint(0, 100, size=n)
      t1 = time.perf_counter()
      tri_tas(tab.tolist())
      t2 = time.perf_counter()
      chrono["tri_tas"][k] = t2 - t1
      t1 = time.perf_counter()
      my_tri_tas(tab.tolist())
      t2 = time.perf_counter()
      chrono["my_tri_tas"][k] = t2 - t1

  plt.figure(1)
  print(chrono)
  plt.plot(listen, chrono["tri_tas"], "o", label="tri_tas")
  plt.plot(listen, chrono["my_tri_tas"], "o", label="my_tri_tas")
  plt.xlabel("Taille du tableau")
  plt.ylabel("Temps (s)")
  plt.title("Comparaison des résultats")
  plt.legend()
  plt.show()

if __name__ == "__main__":
  tests()
  compare_sorting_algorithms()
