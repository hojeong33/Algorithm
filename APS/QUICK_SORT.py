def partition(arr,L,R):
    p=arr[L]
    i=L #p보다 큰거 찾기
    j=R #p보다 작은거 찾기
    while i<=j:
        while i<=j and arr[i]<=p:
            i+=1
        while i<=j and arr[j]>=p:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[L],arr[j]=arr[j],arr[L]
    return j # 새 피봇 인덱스 반환

def quick_sort(arr,L,R):
    if L<R:
        p=partition(arr,L,R)
        quick_sort(arr,L,p-1)
        quick_sort(arr,p+1,R)

arr=[8,13,2,6,1,4]
quick_sort(arr,0,len(arr)-1)
print(arr)