file = open('JeongJae.txt',"rt") # rt는 reat text

while True:
    str = file.readline() # 줄 단위로 읽기
    if str == '':         # 더이상 읽을게 없으면
        break
    print(str, end='')
file.close()
