try:
  new_file=open("text_file.txt","w")
  print("file opened")
  try:
    new_file.write("Hi! My name is Chandana Penumuchu")
    print("data written" )
    new_file.close()
    print("file closed")
  except:
    print("Error in writing data to the file")
except:
  print("error in opening file")
