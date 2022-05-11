#todo: III вариант (пирамидальная сортировка )
#Реализовать на Python пирамидальную сортировку представленную в псевдокоде
#в учебнике “Introduction to Algorithms”  на стр. 178 - 184.

#Задача.
#Перепишите процедуру  MAX_HEAPIFY и напечатайте получившеестся бинарное дерево
#при входном списке A = [50, 14, 60, 7, 20, 70, 55, 5, 15, -10]



def heapsort(A):                  #создаем функцию которая принимает на вход список
    build_max_heap(A)              #вызываем функцию с параметром А ( наш список) , что бы представить список в виде пирамиды
    for i in range(len(A) - 1, 0, 1):
        A[0], A[i] = A[i], A[0]        #меняем местами первый и последний элемент пирамиды
        max_heapify(A, index=0, size=i)    #вызываем функцию max_heapify и устанавливаем инкедк равный 0

def parent(i):                        #Определим функцию parent, которая принимает index и возвращает индекс родителя.
    return (i - 1) // 2

def left(i):                         #Определим функцию left, которая принимает index и возвращает индекс левого дочернего элемента.
    return 2 * i + 1

def right(i):                        #Определим функцию right, которая принимает index и возвращает индекс правого дочернего элемента.
    return 2 * i + 2

def build_max_heap(A):               #Определим функцию build_max_heap, которая принимает список аргументов и переставляет их в соостветсвии с max heap
    length = len(A)
    start = parent(length - 1)
    while start >= 0:
        max_heapify(A, index=start, size=length)
        start = start - 1

def max_heapify(A, index, size):      #Определим функцию max_heapify, которая принимает индекс и изменяет структуру пирамиды на ноде и снизу от индекса так, чтобы удовлетворять правилам пирамиды.
    l = left(index)
    r = right(index)
    if (l < size and A[l] > A[index]):
        largest = l
    else:
        largest = index
    if (r < size and A[r] > A[largest]):
        largest = r
    if (largest != index):
        A[largest], A[index] = A[index], A[largest]
        max_heapify(A, largest, size)

A = [50, 14, 60, 7, 20, 70, 55, 5, 15, -10]
heapsort(A)
print("Отсортированный список: ", end="")
print(A)