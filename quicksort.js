function quicksort(data) {
    if (data.length == 0) return [];
  

  var left = [], right = [], pivot = data[0];
  
    for (var i = 1; i < data.length; i++) {
        if(data[i] < pivot)
            left.push(data[i])
        else
            right.push(data[i]);
    }
    left=quicksort(left) //recursion till left length becomes 0
    right=quicksort(right) //recursion till right length becomes 0
  
    return left.concat(pivot, right);
}


var a=[3,9,8,4,3,9,5,3]
sorted=quicksort(a)
console.log(sorted)

