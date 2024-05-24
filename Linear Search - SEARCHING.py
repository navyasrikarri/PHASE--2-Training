arr = [5,14,7,19,100] 
target = 19 
pos = -1 
for i in range(len(arr)):
  if arr[i] == target:
    pos = i 
    break 
if pos == -1:
  print("Element Not Found") 
else:
  print("Element not found",pos) 
