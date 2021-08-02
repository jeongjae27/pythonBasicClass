class Korean:
    country = 'Korea' # class 변수. 어떤 객체든 서로 공유가능

    def __init__(self, name, age, address): # 이건 객체변수. 
        self.name = name
        self.age = age
        self.address = address


man = Korean('Hong', 35, 'Seoul')
woman = Korean('Julie', 24, 'Seoul')

print(man.name)
print(Korean.country) # 클라스 변수 사용
print(man.country)    # 객체 이름으로도 접근 가능

print(woman.country)

# 즉, 객체변수는 각자 따로 쓰지만, class변수는 공유할 수 있다.

