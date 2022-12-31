# smartFarm

## 구조
### Raspberry Pi Pico W - Firebase Realtime Database - Web or App  

## 세팅
### Raspberry Pi Pico W 세팅

### Firebase 세팅
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

![image](https://user-images.githubusercontent.com/13882302/210128316-0838da1d-557a-4972-86e5-7b5654286696.png)  

<img width="573" alt="210127985-4958b729-b8d9-4291-88dd-9501b94bfc01" src="https://user-images.githubusercontent.com/13882302/210128211-9489a97d-d658-4298-b674-a54d5a44e023.png">  

<img width="716" alt="210128004-1cfdf26e-da0b-4f69-9ae5-163931e758bd" src="https://user-images.githubusercontent.com/13882302/210128268-1395688d-3c6a-4745-b540-76e218954ecd.png">  

![image](https://user-images.githubusercontent.com/13882302/210128010-065282ab-3778-4edb-bed9-709ac418d0de.png)  

![image](https://user-images.githubusercontent.com/13882302/210128019-d674a4f2-a714-42aa-b2f9-c4f908e9df20.png)  

<img width="623" alt="화면 캡처 2022-12-31 155100" src="https://user-images.githubusercontent.com/13882302/210128091-6e17baa4-6798-4b1a-bf11-1a36afd1402c.png">  

<img width="287" alt="화면 캡처 2022-12-31 155119" src="https://user-images.githubusercontent.com/13882302/210128094-0829b06a-c575-4ba5-8ef4-2df90652cc8b.png">  
* firebase config 가져오기(최종 이미지 안에 있는 firebaseConfig 내부의 값만 복사해서 내 웹의 web/public/js/firebase.js파일의 해당 부분에 붙여넣음  

### Web(github pages) 세팅
* 테스트 링크 
[https://mtinet.github.io/smartFarm/web/public/index.html  ](https://mtinet.github.io/smartFarm/web/public/index.html)  

## 세그먼트 간 통신 테스트 영상
### Web - Firebase
https://user-images.githubusercontent.com/13882302/210126670-243a6fd7-b9b9-4378-b12e-63e5b2ef9260.mp4

