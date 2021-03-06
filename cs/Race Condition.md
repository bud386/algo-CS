# Race Condition

race condition이란 두 개 이상의 프로세스가 공통 자원을 병행적으로(concurrently) 읽거나 쓰는 동작을 할 때, 공용 데이터에 대한 접근이 어떤 순서에 따라 이루어졌는지에 따라 그 실행 결과가 같지 않고 달라지는 상황을 말한다. Race의 뜻 그대로, 간단히 말하면 경쟁하는 상태, 즉 두 개의 스레드가 하나의 자원을 놓고 서로 사용하려고 경쟁하는 상황을 말한다.

경쟁 프로세스의 경우, 세 가지 제어 문제에 직면한다. **Mutual exclusion, deadlock, starvation**이다.

1. Mutual exclusion

Race condition을 막기 위해서두 개 이상의 프로세스가 공용 데이터에 동시에 접근을 하는 것을 막아야 한다. 즉, 한 프로세스가 공용 데이터를 사용하고 있으면 그 자원을 사용하지 못하도록 막거나, 다른 프로세스가 그 자원을 사용하지 못하도록 막으면 이 문제를 피할 수 있다. 이것을 상호 배제(mutual exclusion)라고 부른다.

1. deadlock

프로세스가 각자 프로그램을 실행하기 위해 두 자원 모두에 엑세스 해야 한다고 가정할 때 프로세스는 두 자원 모두를 필요로 하므로 필요한 두 리소스를 사용하여 프로그램을 수행할 때까지 이미 소유한 리소스를 해제하지 않는다.

1. starvation

두 개 이상의 작업이 서로 상대방의 작업이 끝나기만을 기다리고 있기 때문에 결과적으로는 아무것도 완료되지 못하는 상태





# 메모리 계층 구조

메모리 계층 구조(Memory hierarchy) 란 메**모리를 필요에 따라 여러가지 종류로 나누어 둠을 의미**합니다. 이때 필요란 대부분의 경우 CPU가 메모리에 더 빨리 접근하기 위함입니다.

