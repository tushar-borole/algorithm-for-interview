def binary_search(data,search_element):
    if len(data) <= 1:
        return False

    mid = len(data)/2
    center_element = data[mid]

    if center_element== search_element:
        return True
    elif data < center_element:
        return binary_search(data[:mid],search_element)
    elif data > center_element:
        return binary_search(data[mid:],search_element)

listdata=[1,2,3,4,5,6,7,8,0]
print binary_search(listdata ,78)