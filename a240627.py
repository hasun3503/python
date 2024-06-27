from tkinter import *

def add_order(item) :
    global amount #전역변수 선언
    order[item] += 1
    amount += coffee_menu[item]
    if item not in order_list:
        order_list.append(item)
    update_display()


def increase_order(item):
    global amount
    order[item] += 1
    amount +=coffee_menu[item]
    update_display()

def decrease_order(item):
    global amount
    if order[item]>0:
        order[item] -= 1
        amount -=coffee_menu[item]
    update_display()

def update_display():
    global amount, order_list  #gpt
    for widget in order_frame.winfo_children():
        widget.destroy()   #mmm
        
    row =0

    for item in reversed(order_list):
        item_label = Label(order_frame, text = f"{item} : {order[item]}개 ", justify= LEFT)
        item_label.grid(row=row, column=0, sticky = W)

        increase_button = Button(order_frame, text='▲', command = lambda item = item: increase_order(item))
        increase_button.grid(row=row, column = 1)

        decrease_button = Button(order_frame, text='▼', command = lambda item = item: decrease_order(item))
        decrease_button.grid(row=row, column = 2)

        row +=1

        total_label.config(text=f"total : {amount} won")

    #order_text = "order list : \n"
    #for item in reversed(order_list):
     #   order_text += f"{item} : {order[item]} \n"  #f is print supporter
     #   order_list_label.config(text=order_text)

        ##이방식은 다음에 생각해보기. 버튼 만들어서 하는 방식임 increase_button = Button()
    
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

#결재창 부분

def process_payment(): 
    global saved_order, saved_amount #gpt

    # Save the current order state
    saved_order = order.copy()
    saved_amount = amount

    for widget in win.winfo_children():
        widget.destroy()
#mmm
    payment_label = Label(win, text='결재수단 선택시요오', font= font_size_menu)
    payment_label.pack()

    card_button = Button(win, text='신용/체크카드') 
    card_button.pack()

    bank_button = Button(win, text='통장')
    bank_button.pack()

    cash_button = Button(win, text='현금')
    cash_button.pack()     

    pay_back_button = Button(win, text= 'cancle', command= process_cancle)
    pay_back_button.pack()

def process_cancle():
    global order, amount #gpt

    # Restore the saved order state
    order = saved_order.copy()
    amount = saved_amount

    # Rebuild the UI
    for widget in win.winfo_children():
        widget.destroy()

    # Restore coffee menu buttons
    for idx, (item, price) in enumerate(coffee_menu.items()):
        button = Button(win, text=f'{item}\n \n{price}원', width=10, height=6, font=font_size_menu, command=lambda item=item: add_order(item))
        button.grid(row=0, column=idx)

    # Restore order display
    update_display()  #mmm


#따로 메뉴 담아놨다가 다시 뒤로가면 복구하는 식으로
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

win = Tk()
win.title('coffee machine') #title 
win.geometry("500x600") # page size

coffee_menu = {"Americano" : 2500, "Cappuccino" : 3000, "espresso   " : 5000} # coffee menu list
order = {"Americano": 0, "Cappuccino" : 0, "espresso   " : 0} #order list  ,빈칸 때문에 글자 오류/? 날수도 읷응깨 채우기
#amount_changer = {a : 0, c : 0 , e : 0}
amount = 0
order_list = []

font_size_menu = ('Arial, 20') #font size for coffee menu
font_size_paylist = ('Arial, 13')  #보류 
font_size_payment = ('Arial, 15')

for idx, (item, price) in enumerate(coffee_menu.items()):   #button for menu setting
    button = Button(win, text=f'{item}\n \n{price}won', width=10, height=6, font = font_size_menu, command = lambda item = item : add_order(item))
    button.grid(row=0, column=idx)

order_frame = Frame(win)
order_frame.grid(row=2, column=0, columnspan=3, sticky=W)

#order_list_label = Label(win, text = order_list , justify = LEFT)  # justify 는 정렬 
#order_list_label.grid(row=1, column=0, columnspan=3, sticky=W)

total_label = Label(win, text=f"결재금액 : {amount} won", font = font_size_payment)
total_label.grid(row=3, column=0, columnspan=3, sticky=W) #sticky는 위치지정. w는 서쪽방향

payment_button = Button(win, text='결제하기', command= process_payment)
payment_button.grid(row=3, column=1) #세로, 가로 칸..

#for idx, (item, amount_change) in enumerate()

#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

#결재창 부분

win.mainloop()