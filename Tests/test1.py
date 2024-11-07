#problem collections.Counter()

from collections import Counter

#number of shoes
num_shoes = int(input())

#sizes of shoes
#shoe_sizes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
shoe_sizes = list(map(int, input().split()))

shoe_inventory = Counter(shoe_sizes)
print(shoe_inventory)

#number of customers
num_customers = int(input())

tot_earning = 0

#Shoes size and prices

for n in range(num_customers):
    size,price = map(int,input().split())
    
    #check if the shoe size is available
    if shoe_inventory[size] > 0:
        tot_earning += price
        
        shoe_inventory[size] -= 1
        

print("Total earning is", tot_earning)