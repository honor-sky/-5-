import pygame
import pygame.locals
import random
import sys
import time


clock = pygame.time.Clock() #Clock 객체 clock 생성
clock.tick(30)              #초당 프레임 수를 30으로 정의

pygame.init()             #pygame 모듈 초기화
pygame.mixer.init()       #mixer 모듈 초기화
pygame.font.init()        #font 모듈 초기화

Screen = pygame.display.set_mode((800,600)) #diplay 화면 생성, 화면 해상도 800*600 으로 설정

#색 설정
WHITE = (255,255,255)    #글자 색(하얀색)으로 쓸 변수
BLACK = (0,0,0)          #글자 색(검정색)으로 쓸 변수
RED = (255,0,0)          #글자 색(빨간색)으로 쓸 변수

#폰트설정
font = pygame.font.Font("font/Wemakeprice-Bold.ttf",30)    #파일로부터 객체 font 생성 , 크기 설정(30)
font_40 = pygame.font.Font("font/Wemakeprice-Bold.ttf",40) #파일로부터 객체 font_40 생성, 크기 설정(40)

#박자를 구현해 놓은 리스트 
rhythm_list=[[0.2 ,0.5 ,0.84, 1.12, 1.43, 1.75],[0.2,0.5,0.74,1.15,1.74],[0.1,0.5,0.75,1.36,1.69,1.91],[0.2,0.9],[0.1,0.5,0.77,1.02,1.35,1.89],
             [0.1,0.5,0.99,1.23,1.58], [0.1,0.5,0.74, 1.06,1.61,1.89],[0.2,0.9],[0.1,0.5,1.08,1.33,1.6],[0.1,0.5,0.69,1.06, 1.29],
             [0.1,0.5,0.76,1.06,1.64],[0.1,0.5, 0.6, 0.7, 1.13, 1.34, 1.63,1.94],[0.1,0.5,0.76,1.06,1.65],[0.1,0.5,1.07],[0.1,0.5,1.51],
             [0.1,0.5,0.8,1.1,1.4],[0.1,0.5,0.62,0.74,0.86,1.24,1.48],[0.1,0.5,0.62,0.68,1.05,1.66],[0.1,0.5,1.06],
             [0.1,0.5,0.77,1.31,1.46,1.73],[0.1,0.5,0.78,1.08,1.36,1.66,1.88],[0.2,0.9]] 


#텍스트 클래스
class Text: 
    def __init__(self):
        pass
    def text_split(self,text): 
        self.text_list=text.split() #text를 스페이스 기준으로 쪼개서 list에 저장
        
    #출력하고자 하는 문자열을 리스트에 저장
    def rand_text(self,i):  
        text=['단 국 여 러 분', '안 녕 하 세요','단 국 인 이 래','..범생이고!',
              '숨 이 턱 막 히는','말도 안 되 게','똑 똑 한 머 리라',
              '..농담이었대!','만점 받 고 싶다!','한 번 이 라도','그 래 좋 아!','먼 저 선 수 쳐 야 겠어!',
              '교 수 님 에게','엄 청','어어엄 청','예 전 부 터','좋 아 했 었 다 고!','A + + 학점을 말이야.',
              '그 럼','이 만 돌 아 가','때 나 밀 어 야 겠다','..농담이래'] 
        return text[i] #인덱스로 문자열 반환
    
     #텍스트 처리 메소드 
    def text(self,text,x,y,i):  #텍스트, 출력 좌표 매개변수, i(리스트 안에 있는 글자 출력하려고 받음)로 받음
        text_surface = font.render(text[i],True, BLACK)   #텍스트가 표시된 surface만듬, text[i]를 출력하면 한 글자씩 나옴.
        Screen.blit(text_surface,(x,y))  #텍스트를 화면에 출력
        
    # 설명하는 텍스트 메소드
    def expl(self,text, x, y): # 텍스트, 출력 좌표 매개변수
        expl_text = pygame.font.Font("font/Wemakeprice-Bold.ttf", 19)   # 파일로부터 객체 expl 생성, 크기 설정(19)
        TextSurf = expl_text.render(text, True, BLACK)  # 텍스트 객체 생성
        Screen.blit(TextSurf, (x,y))  # 텍스트를 화면에 출력
        pygame.display.update()       #화면 업데이트
        
