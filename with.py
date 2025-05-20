#With

filename = '/Users/HP/Downloads/resume%20(1).pdf'

try:
  file = open(filename, 'r')
  content = file.read()
  print(content)
finally:
  file.close()

  #Alternate way: easy way 

  filename = '/Users/HP/Downloads/resume%20(1).pdf'

  with open(filename, 'r' ) as file:
    content = file.read()
    print(content)
    