import numpy as np
import time

class SortAlgorithms:
    def __init__(self):
        super()
        self.nums = []

    def generate_numbers(self, size=10):
        self.nums = np.random.randint(0, size, size)

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

    # O(n**2)
    def selection_sort(self, nums):
        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[min_index] > nums[j]:
                    min_index = j
            self.swap(nums, i, min_index)

    # O(n**2)
    def bubble_sort(self, nums):
        is_sorted = False
        for i in range(len(nums)-1, 0, -1):
            if is_sorted:
                break
            is_sorted = True
            for j in range(i):
                if nums[j+1] < nums[j]:
                    self.swap(nums, j+1, j)
                    is_sorted = False

    # O(n**2)
    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            j = i
            while j>0 and nums[j] < nums[j-1]:
                self.swap(nums, j, j-1)
                j -= 1

    # O(n**1.3)
    def shell_sort(self, nums):
        h = 1
        while h < len(nums)//3:
            h = 3*h+1
        
        while h >= 1:
            for i in range(h, len(nums)):
                j = i
                while j>=h and nums[j] < nums[j-h]:
                    self.swap(nums, j, j-h)
                    j -= h
            h = h // 3

    # O(n*log n)
    def merge_sort(self, nums):
        def merge(nums, l, m, h):
            if h-l > 1:
                merge(nums, l, l+(m-l)//2, m)
                merge(nums, m+1, (m+1)+(h-(m+1))//2, h)
            i, j = l, m+1
            aux = [0]*len(nums)
            aux[l:h+1] = nums[l:h+1]
            for k in range(l, h+1):
                if i > m:
                    nums[k] = aux[j]
                    j+=1
                elif j > h:
                    nums[k] = aux[i]
                    i+=1
                elif aux[i] < aux[j]:
                    nums[k] = aux[i]
                    i+=1
                else:
                    nums[k] = aux[j]
                    j+=1
        merge(nums, 0, len(nums)//2, len(nums)-1)

    def quick_sort(self, nums):
        def partition(nums, l, h):
            i, j = l, h+1
            v = nums[l]
            while True:
                i+=1
                while nums[i] < v and i!=h:
                    i+=1
                j-=1
                while nums[j] > v and j!=l:
                    j-=1
                if i >= j:
                    break
                self.swap(nums, i, j)
            self.swap(nums, l, j)
            return j

        def sort(nums, l, h):
            if l >= h:
                return
            j = partition(nums, l, h)
            sort(nums, l, j-1)
            sort(nums, j+1, h)

        sort(nums, 0, len(nums)-1)

a = SortAlgorithms()
for f in [a.selection_sort, a.bubble_sort, a.insertion_sort,\
    a.shell_sort, a.merge_sort, a.quick_sort_stl]:
    a.generate_numbers(10)
    print('-'*50)
    print(f.__name__.replace('_', ' ').capitalize())
    start_time = time.time()
    f(a.nums)
    print(a.nums)
    print('cost: ' + str(time.time()-start_time))