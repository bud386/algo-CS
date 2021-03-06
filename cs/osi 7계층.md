# osi 7계층

국제표준화기구에서 만든 네트워크 통신의 7단계 과정

계층을 나눈 이유는 통신이 일어나는 과정이 단계별로 파악할 수 있기 때문

계층을 분리함으로서 각 계층은 독립적인 역할을 할 수 있다. 역할이 분리되면서 문제 발생시 문제의 현상을 보았을 때 어떤 계층에 문제가 생겼는지도 파악가능.

각 계층은 하위계층을 사용하고 현계층의 기능을 포함하여 상위 계층에 제공

![image-20210516045938641](C:\Users\mph\AppData\Roaming\Typora\typora-user-images\image-20210516045938641.png)

![image-20210516045847925](C:\Users\mph\AppData\Roaming\Typora\typora-user-images\image-20210516045847925.png)

![image-20210516043437914](C:\Users\mph\AppData\Roaming\Typora\typora-user-images\image-20210516043437914.png)

## 1계층 - 물리계층(Physical Layer)

이 계층에서는 주로 전기적, 기계적, 기능적인 특성을 이용해서 통신 케이블로 데이터를 전송하게 된다. 

즉, 데이터를 전송하는 역할만 진행한다.

이 계층에서 사용되는 통신 단위는 비트이며 이것은 1과 0으로 나타내어지는, 즉 전기적으로 On, Off 상태라고 생각하면 된다. 

이 계층에 속하는 대표적인 장비는 통신 케이블, 허브, 리피터 등

데이터의 종류나 오류를 제어하지 않는다



## 2계층 - 데이터 링크계층(DataLink Layer)

물리계층을 통해 송수신되는 정보의 오류와 흐름을 관리하여 안전한 **정보의 전달을 수행**할 수 있도록 도와주는 역할

오류를 감지하면 재전송하는 방법으로 처리한다.

MAC 주소를 가지고 통신한다.

대표적인 장비로는 브리지, 스위치 



## 3계층 - 네트워크 계층(Network Layer)

데이터를 목적지까지 가장 안전하고 빠르게 전달하는 기능(라우팅)

우리가 흔히 아는 IP주소를 제공하는 계층

주소(ip)를 정하고 경로(route)를 선택하고 패킷을 전달

대표적인 장비는 라우터, L3 스위치, IP 공유기

전송 단위는 Packet





## 4계층 - 전송 계층

데이터를 전송하고 전송속도르 조절하며 오류가 발생한 부분은 다시 맞춰주는계층

통신을 활성화하기 위한 계층이다

데이터를 전송받은 경우 4계층에서 해당 데이터를 하나로 합쳐서 5계층에 보내준다.. 

- 프로토콜 
  - TCP: 신뢰성있는 통신을 보장한다. 따라서 데이터가 전달되는 과정에서 여러 스위치 라우터 등등을 거치면서 데이터가 잘못 전달되는 현상이나 전달이 안되는 경우 오류제어, 흐름제어를 통해 신뢰성있는 데이터가 전달될 수 있도록 한다. 연결지향적 (Connection-oriented) 

    > 데이터 전송단위: segment

  - UDP:  비연결형 프로토콜로서 데이터를 빠르게 전달하는데에 초점을 두고 있다. 따라서 UDP는 목적지에 데이터가 제대로 전달 되었는지 조차 확인하지 않는다. 그냥 전송하면 끝. 그래서 신뢰성 있는 데이터 전송이 필요할 때보다 스트리밍같이 연속적인 특성을 가지고 있는 서비스에 사용한다.

    > 데이터 전송단위: Datagram



## 5계층 - 세션 계층(Session Layer)

세션 계층부터 데이터를 만들어내는 계층이다.

세션을 만들고 유지하며, 세션 종료, 전송 중단시 복구 기능

네트워크상 양쪽 연결을 관리하고 연결을 지속시켜주는 계층.

데이터가 통신하기 위한 논리적인 연결을 말한다

동시 송수신 방식(duplex), 반이중 방식(half-duplex), 전이중 방식(Full Duplex)의 통신과 함께, 체크 포인팅과 유휴, 종료, 다시 시작 과정 등을 수행한다.

이 계층은 TCP/IP 세션을 만들고 없애는 책임을 진다.

통신하는 사용자들을 동기화하고 오류복구 명령들을 일괄적으로 다룬다.
대표적으로 RPC, Socket 등이 있다.





## 6계층 - 표현 계층(Presentation Layer)

데이터 표현이 상이한 응용 프로세스의 독립성을 제공하고, 암호화 한다.

표현 계층(Presentation layer)은 코드 간의 번역을 담당하여 사용자 시스템에서 데이터의 형식상 차이를 다루는 부담을 응용 계층으로부터 덜어 준다. MIME 인코딩이나 암호화 등의 동작이 이 계층에서 이루어진다. 

예를 들면, EBCDIC로 인코딩된 문서 파일을 ASCII로 인코딩된 파일로 바꿔 주는 것, 

해당 데이터가 TEXT인지, 그림인지, GIF인지 JPG인지의 구분 등이 표현 계층의 몫이다.



응용계층으로 전달하거나 전달받은 데이터의 인코딩 및 디코딩이 이루어지는 계층

응용계층에서 data를 이해할수 있도록 응용프로글매에 맞춰 변환.





## 7계층 - 응용 계층(Application Layer)

응용 계층(Application layer)은 응용 프로세스와 직접 관계하여 일반적인 **응용 서비스를 수행**한다. 

일반적인 응용 서비스는 관련된 응용 프로세스들 사이의 전환을 제공한다. 

네트워크 소프트웨어 UI 부분, 사용자의 입출력(I/O)부분

최종 목적지로서 HTTP, FTP, SMTP, POP3, IMAP, Telnet 등과 같은 프로토콜이 있다. 

해당 통신 패킷들은 방금 나열한 프로토콜에 의해 모두 처리되며 우리가 사용하는 브라우저나, 메일 프로그램은 프로토콜을 

보다 쉽게 사용하게 해주는 응용프로그램이다. 한마디로 모든 통신의 양 끝단은 HTTP와 같은 프로토콜이지 응용프로그램이 아니다.

응용 계층은 응용 프로세스와 직접 관계하여 일반적인 응용 서비스를 수행한다.
한마디로 우리가 사용하는 사용자 인터페이스를 제공하는 프로그램 등을 말하는 것이다.

사용자 또는 어플리케이션이 네트워크에 접근 할수 있도록 해준다.

사용자에게 보이는 유일한 계층



**프로토콜**

- HTTP
  - 웹 상에서 웹 서버 및 웹브라우저 상호 간의 데이터 전송을 위한 응용계층 프로토콜
  -  요청 및 응답의 구조
  - 트랜잭션 중심의 비연결성 프로토콜
  -  메세지 교환 형태의 프로토콜 

- SMTP(Simple Mail Transfer Protocol)

  - 인터넷에서 이메일을 보내고 받기 위해 이용되는 프로토콜, TCP 포트번호 25번 사용

- FTP(File Transfer Protocol)

  - 컴퓨터 간 파일을 전송하는데 사용되는 프로토콜 (데이터 전달 : 20번포트, 제어정보전달 : 21번포트)

  

  

  

  