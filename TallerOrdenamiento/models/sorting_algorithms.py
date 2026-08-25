import sys

sys.setrecursionlimit(2000000)


# --- 1. BUBBLE SORT ---
def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Descendente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# --- 2. SHELL SORT ---
def shell_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] < temp:  # Descendente
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# --- 3. QUICKSORT (In-place descendente con pivote central) ---
def quick_sort(arr: list[int]) -> list[int]:
    def _quicksort(items, low, high):
        if low < high:
            p = _partition(items, low, high)
            _quicksort(items, low, p - 1)
            _quicksort(items, p + 1, high)

    def _partition(items, low, high):
        mid = (low + high) // 2
        items[mid], items[high] = items[high], items[mid]
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] >= pivot:  # Mayor o igual a la izquierda (Descendente)
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quicksort(arr, 0, len(arr) - 1)
    return arr


# --- 4. RADIX SORT ---
def _counting_sort_desc(arr: list[int], exp: int):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Acumulación inversa para orden descendente
    for i in range(8, -1, -1):
        count[i] += count[i + 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        _counting_sort_desc(arr, exp)
        exp *= 10
    return arr


# --- 5. BINARY TREE SORT (Iterativo para prevenir desbordes) ---
class TreeNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


def binary_tree_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    root = TreeNode(arr[0])
    for val in arr[1:]:
        curr = root
        while True:
            if val <= curr.key:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right

    # Recorrido inverso (Derecha -> Raíz -> Izquierda) para orden descendente
    result = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        result.append(curr.key)
        curr = curr.left

    return result