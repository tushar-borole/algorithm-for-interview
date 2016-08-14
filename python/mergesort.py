def mergeSort(toSort):
    if len(toSort) <= 1:
        return toSort
 
    mIndex = len(toSort) / 2
    left = mergeSort(toSort[:mIndex])
    #print "left "+str(left)
    right = mergeSort(toSort[mIndex:])
    #print "right "+str(right)
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   #left[0] and right[0] is compared becasue 0 th elemt is smaled between two, as it is sorted and merged into single
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    #print "result "+str(result)
    if len(left) > 0:
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
 
    return result
 
def main():
    l = [1, 6, 7, 2, 76, 45, 23, 4, 8, 12, 11]
    sortedList = mergeSort(l)
    print sortedList
 
if __name__ == '__main__':
    main()