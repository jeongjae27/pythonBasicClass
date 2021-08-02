#class Candy:
#    def set_info(self, shape, color):
#        self.shape = shape
#        self.color = color

class Candy(): 
    def __init__(self, shape, color): # 더블언더바(던더라고 부름) init == 생성자
        self.shape = shape
        self.color = color


#satang = Candy()
#satang.set_info('circle', 'brown')

satang = Candy('circle', 'brown') # 객체에 넣고 메소드를 사용하는걸 한번에 가능케함 

print(satang.shape)
print(satang.color)


class Sample():
    def __del__(self): # 소멸자. 별로 안써서 몰라도 됨
        print('has been closed')

sample = Sample()
del sample              # 객체가 자동으로 삭제됨

class USB:
    def __init__(self, capacity):
        self.capacity = capacity
    
    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(64)
usb.info()



class Service():
    def __init__(self,service):
        self.service = service
        print('{}service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{}service가 종료되었습니다.'.format(self.service))

s = Service('길 안내')
del s 