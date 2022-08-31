# 모듈화 : 작업에 필요한 것만 만드는 것
# 모듈: 파이썬에서 함수나 클래스 같은 정보를 담고있는 파일을 의미

# 일반적으로 모듈을 끌어오는 방법
import theather_module  
theather_module.price(3)
theather_module.price_morinig(4)
theather_module.price_soldier(5)

# 긴 모듈의 이름을 간단하게 재정의 하여 나타내는 방법
#import theather_module as mv 
#mv.price(3)
#mv.price_morinig(4)
#mv.price_soldier(5)

# from import * 로 더 간단하게 가져오는 방법(import *은 전부 가져온다는 것을 의미)
#from theather_module import * 
#price(3)
#price_morinig(4)
#price_soldier(5)


# from import 에서 선별적으로 함수를 가져오는 방법
#from theather_module import price_soldier, price_morinig
#price_morinig(4)
#price_soldier(5)

# from import 에서 선별적으로 가져온 함수를 간단하게 표현하는 것도 가능
from theather_module import price_soldier as A
A(3)
