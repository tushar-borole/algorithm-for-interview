var array = [
  1,
  5,
  10,
  15,
  20,
  25,
  30,
  35,
  40,
  45,
  50,
  55,
  60,
  65,
  70,
  75,
  80,
  85,
  90,
  95,
  100
]
while (array.length != 0) {
  search = 15
  console.log(array)
  var i = Math.round(array.length / 2)
  console.log(i)
  if (search > array[i]) {
    array = array.slice(i, array.length)
  } else if (search < array[i]) {
    array = array.slice(0, i)
  } else if (array[i] == search) {
    
    alert('value found')
    break
    
    
  }else{
  break
  }
}
