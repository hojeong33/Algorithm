x,y,w,h=map(int,input().split())
w_x=w-x
h_y=h-y
print(min(w_x,h_y,x,y))