#이미지 클래스
class Image:
    def __init__(self):
        pass
    
    #이미지 처리 메소드 
    def load_image(self,name,x,y):  #이미지 파일명, 출력 좌표 매개변수로 받음
        image = pygame.image.load(name).convert_alpha() #이미지 로드 ( 이미지가 투명도를 가짐 )
        Screen.blit(image,(x,y))    #화면에 이미지 출력
        
    #이미지 fade out 메소드
    def fadeout(self):
        fadeout = pygame.Surface((800,600)) # fadeout surface 객체 생성 ( 크기 800*600 설정 )
        fadeout = fadeout.convert() # fadeout 복사본
        fadeout.fill(BLACK) #fadeout을 검정색으로 채움
        
        for i in range(255):             # 255번 반복
            fadeout.set_alpha(i)         # fadeout의 투명도를 반복할 때마다 1씩 올림 (0은 완전 투명, 255은 완전 불투명)
            Screen.blit(fadeout, (0, 0)) #fadeout을 (0,0) 위치에 그린다
            pygame.display.update() #화면 업데이트
            pygame.time.delay(5)    # 딜레이를 5로 설정 ( 단위 : milliseconds )
            
   
#효과음 처리 메소드
def music(case): 
    if(case==0): #학생 말할 때 효과음
        stu_sound = pygame.mixer.Sound("music/stu_sound(1).WAV") #파일로부터 객체 stu_sound 생성
        stu_sound.play() #효과음 재생
    elif(case==1): #학생 말할 때 효과음
        stu_sound = pygame.mixer.Sound("music/stu_sound(2).WAV") #파일로부터 객체 stu_sound 생성
        stu_sound.play() #효과음 재생
    elif(case==2): #학생 말할 때 효과음
        stu_sound = pygame.mixer.Sound("music/stu_sound(3).WAV") #파일로부터 객체 stu_sound 생성
        stu_sound.play() #효과음 재생
    elif(case==3): #통역 맞았을 때 효과음
        good_sound=pygame.mixer.Sound("music/bear_sound(1).WAV") #파일로부터 객체 good_sound 생성
        good_sound.play() #효과음 재생
    elif(case==4): #통역 맞았을 때 효과음
        good_sound=pygame.mixer.Sound("music/bear_sound(2).WAV")  #파일로부터 객체 good_sound 생성
        good_sound.play() #효과음 재생
    elif(case==5): #통역 맞았을 때 효과음
        good_sound=pygame.mixer.Sound("music/bear_sound(3).WAV")  #파일로부터 객체 good_sound 생성
        good_sound.play() #효과음 재생
    elif(case==6): #통역 틀렸을 때 효과음          
        bad_sound = pygame.mixer.Sound("music/wrong_sound.WAV") #파일로부터 객체 bad_sound 생성
        bad_sound.play() #효과음 재생
    else: #학생 말할 때 깔리는 추가 효과음
        add_sound = pygame.mixer.Sound("music/add_sound.WAV") #파일로부터 객체 add_sound 생성
        add_sound.set_volume(0.1) #add_sound의 볼륨을 0.1로 설정
        add_sound.play() #효과음 재생

#점수 표시 메소드
def draw_score():
    font_20= pygame.font.Font("font/Wemakeprice-Bold.ttf", 20) #파일로부터 객체 font_20 생성, 크기 설정(20)
    text_score= font_20.render("Score:"+str(score), True, RED) #텍스트 객체 생성(출력할 문자열, Anti-aliasing 사용 여부, 텍스트 컬러) 
    Screen.blit(text_score, (15,10)) #텍스트 화면(15,10)에 출력 
        
