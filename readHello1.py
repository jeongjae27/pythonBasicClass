file = open('JeongJae.txt',"rt") # rt는 reat text

str = file.read()
print(str, end='')
file.close()