print('안녕')
print(1111)

print('차은우'*100)

이름 = '슈퍼 에이전트 하이퍼 초필살 투명드래곤'
print(이름)
print('이름 : ' , 이름[0])

중고차 = ['K5', 'white', 5000]
print(중고차[1])

중고차2 = { 'brand' : 'BMW', 'model' : '520d'}
print(중고차2['brand'])

재고량 = 9
if 재고량 > 10 : 
    print('지금 주문 가능합니다.')
else : 
    print('주문이 불가능합니다.')


중고차재고 = ['K5', 'BMW', 'Tico']
if 'K5' in 중고차재고 : 
    print('K5는 있어용')


for i in range(0, 10) :
    print('BMW 있어용')

중고차들 = ['K5', 'BMW', 'Tico', 'SM']
for i in 중고차들 :
    print(i)


def 인사하기() : 
    print('안녕하세요 중고차 신뢰딜러 차은우입니다.')

인사하기()

def 모자(i) :
    print(i + 1)

모자(1)
모자(2)
모자(3)

