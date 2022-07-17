# 패키지 : 모둘들을 모아둔 집합을 의미

#import travel.thailand  # import 를 사용할때 뒤에는 항상 모듈이나 패키지가 들어가야한다.(class나 함수가 바로 올 수 없다.)
#trip_to = travel.thailand.Thailandpackage()
#trip_to.detail()

#from travel.thailand import Thailandpackage # from import 의 경우 뒤에 class를 사용할 수 있다.
#trip_to = Thailandpackage()
#trip_to.detail()

from travel import vietnam
trip_to = vietnam.Vietnampackage()
trip_to.detail()