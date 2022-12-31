# smartFarm

## 구조
### Raspberry Pi Pico W - Firebase Realtime Database - Web or App  
![1](https://user-images.githubusercontent.com/13882302/210129906-76bc322a-fb4e-4375-8104-6a515bfeb861.png)
![2](https://user-images.githubusercontent.com/13882302/210129908-b2e48b08-0a86-4980-ba4a-a07fab87f81c.png)

---
## 세팅
### 1.Firebase 세팅
1. 아래 링크로 이동해서 구글 계정으로 로그인을 하고, 오른쪽 상단에 있는 '콘솔로 이동' 버튼을 눌러 Firebase 콘솔로 들어간다.  
[https://firebase.google.com/](https://firebase.google.com/)  
![image](https://user-images.githubusercontent.com/13882302/210128421-231a463e-c585-4814-8544-16eb70728961.png)

2. '프로젝트 추가'버튼을 눌러 자신의 프로젝트를 만든다.  
![image](https://user-images.githubusercontent.com/13882302/210128433-2493803d-020a-4560-ac5f-8c6560a0e82c.png)  
![image](https://user-images.githubusercontent.com/13882302/210128462-40a34a3a-6ed5-4759-9292-ed18856f3b6e.png)  

3. 데이터 분석을 하지 않을 경우 Google 애널리틱스 사용 설정을 해제하고 '프로젝트 만들기'버튼을 누른다.  
![image](https://user-images.githubusercontent.com/13882302/210128474-640f97e3-0a27-417a-b9e8-f0d1b747ae97.png)  
![image](https://user-images.githubusercontent.com/13882302/210128488-dc17be71-c67b-4be4-bf07-fd68c77a5117.png)  

4. 30초 정도 프로젝트 생성 시간을 기다린다.  
![image](https://user-images.githubusercontent.com/13882302/210128513-84031eea-968f-4b3d-a7ad-610bd2bd7e91.png)  
![image](https://user-images.githubusercontent.com/13882302/210128514-c0907965-f00a-47cb-af5c-d6b2acde54f9.png)  
![image](https://user-images.githubusercontent.com/13882302/210128521-98278090-4159-4e4c-a769-cba0c58946c5.png)  

5. 새로 만든 프로젝트 폴더로 들어간다.  
![image](https://user-images.githubusercontent.com/13882302/210128535-ea7d689c-2baf-4252-bfab-2746290c8b03.png)  

6. Firebase 메뉴중에서 빌드-Realtime Database를 선택해서 연다.  
<img width="389" alt="화면 캡처 2022-12-31 160136" src="https://user-images.githubusercontent.com/13882302/210128358-d1045b3f-98d1-495c-b4fa-29fab188e25a.png">  

7. '데이터베이스 만들기' 버튼을 누른다.  
![image](https://user-images.githubusercontent.com/13882302/210128622-b9bf441c-b07c-449c-9633-b638d744f179.png)  

8. 서버 위치를 선택한다.  
![image](https://user-images.githubusercontent.com/13882302/210128633-124bfef0-5edc-4214-a111-eea07e291ea1.png)  

9. 데이터베이스 기본 설정을 한다. 추후 언제나 바꿀 수 있으니 기본 세팅으로 사용설정을 한다.  
![image](https://user-images.githubusercontent.com/13882302/210128658-8eaa6130-0875-4517-b8a0-1c34824340b9.png)  

10. 가운데 있는 링크를 통해 Realtime Database에 접근을 할 수 있다.  
![image](https://user-images.githubusercontent.com/13882302/210128672-ce1602e5-535c-4db1-80e0-77c6f38a5e5e.png)  

11. '규칙' 탭으로 들어오면 데이터베이스에 대한 읽기, 쓰기 권한이 설정되어 있는데, 이 설정이 매우 중요하다.  
![image](https://user-images.githubusercontent.com/13882302/210128700-f12252c9-6de3-4c2b-a0e2-feb2801dc9b2.png)  

12. false로 기본 설정되어 있는데, 이곳을 클릭하여 true로 바꿔주고 '게시'버튼을 누르면 누구나 접근해서 데이터를 읽고 쓸 수 있다. 추후 보안 및 트래픽에 따른 결제비용 증가에 영향을 줄 수 있으니, 테스트 할 때만 true로 설정하고, 실제 사용할 때는 읽고 쓰는 권한을 false로 바꾸고 접근한 사람의 사용자 권한에 따라 사용하거나, 엑세스 토큰을 부여받아 사용할 수 있도록 해야한다.  
![image](https://user-images.githubusercontent.com/13882302/210128717-727f05cb-7f26-4512-ad64-05fe50a9a7c5.png)  

13. 다음으로 이 Realtime Database를 실제로 사용하기 위해서 관련 config 내용을 얻어야 한다. 프로젝트 개요-기어 버튼-프로젝트 설정으로 가서 내 웹앱에 firebase를 추가하는 버튼을 눌러 세팅을 완료하고, config 정보를 얻어낸다. 한 번 세팅을 완료하면 세팅을 삭제하기 전까지는 계속 해당 config를 사용할 수 있다.    
![image](https://user-images.githubusercontent.com/13882302/210128316-0838da1d-557a-4972-86e5-7b5654286696.png)  

<img width="573" alt="210127985-4958b729-b8d9-4291-88dd-9501b94bfc01" src="https://user-images.githubusercontent.com/13882302/210128211-9489a97d-d658-4298-b674-a54d5a44e023.png">  

<img width="716" alt="210128004-1cfdf26e-da0b-4f69-9ae5-163931e758bd" src="https://user-images.githubusercontent.com/13882302/210128268-1395688d-3c6a-4745-b540-76e218954ecd.png">  

![image](https://user-images.githubusercontent.com/13882302/210128010-065282ab-3778-4edb-bed9-709ac418d0de.png)  

![image](https://user-images.githubusercontent.com/13882302/210128019-d674a4f2-a714-42aa-b2f9-c4f908e9df20.png)  

<img width="623" alt="화면 캡처 2022-12-31 155100" src="https://user-images.githubusercontent.com/13882302/210128091-6e17baa4-6798-4b1a-bf11-1a36afd1402c.png">  

14. firebase config 정보를 가져온다. 아래의 최종 이미지 안에 있는 firebaseConfig 내부의 값만 복사해서 내 웹의 web/public/js/firebase.js파일의 해당 부분에 붙여넣으면 자신의 Realtime Database에 접근해서 온도, 습도, 조도, LED제어, Fan제어를 위한 데이터를 주고 받는 smartFarm 제어용 웹 서비스를 바로 이용할 수 있다. 
<img width="287" alt="화면 캡처 2022-12-31 155119" src="https://user-images.githubusercontent.com/13882302/210128094-0829b06a-c575-4ba5-8ef4-2df90652cc8b.png">  

* Firebase 사용 요금제는 아래 링크를 참고하면 되며, 테스트 용도로는 비용이 따로 들지 않는다고 봐도 무방하다.  
[https://firebase.google.com/pricing?authuser=0&hl=ko](https://firebase.google.com/pricing?authuser=0&hl=ko)  

### 2. Web(github pages) 세팅
* 테스트 링크 
[https://mtinet.github.io/smartFarm/web/public/index.html  ](https://mtinet.github.io/smartFarm/web/public/index.html)  

### 3. Raspberry Pi Pico W 세팅

---
## 세그먼트 간 통신 테스트 영상
### Web - Firebase
https://user-images.githubusercontent.com/13882302/210126670-243a6fd7-b9b9-4378-b12e-63e5b2ef9260.mp4