#리듬을 출력하는 메소드
def student_speaking(listA,order):
    list_X = [0,260,310,360,410,460,510,560,610,660] #x 좌표 저장한 리스트 #고정
     
    Im = Image()  #이미지 객체 생성
    Im.load_image("image/game_screen.png",0,0)       #게임 화면 이미지 로드
    Im.load_image("image/speaking_stu.png", 0, 0)    #학생 기본 이미지 로드
    Im.load_image("image/default_bear.png", 0, 0)    #단곰이 기본 이미지 로드
    Im.load_image("image/brown_bubble.png",0,0)      #학생용 말풍선 이미지 로드
    draw_score()          #스코어 표시 메소드 호출                      
    pygame.display.flip() #화면 업데이트

    time.sleep(0.18) #0.18초 대기
    
    j=0                           #이미지 출력 위한 x좌표 리스트 인덱스 변수
    for i in range(len(listA)-1): # 박자 리스트의 -1만큼 반복   
        a = (listA[i+1]-listA[i]) # 지연시간 저장
        
        if(a > 0.5): #박자가 긴 경우, 박자 이미지 간격 넓게 함
            time.sleep(a)                              #박자 간 시간 지연
            sound = random.randint(0,2)                #학생 말하는 효과음 랜덤 선택
            music(sound)                               #소리 출력(학생 효과음)
            music(7)                                   #소리 출력(추가 효과음)
            if(order==3): #i가 3,7,21일 땐, 박자 이미지가 정가운데 출력
                Im.load_image("image/image011.png",350,480)    #박자 이미지 로드
            elif(order==7):
                Im.load_image("image/image011.png",350,480)    #박자 이미지 로드
            elif(order==21):
                Im.load_image("image/image011.png",350,480)    #박자 이미지 로드
            else:
                Im.load_image("image/image01.png",list_X[j+2],480) #박자 이미지 로드
            pygame.display.update()                               #화면 업데이트
            j = j+2                                               #현재 x좌표의 위치를 j에 저장
            
        else:#박자가 짧은 경우
            time.sleep(a)      #박자 간 시간 지연
            sound = random.randint(0,2)  #학생 말하는 효과음 랜덤 선택
            music(sound)     #소리 출력(학생 효과음)
            music(7)           #소리 출력(추가 효과음)
            Im.load_image("image/image01.png",list_X[j+1],480)    #박자 이미지 로드
            pygame.display.update()                               #화면 업데이트
            j = j+1                                               #현재 x좌표의 위치를 j에 저장

    time.sleep(0.4) #리듬 출력 후, 잠시 대기
    next_sound = pygame.mixer.Sound("music/next_sound.WAV")  ##파일로부터 객체 next_sound 생성
    Im.load_image("image/hand-up_stu.png", 0, 0)             #학생이 단곰이 가르키는 이미지 로드 
    pygame.display.update()       #화면 업데이트
    next_sound.play()             #next_sound 재생
           
