m = int(input('Enter the length of first sequence: '))
n = int(input('Enter the lenght of second sequence: '))
seq1 = []
seq2 = []
for i in range(m):
  ele = input(f'Enter element to complete the sequence 1 of length {m}: ')
  seq1 = seq1 + [int(ele)]

print(f'The first seq is {seq1}')

for i in range(n):
  ele = input(f'Enter element to complete the sequence 2 of length {n}: ')
  seq2 = seq2 + [int(ele)]

print(f'The second seq is {seq2}')

max = 10

def circular_conv(s1, s2):
  # m = len(s1)
  # n = len(s2)

  if m == n:
    mat1 = s1
    mat2 = s2
    max = m
  elif m > n:
    mat1 = s1
    mat2 = s2
    max = m
  else:
    mat1 = s2
    mat2 = s1
    max = n

  print(f'{max}')
  if max < 4 | max > 10:
    return -1

  else:
    folded_arr_zeros = [[0 for i in range(max)] for j in range(max)]
    column_matrix = [0]*max

    if len(mat2) < max:
      for i in range(len(mat2)):
        column_matrix[i] = mat2[i]
      mat2 = column_matrix
      print(f'{column_matrix}')

    conv_result = []

    for i in range(max):
      arr2 = mat1[3:len(s1)-1-i:-1] + mat1[0:len(s1)-i]
      if i == 0:
        folded_arr_zeros[i] = mat1
      else:
        folded_arr_zeros[i] = arr2
    print(f'The folded sequence is: {folded_arr_zeros}')
  
  for i in range(max):
    result = 0
    for j in range(max):

      result += folded_arr_zeros[i][j]* mat2[j]
      #print(f'i:{i}; j:{j}; m1={folded_arr_zeros[i][j]}; m2={s2[j]} ; result = {result}')
    
    conv_result = conv_result + [result]
  print(conv_result)
  #print(folded_arr_zeros)

circular_conv(seq1, seq2)