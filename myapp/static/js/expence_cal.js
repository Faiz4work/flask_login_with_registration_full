

var tVal = document.getElementById("total_fuel_value")
// console.log(tVal)


var fuel_values = document.getElementsByClassName('fuel_value')
// alert(fuel_values)

var a = []

for (let index = 0; index < fuel_values.length; index++) {
    var element = fuel_values[index];
    a.push(element.innerHTML)  
}
const sum = a.reduce((partialSum, b) => partialSum + parseInt(b), 0);

tVal.innerHTML= sum


// Oil value

var oVal = document.getElementById("total_oil_value")
// console.log(oVal)

var oil_values = document.getElementsByClassName('oil_value')
// alert(Oil_values)

var b = []

for (let index = 0; index < oil_values.length; index++) {
    var element = oil_values[index];
    b.push(element.innerHTML)  
}
const sum_2 = b.reduce((partialSum, c) => partialSum + parseInt(c), 0);

oVal.innerHTML= sum_2


// total_Maintanance

var mVal = document.getElementById("total_Maintanance")
// console.log(oVal)

var total_maintanance = document.getElementsByClassName('total_maintanance')
// alert(Oil_values)

var c = []

for (let index = 0; index < total_Maintanance.length; index++) {
    var element = total_Maintanance[index];
    c.push(element.innerHTML)  
}
const sum_3 = c.reduce((partialSum, d) => partialSum + parseInt(d), 0);

mVal.innerHTML= sum_3
