from timeit import default_timer as timer
import heapq as hs
list1 = ['4','10','11','5','73','5','1'] 
list2 = ['4','10','11','5','73','5','1'] 

start = timer()
list1.sort()
print(list1)
end = timer()
print('Dla sortowania szybkiego:', end-start )

start = timer()
hs.heapify(list2)
print(list2)
end = timer()
print('Dla sortowania kopcem:', end-start )
