function mergeSort (arr) {    
    if (arr.length < 2) return arr;
    
    var mid = Math.floor(arr.length /2);
    var subLeft = mergeSort(arr.slice(0,mid));
    var subRight = mergeSort(arr.slice(mid));
    
    return merge(subLeft, subRight);
}

function merge (a,b) {
    var result = [];
    while (a.length >0 && b.length >0)
        result.push(a[0] < b[0]? a.shift() : b.shift());
    return result.concat(a.length? a : b);
}

var test = [1,2,9,3,2,5,14,0];
console.log(mergeSort(test)); // -> [0, 1, 2, 2, 3, 5, 9, 14]
