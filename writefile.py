prompt = input("Type a message: ")

#write message
with open('/home/jnunez/Desktop/testwrite.txt','w') as somefile1:
  somefile1.write(prompt)

