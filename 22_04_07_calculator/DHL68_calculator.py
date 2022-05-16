import tkinter as tk


# 명령어 변수
operator = {'+':1, '-':2, '/':3,
            '*':4, 'C':5, '=':6}
disValue = 0 # 결과값 변수 / 정수
stoValue = 0 # 저장된 값
opPre = 0 # 이전 명령어

# 숫자 클릭
def number_click(value):
    # print('숫자', value)
    global disValue
    disValue = (disValue * 10) + value
    str_value.set(disValue)

# 리셋
def clear():
    global disValue, stoValue, opPre
    stoValue = 0
    opPre = 0
    disValue = 0
    str_value.set(disValue)

# 해당 명령 조건
def operator_click(value):
    # print('명령', value)
    global disValue, operator, stoValue, opPre
    op = operator[value]
    if op == 5: # C
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(disValue)
    elif op == 6: # =
        if opPre == 1:
            disValue = stoValue + disValue
        if opPre == 2:
            disValue = stoValue - disValue
        if opPre == 3:
            disValue = stoValue / disValue
        if opPre == 4:
            disValue = stoValue * disValue

        str_value.set(str(disValue))
        disValue = 0
        stoValue = 0
        opPre = 0
    else:
        clear()

    

# 버튼
def button_click(value):
    # print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)

# 계산기 폼
win = tk.Tk() # 클래스 생성
win.title('계산기') # 타이틀 입력

str_value = tk.StringVar()
str_value.set(str(disValue)) # disValue의 정수를 str을 통해 문자열로 변환 / .set 으로 str_value 에 입력
dis = tk.Entry(win, textvariable = str_value, justify = 'right', bg = 'white', fg = 'red') # [계산기 입력 표시 영역] textvariable 값을 자동으로 갱신 / justify : 배치
dis.grid(column = 0, row = 0, columnspan = 4, ipadx = 80, ipady = 30) # columnspan : colum의 span 위치 조정 / ipad x,y input 창의 크기 조정


calItem = [['1', '2', '3', '4'],
           ['5', '6', '7', '8'],
           ['9', '0', '+', '-'],
           ['/', '*', 'C', '=']]

for i, items in enumerate(calItem):
    for k, item in enumerate(items):
        try:
            color = int(item) # 정수 에러를 이용해서 정수일 경우 검은색, 에러가 날 경우 초록색
            color = 'black'
        except:
            color = 'green'

        # [계산기 숫자 버튼 입력 영역]
        bt = tk.Button( # 변수 선언
            win,
            text = item, # item 선언
            width = 10, # 가로
            height = 5, # 세로
            bg = color, # 배경색
            fg = 'white', # 글자색
            command = lambda cmd = item: button_click(cmd) # item 을 cmd에 받아 버튼 클릭 시 cmd을 버튼 기능에 입력
            )
        bt.grid(column = k, row = i + 1) # 반복구문을 통해 리스트의 순서를 반복 합산하여 위치 지정

win.mainloop() # 계산기 모듈 실행