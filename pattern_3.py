def pattern_3(n):
  n+=1
  for i in range(n):
    for j in range(n):
      if (j>=n-i):
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print("\n")

pattern_3(5)