def findMax(bookings):
    if bookings is None:
        return None
    size = len(bookings)
    if size == 0:
        return 0
    if size == 1:
        return bookings[0]
    maxim1 = bookings[0]
    maxim2 = max(bookings[0],bookings[1])
    for i in range(2,size):
        maxim = max(maxim1+bookings[i],maxim2)
        maxim1 = maxim2
        maxim2 = maxim
    return maxim2

print(findMax([5,6,3,1]))
print(findMax([6,5,1,3]))
print(findMax([6, 5, 0, 1, 0, 9]))
print(findMax([5, 1, 1, 5]))
print(findMax([3,6,4]))
print(findMax([4, 10, 3, 1, 5]))