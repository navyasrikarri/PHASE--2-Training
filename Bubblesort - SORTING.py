def bubblesort(arr,pos):
  while pos>0:
  for i in range(pos):
    if arr[i]>arr[i+1]:
      arr[i],arr[i+1] = arr[i+1],arr[i]   
  pos-=1    
arr = [9,8,7,6,5,4,3,2,1] 
pos = len(arr)-1 
bubblesort(arr,pos)
print(arr)