메모리를 필요에 따라 여러가지 종류로 나누어 둠을 의미한다[[1\]](https://ko.wikipedia.org/wiki/메모리_계층_구조#cite_note-1). 이때 필요한 대부분의 경우 [CPU](https://ko.wikipedia.org/wiki/중앙_처리_장치)가 메모리에 더 빨리 접근하기 위함이다.

![img](https://upload.wikimedia.org/wikipedia/commons/c/c6/%EB%A9%94%EB%AA%A8%EB%A6%AC%EA%B3%84%EC%B8%B5%EA%B5%AC%EC%A1%B0%EA%B7%B8%EB%A6%BC1.png)

1. 레지스터와 캐시는 CPU 내부에 존재. 당연히 CPU는 아주 빠르게 접근할 수 있다.
2. 메모리는 CPU 외부에 존재한다. 레지스터와 캐시보다 더 느리게 접근 할 수 밖에 없다.
3. 하드 디스크는 CPU가 직접 접근할 방법조차 없다. CPU가 하드 디스크에 접근하기 위해서는 하드 디스크의 데이터를 메모리로 이동시키고, 메모리에서 접근해야 한다. 아주 느린 접근 밖에 불가능하다.

### 필요성

- **비용적인 측면** : 레지스터, 캐시, 메모리, 하드 디스크는 하드웨어적으로 만들어지는 방법이 다를 때가 많다. 그리고 메모리 구조에서 상층에 속할 수록 더 비싸다.
- **자주 쓰이는 데이터는 계속 쓰임(참조의 지역성)** : 자주 쓰이는 데이터는 계속 자주 쓰이고, 자주 쓰이지 않는 데이터는 계속 자주 쓰이지 않는다. 이를 이용해서 운영체제나 CPU는 자동으로 자주 쓰이는 데이터, 또는 자주 쓰일 것 같은 데이터를 메모리에서 캐시로 읽어온다. 자주 쓰이는 데이터는 전체 데이터 양에 비해 작은 양이기때문에, 캐시는 메모리보다 더 작아도 된다. 메모리와 하드 디스크의 관계도 마찬가지이다.
- **속도적인 측면** : CPU와 가까이 있는 레지스터가 가장 빠르게 접근가능하고 밑으로 내려갈수록 접근 속도가 느려짐



**지역성**

시간적 지역성과 공간적 지역성이 있다.

좋은 **시간적 지역성**을 갖는다: 접근한 데이터에 조만간 접근할 확률이 크다.(어떤 항목이 참조되면, 곧바로 다시 참조되기 쉽다,)

좋은 **공간적 지역성**을 갖는다: 접근한 데이터 근처에 있는 데이터에 접근할 확률이 크다.(어떤 항목이 참조되면 근처에 있는 다른 ㅏ항목들도 참조될 가능성이 높다.)

 

간단히 이야기해서 모든 데이터에 접근할 확률은 동일하지 않고, 따라서 이 특성을 잘 이용하여 캐싱한다면 피라미드의 아래쪽에 위치한 메모리에 접근하는 횟수보다 위쪽에 접근하는 횟수가 많아서 전체적으로 빠른 속도를 얻을 수 있다.

#### 종류

1. 레지스터

   컴퓨터의 프로세서 내에서 자료를 보관하는 아주 빠른 기억 장소이다. 일반적으로 현재 계산을 수행중인 값을 저장하는 데 사용된다.

   

2. 캐시

   CPU 캐시는 메인 메모리에서 가장 자주 사용되는 위치의 데이터를 갖고 있는, 크기는 작지만 빠른 메모리이다. 프로세서가 메인 메모리를 읽거나 쓰고자 할 때, 그 주소에 해당하는 데이터가 캐시에 존재한다면 데이터를 캐시에서 직접 읽어서 메모리 접근 시간을 아낄수 있다.

   

3. 주기억장치(메인메모리, 1차기억장치)

   CPU에서 직접 접근이 가능한 메모리

   - RAM(Random Access Memory, 임의접근 기억장치)

     사용자가 자유롭게 내용을 읽고 쓰고 지울 수 있는 기억장치. 컴퓨터가 켜지는 순간부터 CPU는 연산을 하고 동작에 필요한 모든 내용이 전원이 유지되는 내내 이 기억장치에 저장. 전원이 꺼지면 기억된 내용이 모두 사라지는 휘발성 메모리.

     RAM은 어느 위치에 저장된 데이터든지 접근(읽기 및 쓰기)하는 데 동일한 시간이 걸리는 메모리이기에 ‘랜덤(Random, 무작위)’이라는 명칭이 주어졌습니다.

   - ROM(read only memory)

     ROM은 기억된 내용을 읽을 수만 있는 기억장치로서 일반적으로 쓰기는 불가능 합니다. 전원이 실제로 꺼져도 기억된 내용이 지워지지않는 비휘발성 메모리입니

     변경 가능성이 희박한 시스템 소프트웨어를 기억시키는데 이용합니다.

   - Flash Memory

     플래시 메모리는 비휘발성 반도체 저장장치다. 전기적으로 자유롭게 재기록이 가능하다.

4. 보조기억장치(2차기억장치)

   CPU에서 직접 접근이 불가능한 메모리. 접근하려면 디바이스 드라이버와 시스템 콜을 통하여 기억장치의 특정 위치의 내용을 주기억장치로 로드(Load)한 뒤 읽어야 한다.

   SSD, HDD, CD, 자기테이프, 광디스크 등이 존재합니다.

   - SSD(Solid State Drive)

     솔리드 스테이트 드라이브는 순수 전자식으로 작동하므로 기계식인 하드 디스크 드라이브(HDD)의 문제인 긴 탐색 시간, 반응 시간, 기계적 지연, 실패율, 소음을 크게 줄여 준다.

   - HDD(Hard Disk Drive)

     하드 디스크(hard disk)는 비휘발성, 순차접근이 가능한 컴퓨터의 보조 기억장치이다.

___

## **캐시**

'캐싱한다'는 말이 있다. 이 말은 무언가를 저장한다는 말이고, 그 무언가는 당연히 앞으로 또 찾을 가능성이 높은 것을 말한다. 이런 맥락에서 캐시를 이해해볼 수 있을 것 같다. 캐시는 메모리처럼 무언가를 저장하는 공간인데, 그 무언가란 앞으로 또 찾을 가능성이 높은 것이다.

 

예를 들어 레지스터와 메인메모리, 로컬 디스크가 있다고 해보자. 로컬 디스크에 있는 데이터 중 앞으로 찾을 가능성이 높은 데이터를 메인 메모리에 저장하고, 메인 메모리에 있는 데이터 중 앞으로 찾을 가능성이 높은 데이터를 레지스터에 저장한다. 이때 메인 메모리는 로컬 디스크를 위해 캐시 메모리라고 볼 수 있고, 레지스터는 메인 메모리를 위한 캐시 메모리라고 볼 수 있다. 일반화하면 메모리 계층구조에서 레벨 k에 있는 보다 빠르고 더 작은 저장장치는 레벨 k+1에 있는 더 크고 더 느린 저장장치를 위한 캐시 서비스를 제공한다.

 

이것만으로는 어딘가 부족하다. 아무리 캐싱이 되었다고 하더라도 처음에 살펴본 그림에서 피라미드의 가장 밑 메모리에만 있는 데이터가 필요하다면? 캐싱은 아무 소용 없고 피라미드 가장 밑 메모리의 속도를 따라 결국 속도도 느리지 않을까? 모든 데이터에 접근할 확률이 동일하다면 캐싱은 쓸모 없을 것이다. 하지만 컴퓨터 프로그램은 지역성이라는 특성을 띤다.

___



메모리는 계층구조를 이루고 있고, 계층구조의 핵심은 캐싱이며, 캐싱이 가능한 이유는 프로그램이 지역성을 띠기 때문이다. 덕분에 우리는 속도가 빠르고 용량도 큰 메모리를 쓰는 것 같은 착각을 느낄 수 있다. 속도는 피라미드 위의 메모리에 근접하고, 용량은 피라미드 아래의 메모리에 근접하다.





# 메모리 단편화

RAM에서 메모리의 공간이 작은 조각으로 나뉘어져 사용가능한 메모리가 충분히 존재하지만 할당(사용)이 불가능한 상태

### 내부 단편화

- 메모리를 할당할 때 프로세스가 필요한 양보다 더 큰 메모리가 할당되어서 프로세스에서 사용하는 메모리 공간이 낭비 되는 현상

  4k를 할당, 하지만 1k만 사용하면 3k 만큼의 내부 단편화 발생

### . 외부 단편화

- 메모리가 할당 및 해제 작업의 반복으로 작은 메모리가 중간중간에 존재 중간중간에 생긴 사용하지 않는 메모리가 존재해서 총 메모리 공간은 충분하지만 실제로 할당할 수 없는 상황

- 여유 공간이 여러 조각으로 나뉘는 현상

  ex) 메모리 시작부터 8, 16 mb 프로세스 할당, 첫번째 종료하면 메모리 시작 주소부터 8mb 공간이 발생

## 가상메모리란?

메인 메모리보다 훨씬 큰 기억공간인 디스크를 가상의 메모리 공간으로 이용하는 기법

실제 메모리 크기와 상관 없이 메모리를 이용할 수 있도록 가상의 메모리 주소를 사용하는 방법이다.

가상 메모리의 핵심은 필요한 부분만 메모리에 적재(**부분적재**)하는 것!

가상 메모리를 사용하면 다음과 같은 이점이 있다.

- 실제 메모리(RAM) 크기 보다 더 큰 공간을 사용할 수 있다. (보조 기억장치 공간 사용)
- 가상의 주소 공간을 사용하여 논리적인 연속성을 제공해준다.
- 물리 메모리 주소 공간을 알 필요가 없어진다.

## 메모리 파편화 문제 해결 방법

1. 페이징(Paging)기법 - 가상메모리사용, 외부 단편화 해결, 내부 단편화 존재

   ___

   **요구페이징**

   현재 필요한 페이지만 메모리에 올리는 것을 요구페이징이라고 한다.

   대부분의 프로그램이 프로그램 전체가 적제되지 않아도 **사용 가능하다**는 특징을 이용해서, **필요한 페이지**만 저장공간에 적제하고, 다른 페이지는 **보조기억장치**에 적제해서 사용한다.

   ___

   

   페이징이란 고정 크기로 분할된 페이지(page)를 통해 가상 메모리를 관리하는 기법이다.

   - 페이지(page) : 가상 메모리를 고정 크기로 나눈 블록
   - 프레임(frame) : 실제 메모리를 페이지와 같은 크기로 나눈 블록 (= 페이지 프레임)

   ___

   - 보조기억장치를 이용한 가상메모리를 같은 크기의 블록으로 나눈 것을 페이지라고 하고 RAM을 페이지와 같은 크기로 나눈 것을 프레임이라고 할 때,
   - 사용하지 않는 프레임을 페이지에 옮기고, 필요한 메모리를 페이지 단위로 프레임에 옮기는 기법.

   

   - 페이지와 프레임을 대응시키기 위해 page mapping과정이 필요해서 paging table을 만든다.

   - 페이징 기법을 사용하면 연속적이지 않은 공간도 활용할 수 있기 때문에 외부 단편화 문제를 해결할 수 있다.

   - 대신 페이지 단위에 알맞게 꽉채워 쓰는게 아니므로 내부 단편화 문제는 여전히 있다.
     - 페이지 단위를 작게하면 내부 단편화 문제도 해결할 수 있겠지만 대신 page mapping 과정이 많아지므로 오히려 효율이 떨어질 수 있다.

2. 세그멘테이션(Segmentation)기법 - 가상메모리사용, 내부 단편화 해결, 외부 단편화 존재