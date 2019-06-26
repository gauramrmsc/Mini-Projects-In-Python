#Program To Merge Two Sorted Lists(Time Complexity-n)
lst=[]
l1=[1,3,4,9,27,33,39,50,78]
l2=[3,5,7,8,25]
l1_ptr=0;
l2_ptr=0;
l1_len=len(l1);
l2_len=len(l2);

while l1_ptr<l1_len and l2_ptr<l2_len:
    if(l1[l1_ptr]<l2[l2_ptr]):
        lst.append(l1[l1_ptr])
        l1_ptr=l1_ptr+1
    elif(l1[l1_ptr]>l2[l2_ptr]):
        lst.append(l2[l2_ptr])
        l2_ptr=l2_ptr+1
    else :
        lst.append(l1[l1_ptr])
        l1_ptr=l1_ptr+1
        lst.append(l2[l2_ptr])
        l2_ptr=l2_ptr+1

if(l1_ptr<l1_len):
    for n in range(l1_ptr,l1_len):
        lst.append(l1[n])
if(l2_ptr<l2_len):
    for n in range(l2_ptr,l2_len):
        lst.append(l2[n])
print(lst)