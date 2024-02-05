import time

def bubble_sort(data,draw_data,timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                draw_data(data,['blue' if x==j or x==j+1 else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    draw_data(data,['yellow' for i in range(len(data))])