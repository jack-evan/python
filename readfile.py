
with open('/home/jnunez/Desktop/testwrite.txt','r') as open_file:
  bookmark = open_file.readline()
  count = 0
  list = bookmark.split() 
  for i in list:
    count += 1
  print(count)






