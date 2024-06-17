def pattern_7(n):
  for i in range(5):
    for j in range(11):
      if(j<= 6-i or j >= 4+i):
        print("*", end=" ")
      else:
        print(" ", end=" ")

    print("\n")
pattern_7(5)