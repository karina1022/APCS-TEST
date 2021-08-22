# Inout R, C, M
R,C,M = map(int, input().split(" "))

## 1. 先完成 10x10, 0 矩陣
# 1-1. 矩陣賦值
def make_array():
  big_array = []
  small_array = []
  for m in range(10):
    small_array = []
    for n in range(10):
      small_array.append(0)

    big_array.append(small_array)
  
  return big_array

big_array = make_array()


## 2. 才做 input 給矩陣值
for i in range(R):
  # Note:
  # 你看第 2 行，map return 出來的值，多半用幾個變數接住了，例如 R,C,M = map(int, input().split(" "))
  # 在這個例子裡面，你的 map return 值應該有好幾個，但 big_array[i] 其實是 1 個變數而已，
  # 所以你整個 map 應該要用 list 包起來，他會有又便這種效果： big_array[i] = [xxxxxxx]
  big_array[i] =list(map(int, input().split(" "))) 

number_M = list(map(int, input().split(" ")))

# 逆翻 ( 寫成模組 )
# 1. 把 10x10 array 這一段，收斂成 function => array = make_array(10, 10)
# 2. X = make_array(10, 10)
# 3. 換位 ( 走過一次 B 矩陣 )
# 4. 換位公式

def overturn():
  new_array = make_array()
  for i in range(R):
    for j in range(C):
      new_array[R-i-1][j] = big_array[i][j]
  return new_array 

# 逆旋 ( 寫成模組 )

def spin():
  new_array = make_array()
  for i in range(R):
    for j in range(C):
      new_array[C-j-1][i] = big_array[i][j]
  return new_array


for i in range(len(number_M)):
  N = 0
  if number_M[i] == 0 :
    big_array = spin()
    N = R
    R = C
    C = N
    print(big_array)

  if number_M[i] == 1 :
    big_array = overturn()
    print(big_array)

print(R , end = ' ')
print(C)
for i in range(10):
  for j in range(10):
    if big_array[i][j] != 0:
       print(big_array[i][j], end ='\n' if j == C-1 else ' ')
       # print(B[i][j], end='\n' if j == C - 1 else ' ')

## TODOs
# 1. 你需要 print 新的 RC
# 2. 答案矩陣要合乎大小
# 2-1. 參考：make_array
# 2-2. 你不是要針對答案建立一個矩陣喔！你只是要從 big_array 把答案印出來而已 ( 跳過 0 )
# 2-1. https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/362821/ 
