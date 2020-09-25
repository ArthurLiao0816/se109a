//這是迴圈版的二元搜尋法 ~
function search(a, o) {
    var n = a.length
    var from = 0
    var to = n
    
    while (true){
        if (from > to) return null
        var mid = Math.floor((from + to)/2)
        if (a[mid] === o)
            return mid
        else if (o > a[mid]){
            from = mid + 1;
        }
        else {// o < a[mid]
            to = mid - 1;
        }
    }
}
  
var t = search([1, 3, 4, 6, 7, 8], 4)
console.log('t=', t)
var t = search([1, 3, 4, 6, 7, 8], 5)
console.log('t=', t)
var t = search([1, 3, 4, 6, 7, 8], 8)
console.log('t=', t)
var t = search([1, 3, 4, 6, 7, 8], 9)
console.log('t=', t)
  