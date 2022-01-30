"""
Given two array of integers, merge the arrays in the following manner. The new array will contain the 1st element of array1, then 1st element of array2, then 2nd element of array1, then 2nd element of array2 and so on. The two arrays can be of any size. If any array is over then the remaining elements of the remaining array are copied into the new array.
Input-> [1,3,5,7],[2,4]
Output-> [1,2,3,4,5,7]
"""

ls1 = [1,3,5,7]
ls2 = [2,4]
ln1 = len(ls1)
ln2 = len(ls2)
nw_ls = []
for i in range(0,ln1):
  e1 = ls1[i]
  nw_ls += [e1]
  for j in range(0,ln2):
    e2 = ls2[j]
    if(i==j):
      nw_ls += [e2]
print(nw_ls)
