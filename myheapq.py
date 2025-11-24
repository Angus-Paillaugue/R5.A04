from typing import List, Any

class MyHeapQ:
    @staticmethod
    def check_heap(arr: List[Any]) -> bool:
        """Check if the list satisfies the heap property"""
        size = len(arr)
        for i in range((size - 2) // 2 + 1):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < size and arr[i] > arr[left]:
                return False
            if right < size and arr[i] > arr[right]:
                return False
        return True

    @staticmethod
    def heapify(arr: List[int]) -> None:
        """Transform list into a heap, in-place"""
        size = len(arr)
        for i in range((size - 2) // 2, -1, -1):
            index = i
            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                smallest = index

                if left < size and arr[left] < arr[smallest]:
                    smallest = left
                if right < size and arr[right] < arr[smallest]:
                    smallest = right

                if smallest == index:
                    break

                arr[index], arr[smallest] = arr[smallest], arr[index]
                index = smallest

    @staticmethod
    def heappop(arr: List[int]) -> int:
        """Pop and return the smallest item from the heap"""
        if not arr:
            raise IndexError("pop from empty heap")
        min_value = arr[0]
        arr[0] = arr[-1]
        arr.pop()
        size = len(arr)
        index = 0
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and arr[left] < arr[smallest]:
                smallest = left
            if right < size and arr[right] < arr[smallest]:
                smallest = right

            if smallest == index:
                break

            arr[index], arr[smallest] = arr[smallest], arr[index]
            index = smallest

        return min_value

    @staticmethod
    def heappush(arr: List[int], value: int) -> None:
        """Push a new item onto the heap"""
        arr.append(value)
        index = len(arr) - 1
        while index > 0:
            parent = (index - 1) // 2
            if arr[parent] <= arr[index]:
                break
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent

def my_tri_tas(tas: List[int]) -> List[int]:
    """Sort a list using heap sort"""
    h: List[int] = []
    for value in tas:
        MyHeapQ.heappush(h, value)
    return [MyHeapQ.heappop(h) for _ in range(len(h))]
