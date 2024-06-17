def pattern_4(n):
  for i in range(n):
    for j in range(n):
      if (j<=(n-1)-i):
        print("*",end=" ")
      else:
        print(" ",end=" ")
    print("\n")

pattern_4(5)