#사용자 입력 받고, 확인하는 메소드
def translate(listA,txt_index):
    
     list_X = [260,310,360,410,460,510,560,610,660] #x 좌표 저장한 리스트(고정)
     Im = Image()            #이미지 객체 생성
     Txt = Text()            #텍스트 객체 생성
     i=0                     #박자 리스트 위한 인덱스 변수
     j=0                     #텍스트 출력 위한 x좌표 리스트 인덱스 변수
     result = True           #한 판이 성공했는지 실패했는지 저장하는 변수
 
     Im.load_image("image/game_screen.png",0,0)     #게임 화면 이미지 로드
     Im.load_image("image/speaking_bear.png", 0, 0) #손 든 학생 이미지 로드
     Im.load_image("image/hand-up_stu.png", 0, 0)   #손 든 단곰이 이미지 로드
     Im.load_image("image/white_bubble.png",0,0)    #하양 말풍선 로드(단곰이용)
     draw_score()           #스코어 표시 메소드 호출
     pygame.display.flip()  #화면 업데이트
 
     Txt.text_split(Txt.rand_text(txt_index))       #인덱스 이용해 저장된 문자열 불러오고 분리해 인스턴스 객체의 리스트에 저장
     pre_ticks = time.time()                        #사용자의 시작 타이밍 체크 위함


     while(True): # 참인 동안 반복
       
        for event in pygame.event.get(): # 이벤트가 발생하면 실행되는 반복

                pygame.display.update()
                
                keys = pygame.key.get_pressed() #키 입력받음
            
                if(result == False):      #이 판은 실패 했으므로 메소드 바로 끝남
                    return False
                if(i==len(listA)-1):      #i가 0부터 시작하기 때문에 i가 len(listA)-2만큼 게임 실행하면 성공 #즉,len(listA)-1에서 멈춤
                    time.sleep(0.1)       #대기(bgm과의 박자 맞추기 위함)
                    wow_sound=pygame.mixer.Sound("music/wow_sound(2).WAV")  #파일로부터 객체 wow_sound 생성 (성공 시 효과음)
                    wow_sound.play()      #wow_sound 재생 
                    time.sleep(0.2)       #0.2초 대기
                    return True 

                if (keys[pygame.K_RIGHT]):      #->버튼 누르면 사용자 입력받음
                    current_ticks = time.time() #버튼 누른 시간
                
                    if((listA[i+1]-listA[i]) - 0.3 <= (current_ticks- pre_ticks) <= 0.5 + (listA[i+1]-listA[i])): #제대로 클릭 시,
                        a = (listA[i+1]-listA[i])# 박자 간 지연 시간 저장

                        if(a > 0.4):#박자가 긴 경우, 박자 이미지 간격 넓게 함
                            if(txt_index==3): #i가 3,7,21일 땐, 글자가 정가운데 출력
                                Txt.text(Txt.text_list,330,490,i)            #박자에 해당하는 글자 출력    
                            elif(txt_index==7):
                                Txt.text(Txt.text_list,330,490,i)            #박자에 해당하는 글자 출력    
                            elif(txt_index==21):
                                Txt.text(Txt.text_list,330,490,i)            #박자에 해당하는 글자 출력
                            elif(txt_index==11):
                                Txt.text(Txt.text_list,list_X[j+1]-30,490,i) #박자에 해당하는 글자 출력
                            else:
                                Txt.text(Txt.text_list,list_X[j+1],490,i) #박자에 해당하는 글자 출력 
                            sound = random.randint(3,5)                   #올바른 글자 출력시 효과음 랜덤으로 저장
                            music(sound)                                  #효과음 호출
                            j=j+1       #현재 x좌표의 위치를 j에 저장
                            
                        else: #박자가 짧은 경우
                            if(txt_index==11): #i=11일 땐, 좀 더 왼쪽에 글자 출력
                                Txt.text(Txt.text_list,list_X[j]-30,490,i) #박자에 해당하는 글자 출력   
                            else:
                                 Txt.text(Txt.text_list,list_X[j],490,i)   #박자에 해당하는 글자 출력        
                            sound = random.randint(3,5)               #올바른 글자 출력시 효과음 랜덤으로 저장
                            music(sound)                              #효과음 호출
                        pre_ticks= current_ticks                      #다음 -> 버튼 클릭 시,시간 차이 비교 위해 curren을 pre로 바꾼다
                    
                    else: #실패 시
                        Im.load_image("image/game_screen.png",0,0)     #게임 화면 이미지 로드
                        Im.load_image("image/hand-up_bear.png", 0, 0)  #손 든 학생 이미지 로드
                        Im.load_image("image/hand-up_stu.png", 0, 0)   #손 든 단곰이 이미지 로드
                        Im.load_image("image/white_bubble.png",0,0)    #하양 말풍선 로드(단곰이용)
                        draw_score()                  #스코어 표시 메소드 호출
                        pygame.display.flip()         #화면 업데이트
                        
                        text_surface = font.render("??솰라솰라?#$%?&#?",True,BLACK)  #텍스트 객체 생성
                        Screen.blit(text_surface,(250,490))                          #(250,490)위치에 이상한 말  출력
                        pygame.display.flip()         #화면 업데이트
                        music(6)                      #이상한 소리 출력
                        time.sleep(listA[(len(listA)-1)]-listA[i+1]+0.2)#틀리면 실패이므로 그 판에 할당된 시간 끝날 때까지 기다려야 함(추가로 0.2초 더 대기)
                        result = False                #게임 실패 / 여기서 return문 사용하면 마지막 이미지 출력이 안 돼서 변수로 저장
                        
                    j += 1              # 텍스트 출력위한 x좌표 리스트 인덱스 1 증가
                    if(i<len(listA)-1): #다음 박자 위해 i +1 한다
                       i += 1                            


                
'''게임 방법 설명 화면'''
Im = Image()                              #이미지 객체 생성
Txt = Text()                              #텍스트 객체 생성
Im.load_image("image/Title_image.png", 0, 0)         #시작 배경 화면 로드
first_music = pygame.mixer.Sound("music/first.mp3")  #파일로부터 객체 first_music 생성 (시작 음악)
first_music.play()         #시작 음악 출력
pygame.display.update()    #화면 업데이트
time.sleep(4)              #4초 대기 
Im.fadeout()               #4초 후 fadeout 함수 호출

