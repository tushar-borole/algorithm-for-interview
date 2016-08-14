def quickSort(toSort):
    if len(toSort) <= 1:
        return toSort
 
    end = len(toSort) - 1
    pivot = toSort[end]
 
    low = []
    high = []
 
    for num in toSort[:end]:
        if num <= pivot:
            low.append(num)
        else:
            high.append(num)
    #print pivot        
    #print low
    sortedList = quickSort(low)
    #print "Low sorting done"
    #print sortedList
    sortedList.append(pivot)
    sortedList.extend(quickSort(high))
    #print "High sorting done"
    return sortedList
 
def main():
    l = [1,3,6,9, 200, 5678, 76, 45, 23, 44, 81, 121, 11]
    sortedList = quickSort(l)
    print sortedList
 
if __name__ == '__main__':
    main()

#O(n log(n))