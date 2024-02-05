import time

def selection_sort(A,draw_data,timeTick):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j        
        A[i], A[min_idx] = A[min_idx], A[i]
        draw_data(A,['blue' if x==i or x==min_idx else 'red' for x in range(len(A))])
        time.sleep(timeTick)
    draw_data(A,['yellow' for i in range(len(A))])