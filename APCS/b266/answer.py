def make_array():
  big_array = []
  small_array = []
  for m in range(10):
    small_array = []
    for n in range(10):
      small_array.append(0)
    big_array.append(small_array)

  return big_array

def overturn(big_array):
  new_array = make_array()
  for i in range(R):
    for j in range(C):
      new_array[R-i-1][j] = big_array[i][j]
  return new_array

def spin(big_array):
  new_array = make_array()
  for i in range(R):
    for j in range(C):
      new_array[C-j-1][i] = big_array[i][j]
  return new_array

R,C,M = map(int, input().split())

big_array = make_array()
for i in range(R):
  big_array[i] =list(map(int, input().split())) 

number_M = list(map(int, input().split()))

for i in range(len(number_M)):
  N = 0
  if number_M[len(number_M)- i - 1] == 0 :
    big_array = spin(big_array)
    N = R
    R = C
    C = N
  else:
    big_array = overturn(big_array)

print(R , end = ' ')
print(C)
for i in range(R):
  for j in range(C):
    print(big_array[i][j], end ='\n' if j == C-1 else ' ')
