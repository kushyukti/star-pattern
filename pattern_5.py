# def pattern_5(n):
#   for i in range(n):
#     for j in range(n):
#       if (j>=((6)-i) and j<=((4)+i)):
#         print("*",end=" ")
#       else:
#         print(" ",end=" ")
#     print("\n")

# pattern_5(5)


rows = 5
k = 2 * rows - 2     # Here, the K is used for number of spaces    
# Here, we are declaring an outer loop to handle number of rows  
for i in range(0, rows):    
      # Here, we are declaring an inner loop to handle number of spaces  
    for j in range(0, k):    
        print(end=" ")    
    k = k - 2      # Here, we are decrementing the k value after each iteration    
# Here, we are declaring an for loop to handle number of rows      
for j in range(0, i + 1):    
        print("* ", end="")   # Here, we are printing the star pattern    
print("")