from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from selectionsort import selection_sort


root = Tk()
root.title("Algorithm Visualiser")
root.geometry("900x600+200+80")
root.config(bg="#082a46")
root.resizable(False,False)

data =[]

def draw_data(data,colorArray):
    canvas.delete('all')
    canvas_width = 870
    canvas_height = 450
    x_width = canvas_width /(len(data)+1)
    offset = 10
    spacing = 10
    normalised_data = [i / max(data) for i in data]

    for i,height in enumerate(normalised_data):
        x0 = i*x_width+spacing+offset
        y0 = canvas_height - height * 400

        x1 = (i+1)*x_width
        y1 = canvas_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]),font=('new roman',15,'italic bold'),fill='orange')
    root.update_idletasks()

def sorting():
    global data
    print("sorting started")
    if not data:
        return
    elif select_algorithm.get()=='Bubble Sort':
        bubble_sort(data,draw_data,speed.get())
    elif select_algorithm.get()=='Selection Sort':
        selection_sort(data,draw_data,speed.get())

def generate():
    global data
    print("selected algorithm  :- "+select_algorithm.get())
    min_value = int(min_size.get())
    max_value = int(max_size.get())
    size_value = int(size.get())
    
    data = []

    for _ in range(size_value):
        data.append(random.randrange(min_value,max_value+1))
    draw_data(data,['red' for i in range(len(data))]) 


selected_algorithm = StringVar()

alogithm_label = Label(root,text="Algorithm :",font=('new roman',16,'italic bold'),bg='#05897A',width=10,fg="white",bd=5,relief=GROOVE)
alogithm_label.place(x=0,y=0)

# this is combox of algorithm which algorithm you select it

select_algorithm = ttk.Combobox(root,width =15,font=('new roman',19 ,'italic bold'),textvariable=selected_algorithm,
                                values=['Bubble Sort','Quick Sort','Merge Sort','Selection Sort'])
select_algorithm.place(x=145,y=0)
select_algorithm.current(0)

# !select the speed of code runner
speed_label = Label(root,text='Speed :',width=10,height=1,font=('new roman',14,'italic bold'),bg='#05897A',fg='white',bd=5,relief=GROOVE)
speed_label.place(x=450,y=0)

speed = Scale(root,from_=0.1,to=5.0,font=('arial',12,'bold'),orient=HORIZONTAL,resolution=0.1,length=200,digits=2,width=10,bd=2,relief=GROOVE)
speed.place(x=600,y=0)

#! start button where the sorting algorithm are started

start_buton = Button(root,text='Start',width=10,font=('arial',14,'italic bold'),bd=5,bg='orange',fg='white',command=sorting,activeforeground='black',activebackground='green',relief=SUNKEN)
start_buton.place(x=750,y=0)

# ! select the size  of array
size_label = Label(root,text='Size :',width=10,height=2,font=('new roman',12,'italic bold'),bd=5, fg='white',bg="#05897A",relief=GROOVE)
size_label.place(x=0,y=60)

size = Scale(root,width=10,from_=0,to=20,font=('new roman',14,'italic bold'),orient=HORIZONTAL,resolution=1,bd=2,relief=GROOVE)
size.place(x=120,y=60)

#? select the min number of array where the start the nummber
min_label = Label(root,text='Min :',width=10,height=2,font=('new roman',12,'italic bold'),bd=5,fg='white',bg='#05897A',relief=GROOVE)
min_label.place(x=250,y=60)

min_size = Scale(root,width=10,from_=0,to=20,font=('new roamn',14,'italic bold'),orient=HORIZONTAL,bd=2,relief=GROOVE,resolution=1)
min_size.place(x=370,y=60)

#! select the max value of array where the array is last number
max_label = Label(root,text='Max :',width=10,height=2,font=('new roman',12,'italic bold'),bd=5,fg='white',bg='#05897A',relief=GROOVE)
max_label.place(x=500,y=60)

max_size = Scale(root,width=10,from_=0,to=100,font=("new roman",14,'italic bold'),orient=HORIZONTAL,resolution=1,bd=2,relief=GROOVE)
max_size.place(x=620,y=60)

#! generate button where the rectange bar or array is generated 
random_generate = Button(root,text="Generate",width=10,font=('arial',14,'italic bold'),bd=3,fg='white',bg='red',activebackground='green',activeforeground='white',relief=SUNKEN,command=generate)
random_generate.place(x=750,y=60)

#? this is canvas where the array and retangle bar and code working area
canvas = Canvas(root,width=870,height=450,bg="black")
canvas.place(x=13,y=130)





root.mainloop()



