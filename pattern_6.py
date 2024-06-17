def pattern_6(n):
  k = 1
  for i in range(6):
    for j in range(10):
      if(j>= 6-i and j <= 4+i and k == 1):
        print("*", end=" ")
        k=0
      else:
        print(" ", end=" ")
        k=1

    print("\n")


pattern_6(5)