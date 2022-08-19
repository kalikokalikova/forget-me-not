const today= new Date().getDay();
let weekday= ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
const dayTwo = weekday[(today+1)%7]
const dayThree = weekday[(today+2)%7]
const dayFour = weekday[(today+3)%7]
const dayFive = weekday[(today+4)%7]

function showDays(){
    document.getElementById("current_date").innerHTML = new Date();
    document.getElementById("day2_date").innerHTML = dayTwo;
    document.getElementById("day3_date").innerHTML = dayThree;
    document.getElementById("day4_date").innerHTML = dayFour;
    document.getElementById("day5_date").innerHTML = dayFive;
}

showDays()


