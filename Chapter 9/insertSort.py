def find_indextoinsert(lst, data):
    if len(lst) == 0 or lst[0] > data:
        return 0
    return 1+find_indextoinsert(lst[1:], data)

def InsertionSort(left, right):
    if len(right) == 0:
        return left
    data = right.pop(0)
    index = find_indextoinsert(left, data)
    left.insert(index, data)
    print(f"insert {data} at index {index} : {left} ", end="")
    if len(right) != 0:
        print(right)
    return InsertionSort(left, right)

com = list(map(int, input("Enter Input : ").split()))
left = [com.pop(0)]
right = com
print(f"\nsorted\n{InsertionSort(left, right)}")
