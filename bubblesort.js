var array = [
  3,
  1,
  18,
  90,
  8,
  10,
  55,
  30,
  20,
  25
]
var swapped = false
while (true) {
  var swapped=false
  for (i = 0; i <= array.length-2; i++) {
    console.log(array[i])
    console.log(array[i+1])
    if (array[i] > array[i + 1]) {
      var temp = array[i]
      array[i] = array[i + 1]
      array[i + 1] = temp
      swapped=true
    }
  }
  if(swapped==false){
  break;
  }
}
console.log(array)
