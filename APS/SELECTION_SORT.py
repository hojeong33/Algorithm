# 구간의 최소값을 구해서 start와 스왑

def selection_sort(start,end):
    if start==end:
        return arr

    MIN=min(arr[start:end+1])
    idx=arr.index(MIN)

    if idx!=start:
        arr[idx],arr[start]=arr[start],arr[idx]
    return selection_sort(start+1,end)

arr=[8,13,2,6,1,4]
print(selection_sort(0,len(arr)))

