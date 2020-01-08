def find_peak(list):
    high = len(list)-1
    low = 0
    if len(list) == 1:
        return list[0]
    while high >= low:
        mid = (high+low)//2
        if mid-1 >= 0 and list[mid-1] > list[mid]:
            high = mid
        elif mid+1 < len(list) and list[mid+1] > list[mid]:
            low = mid
        else:
            return list[mid]

print(find_peak([1,2]))
        