Im.load_image("image/manual_screen.png", 0, 0)#게임 설명 화면 로드
pygame.display.update()                       #화면 업데이트


Txt.expl("프로젝트 명 : 절대음감 단곰이", 85,75)  #expl 함수를 통해 설명서 출력, 입력된 위치에 각각의 문자열
Txt.expl("제작 : 박치 (5조)", 85, 105)
Txt.expl("BGM의 리듬에 맞춰 → 키를 누르면 단곰이가 학생의 말을 통역합니다.", 135, 140)
Txt.expl("타이밍에 맞지 않을 경우 단곰이가 학생의 말을 제대로 통역하지 못하니 주의!", 110,170)
Txt.expl("게임을 시작하려면 → 키를 눌러주세요!", 245, 210)
                
A = True 
while (A): #A가 참일 동안 

    for event in pygame.event.get():        #이벤트가 발생하면 실행되는 반복
        if event.type == pygame.KEYDOWN:    #방향키를 누를 때
            if event.key == pygame.K_RIGHT: #-> 방향키 누르면
                Im.fadeout()            #fadeout 함수 호출
                first_music.fadeout(30) #30 milliseconds 동안 모든 소리의 볼륨을 페이드 아웃 / 사운드가 음소거 되면 재생 중지 
                A = False


'''본 게임'''
Im.load_image("image/game_screen.png",0,0)  #게임화면 이미지 로드
Im.load_image("image/default_bear.png",0,0) #단곰이 기본 이미지 로드
Im.load_image("image/default_stu.png",0,0)  #학생 기본 이미지 로드
pygame.display.flip()    #화면 업데이트

score = 0   #점수를 저장하는 score 변수
game_start = pygame.mixer.Sound("music/game_sound.mp3") #게임 bgm 객체 생성
game_start.play()            #game_start에 저장된 game_sound 출력
time.sleep(4.1)              #4.1초 대기 
game_start.set_volume(0.55)  # 소리 크기 0.55로 설정 

#게임 22번 반복
for i in range(22):
  draw_score()           #점수 출력
  pygame.display.update()#화면 업데이트
  student_speaking(rhythm_list[i],i)     #리듬 리스트에서 리듬 매개변수로 전달해 student_speaking 메소드 호출
  result = translate(rhythm_list[i],i)   #사용자의 게임 성공 여부를  result에 저장(True -> 성공,False -> 실패)
  
  #score체크  
  if(result == True):#성공 시, score 1 증가, 실패시에는 점수 변동 없음       
       score += 1
    
  #중간점검    
  if(i==7):
       if(score < 6):#게임이 11번 진행하는 동안 점수가 6점보다 낮은 경우
           Im.load_image("image/sleep_bear.png",0,0)     #조는 단곰이 사진 출력
           pygame.display.flip()     #화면 업데이트
           time.sleep(0.8)           #0.8초간 대기
       else:
           Im.load_image("image/wake_bear.png",0,0) #깬 단곰이 사진 출력
           pygame.display.flip()         #화면 업데이트
           time.sleep(0.8)               #0.8초간 대기
  time.sleep(0.4)                        #한 번 반복 끝나면 0.4 대기
    
time.sleep(0.4) #마지막 게임에서는 0.4초 더 대기

#성공, 실패 화면 설정
if(score < 16):#최소 점수가 16점이여야 성공
    Im.load_image("image/sleep_bear.png",0,0) #조는 단곰이 이미지 로드
    pygame.display.update()     #화면 업데이트
    time.sleep(3)               #3초 대기
    Im.load_image("image/gameover.png",0,0)   #실패 이미지 로드
    pygame.display.update()     #화면 업데이트

else:
    Im.load_image("image/wake_bear.png",0,0) #깬 단곰이 이미지 로드
    pygame.display.update()             #화면 업데이트
    time.sleep(3)                       #3초 대기
    Im.load_image("image/clear.png", 0,0)    #성공 이미지 로드
    pygame.display.update()                  #화면 업데이트


time.sleep(15) #15초 대기

pygame.quit()  #pygame 종료

                    
