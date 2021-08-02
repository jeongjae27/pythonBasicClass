class Korean:
    country = 'korea'

    @classmethod  # decorater(장식자). 특징) cls를 self처럼 사용. 이거 없으면 class변수를 여기서 사용 못함
    def trip(cls, country):
        if cls.country == country:
            print("국내여행입니다.")
        else:
            print("해외여행입니다.")


Korean.trip('korea')
Korean.trip('USA')