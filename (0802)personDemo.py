class Person:
    def who_am_i(self, name, age, tel, address): # class 속 함수는 메소드
        # self는 객체의 이름이 들어옴
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person() # boy라는 객체에 person()이라는 클래스를 넣은것
girl = Person()

boy.who_am_i('John', 15, '123-1234', 'toronto')
girl.who_am_i('Alice', 13, '321-3321', 'NY')

print(boy.name)
print(boy.age)
print(boy.tel)
print(boy.address)

print(girl.name)
print(girl.age)
print(girl.tel)
print(girl.address)