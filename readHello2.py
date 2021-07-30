file = open('JeongJae.txt',"rt") # rt는 reat text

while True:
    str = file.read(5) # 다섯글자만 읽기
    if not str:         # 더이상 읽을게 없으면
        break
    print(str, end='')
file.close()
