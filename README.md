# 나도 코딩 파이썬 : 11강 모듈

# 1. 모듈 정의
- 모듈 : 파이썬에서 함수나 클래스 같은 정보를 담고있는 파일을 의미
- 모듈화 : 작업에 필요한 것만 만드는 것
- 외부에 정리된 모듈을 끌어와서 사용

- import : 일반적으로 모듈을 끌어올때 사용
```
import theather_module  
theather_module.price(3)
theather_module.price_morinig(4)
theather_module.price_soldier(5)
->
3 명 가격은 30000원 입니다. (외부에 정의된 함수를 끌어온 것)
4 명 가격은 24000원 입니다.
5 명 가격은 20000원 입니다.
```

- as : 긴 이름의 모듈을 간단하게 재정의하여 사용
```
import theather_module as mv 
mv.price(3)
mv.price_morinig(4)
mv.price_soldier(5)
->
3 명 가격은 30000원 입니다.
4 명 가격은 24000원 입니다.
5 명 가격은 20000원 입니다.
```

- from import * : 모듈내 함수를 전부 가져오는 것을 의미(표현이 간단해짐)
```
from theather_module import * 
price(3)
price_morinig(4)
price_soldier(5)
->
3 명 가격은 30000원 입니다.
4 명 가격은 24000원 입니다.
5 명 가격은 20000원 입니다.
```

- from import : 모듈내 함수를 선별적으로 가져오는 방법
```
from theather_module import price_soldier, price_morinig
price_morinig(4)
price_soldier(5)
->
4 명 가격은 24000원 입니다.
5 명 가격은 20000원 입니다.
```

- from import as : 선별적으로 가져온 함수를 간단하게 표현하는 것
```
from theather_module import price_soldier as A
A(3)
->
3 명 가격은 12000원 입니다.
```

# 2. 패키지 

- 패키지 : 모둘들을 모아둔 집합을 의미

- import 를 사용할때 뒤에는 항상 모듈이나 패키지가 들어가야함
```
import travel.thailand 
trip_to = travel.thailand.Thailandpackage()
trip_to.detail()
```

- from import 의 경우 뒤에 class를 사용할 수 있음
```
from travel.thailand import Thailandpackage 
trip_to = Thailandpackage()
trip_to.detail()
```

# 3. 내장함수
파이썬 내에 내장되어 있는 함수(import를 사용하지 않는다)

- input : 사용자 입력을 받는 함수
```
language = input("무슨 언어를 좋아하시나요? ")
print("{0}은 아주 좋은 언어입니다!".format(language))
->
무슨 언어를 좋아하시나요? 자바스크립트
자바스크립트은 아주 좋은 언어입니다!
```

- dir: 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
```
import random
print(dir(random))
->
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```

# 4. 외장함수
기본적으로 import를 통해 불러서 사용하는 함수

### 1. glob : 경로 내의 폴더 / 파일 목록 조회
```
import glob
print(glob.glob("*.py")) # .py로 끝나는 모든 폴더를 조회
->
['11-1 모듈.py', '11-10 퀴즈 정답.py', '11-2 패키지.py', '11-5 패키지, 모듈 위치.py', '11-6 pip install.py', '11-7 내장함수.py', '11-9 퀴즈.py', 'byme.py', 'theather_module.py']
```

### 2. os : 운영체제에서 제공하는 기본 기능

```
import os


folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print("폴더를 삭제했습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print("폴더를 생성했습니다.")

->
경로 내 해당 폴더가 없는 경우 : 폴더를 생성했습니다.
경로 내 해당 폴더가 있는 경우 : 이미 존재하는 폴더입니다.
                              폴더를 삭제했습니다.
```

### 3. time : 시간 관련 함수

- .localtime() : 현지 시간을 알려주는 함수
- .strftime("%Y-%m-%d %H:%M:%S") : 보다 간단하게 시간을 출력하는 방법(대문자나 부호를 확실하게 입력해야함)
```
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
->
time.struct_time(tm_year=2022, tm_mon=8, tm_mday=31, tm_hour=12, tm_min=3, tm_sec=14, tm_wday=2, tm_yday=243, tm_isdst=0)
2022-08-31 12:03:14
```

### 4. datetime 
- 날짜를 보다 간단하게 출력하는 방법
- .date.today() : 오늘 날짜를 알려주는 함수

```
import datetime
print("오늘 날짜는", datetime.date.today())
->
오늘 날짜는 2022-08-31
```

### 5. timedelta
- 두 날짜 사이의 간격 측정
```
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days= 100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후
->
우리가 만난지 100일은 2022-12-09
```



