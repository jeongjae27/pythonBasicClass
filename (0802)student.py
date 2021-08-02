def student_info(name, department, professor, phone, address, grade):
    print(name)
    print(department)
    print(professor)
    print(phone)
    print(address)
    print(grade)


name1 = 'Emily'
department1 = 'Computer engineering'
professor1 = 'James'
phone1 = '010-0000-0000'
address1 = 'Seoul'
grade1 = 'A'

student_info(name1, department1, professor1, phone1, address1, grade1)

name2 = 'Alice'
department2 = 'Chemical engineering'
professor2 = 'David'
phone2 = '010-1111-1111'
address2 = 'Busan'
grade2 = 'B'

student_info(name2, department2, professor2, phone2, address2, grade2)

# 학생이 늘어날때마다 해야하는 작업이 너무 많음

# class와 객체를 사용하면, 붕어빵기계처럼 하나의 클래스에 다른 객체를 넣을 수 있다. (인스턴스 == 객체)
# 붕어빵기계 == 클래스 // 붕어빵 == 객체

