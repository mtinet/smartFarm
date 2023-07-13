#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <AHT10.h>

#define A_IA 5 // 모터드라이버 A_1A 단자 연결 핀번호(워터펌프)
#define A_IB 4 // 모터드라이버 A_1B 단자 연결 핀번호
#define B_IA 6 // 모터드라이버 B_1A 단자 연결 핀번호(팬)
#define B_IB 7 // 모터드라이버 B_1B 단자 연결 핀번호
#define SOIL_HUMI A0

LiquidCrystal_I2C lcd(0x27,20,4);  // LCD I2C 주소: 0x27
AHT10Class AHT10;

int cds_pin = A1; // 조도센서에 사용할 핀번호
int cds_ledpin = 13; // LED에 사용할 핀번호
int soil, psoil;  // 수분센서 값을 사용하기 위한 변수 선언
int val, cdsval, pcdsval; // 조도센서 값을 사용하기 위한 변수 선언
float t = 0;
float h = 0;
int waterpumpPower = 150;
int fanPower = 150;

void setup() {
  // AHT10 초기 설정
  Serial.begin(9600);
  Wire.begin();
  if(AHT10.begin(eAHT10Address_Low)) {
    Serial.println("Init AHT10 Success.");
  } else {
    Serial.println("Init AHT10 Failure.");
  }

  // LCD 초기 설정, 오프닝 이벤트    
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Hello,SmartFarm!");
  lcd.setCursor(0,1);
  lcd.print("Made by M2Hands!");

  // 시리얼 통신 설정
  Serial.begin(9600); 
  Serial.println("Let's Go!");
  delay(1000);

   // 핀 설정 초기화
   pinMode(A_IA, OUTPUT); // 모터드라이브 출력모드
   pinMode(A_IB, OUTPUT);  
   analogWrite(A_IA, LOW); // 모터드라이브 초기값은 끈 상태
   analogWrite(A_IB, LOW);
   pinMode(B_IA, OUTPUT);
   pinMode(B_IB, OUTPUT);  
   analogWrite(B_IA, LOW);
   analogWrite(B_IB, LOW);
   pinMode(cds_ledpin,OUTPUT);
}

void loop() {
  t = AHT10.GetTemperature();
  h = AHT10.GetHumidity();

  soil = analogRead(SOIL_HUMI); // A0에서 읽은 값을 soil 변수에 저장
  psoil = map(soil, 1023, 0, 0, 100); // map함수를 사용하여 soil값을 1~100으로 변환한 값을 psoil에 저장
  val = analogRead(cds_pin); // A1에서 읽은 값을 val 변수에 저장
  cdsval = map(val,0, 1023, 250, 0); // map함수를 사용하여 val값을 1~250으로 변환한 값을 cdsval에 저장
  pcdsval = cdsval*0.4; // 조도센서값을 0~100으로 표시하기 위한 설정
  
  lcd.init(); // LCD 초기화 init() 명령이 안먹으면 begin으로 수정
  lcd.clear(); // 이전에 출력한 값 지우기 
  lcd.backlight(); // 배경화면 빛이 들어오도록 설정 
  lcd.display(); // 내용을 표시
  lcd.setCursor(0,0);
  lcd.print("M: "); //수분 M 
  lcd.print(psoil);
  lcd.print("%");
  lcd.setCursor(8,0);
  lcd.print("L: "); //조도 L
  lcd.print(pcdsval);  
  lcd.print("%");
  lcd.setCursor(0,1);
  lcd.print("T: "); //온도 T
  lcd.print(t,0);
  lcd.print("C");
  lcd.setCursor(8,1);
  lcd.print("H: "); //습도 H
  lcd.print(h,0);  
  lcd.print("%");

  Serial.print("수분: ");
  Serial.print(psoil);
  Serial.print("  조도: ");
  Serial.print(cdsval);
  Serial.print("  온도: ");
  Serial.print(t);
  Serial.print("  습도: ");
  Serial.print(h);
  Serial.println();
  delay(1000); 

  if(psoil < 30) { // 토양수분값이 30미만이면
    analogWrite(A_IA, waterpumpPower);  // 값을 변화시키면 서 호스에서 나오는 물의 양을 적정하게 설정
    digitalWrite(A_IB, LOW);    
  } else {  // 그 외 토양수분값이 측정되면 워터모터를 끄라
    digitalWrite(A_IA, LOW);
    digitalWrite(A_IB, LOW);
  } 
  if(t >= 20 || h >= 60) { // 온도가 20이상 또는 습도가 60이상이면,  || => [Shift] + [\]
    analogWrite(B_IA, fanPower);  // 값을 변화시키면서 팬의 세기를 설정(0~255)
    digitalWrite(B_IB, LOW);
  } else { // 그 외 온습도 측정값이면 미니모터를 끄라
    digitalWrite(B_IA, LOW);
    digitalWrite(B_IB, LOW);
  }
  if (pcdsval < 70) { // 조도센서값이 70미만이면
    digitalWrite(cds_ledpin, HIGH );   
  } else {  // 그 외 조도센서값이면 LED를 끄라
    digitalWrite(cds_ledpin, LOW);    
  }
}
