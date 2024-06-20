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
    row =0
    for item in reversed(order_list):
        item_label = Label(order_frame, text = f"{item} : {order[item]} \n", justify= LEFT)
        item_label.gird(row=row, column=0, sticky = LEFT)

        increase_b0
        utton = Button(order_frame, text='▲', command = lambda item = item: increase_order(item))
        increase_button.gird(row=row, column = 1)
        decrease_button = Button(order_frame, text='▼', command = lambda item = item: decrease_order(item))
        decrease_button.gird(row=row, column = 2)

        row +=2


    #order_text = "order list : \n"
    for item in reversed(order_list):
        order_text += f"{item} : {order[item]} \n"  #f is print supporter
        order_list_label.config(text=order_text)

        ##이방식은 다음에 생각해보기. 버튼 만들어서 하는 방식임 increase_button = Button()
    
    total_label.config(text=f"total : {amount} won")



win = Tk()
win.title('coffee machine') #title 
win.geometry("500x600") # page size

coffee_menu = {"Americano" : 2500, "Cappuccino" : 3000, "espresso" : 5000} # coffee menu list
order = {"Americano": 0, "Cappuccino" : 0, "espresso" : 0} #order list
#amount_changer = {a : 0, c : 0 , e : 0}
amount = 0
order_list = []

font_size = ('Arial, 20') #font size for coffee menu

for idx, (item, price) in enumerate(coffee_menu.items()):   #button for menu setting
    button = Button(win, text=f'{item}\n \n{price}won', width=10, height=6, font = font_size, command = lambda item = item : add_order(item))
    button.grid(row=0, column=idx)

order_frame = Frame(win)
order_frame.grid(row=1, column=0, columnspan=3, sticky=W)

order_list_label = Label(win, text = "order list : \n ", justify = LEFT)  # justify 는 정렬 
order_list_label.grid(row=1, column=0, columnspan=3, sticky=W)

total_label = Label(win, text=f"결재금액 : {amount}, won")
total_label.grid(row=2, column=0, columnspan=3, sticky=W) #sticky는 위치지정. w는 서쪽방향

#for idx, (item, amount_change) in enumerate()

win.mainloop()