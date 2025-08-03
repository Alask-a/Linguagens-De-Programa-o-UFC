from typing import List, Callable

def filter_func(lst: List[int], predicate: Callable[[int], bool]) -> List[int]:
    """
    Função recursiva para filtrar elementos que satisfazem o predicado.
    """
    if not lst:
        return []
    head, *tail = lst
    if predicate(head):
        return [head] + filter_func(tail, predicate)
    else:
        return filter_func(tail, predicate)

def map_func(lst: List[int], func: Callable[[int], int]) -> List[int]:
    """
    Função recursiva para aplicar func a cada elemento da lista.
    """
    if not lst:
        return []
    head, *tail = lst
    return [func(head)] + map_func(tail, func)

def reduce_func(lst: List[int], func: Callable[[int, int], int], initial: int) -> int:
    """
    Função recursiva para reduzir a lista a um valor usando func.
    """
    if not lst:
        return initial
    head, *tail = lst
    return reduce_func(tail, func, func(initial, head))

def is_even(n: int) -> bool:
    return n % 2 == 0

def square(n: int) -> int:
    return n * n

def sum_func(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    pares = filter_func(numeros, is_even)
    quadrados = map_func(pares, square)
    soma = reduce_func(quadrados, sum_func, 0)
    
    print(f"Números originais: {numeros}")
    print(f"Números pares: {pares}")
    print(f"Quadrados dos pares: {quadrados}")
    print(f"Soma dos quadrados dos pares: {soma}")
