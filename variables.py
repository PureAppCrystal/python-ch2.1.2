# 변수 이름은 문자, 숫자, _ 로 구성해야 한다.
import keyword


friend = 1
a = 10
my_name = '배상훈'
_yourNname = 'what'
member1 = '도우넛'
member2 = '크라잉넛'

# 에러
# $ㄹ갸둥 = 2
# ㅁ! = 1
# 1뮻 = 10

# 에러 : 예약어는 사용할 수 없다.
# def = 10

print(keyword.kwlist)

#한글이름의 변수도 가능하다.

가격1 = 2000
print(가격1 - 200)


# 치한문의 예
a = 1
b = a + 1
print(a, b, sep=',')
e = 3
f = 5 + 2
e, f = 3, 7
print(e, f)

# 하나의 값을 여러 변수에 대입하기
x = y = z = 1

# 값 교환
f, e = e, f
print(e, f)

#동적 타이핑
a = 1
print(type(a))
a = 'hello'
print(type(a))

