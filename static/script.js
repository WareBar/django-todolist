function RealTime(){

    // gets the date and time
    let date = new Date();
    let dateTime = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`

    // get the node
    let todayDate = document.getElementById('todayDate');
    let currentTime = document.getElementById('currentTime');

    // apply the date and time to each node
    todayDate.innerHTML = date.toDateString()
    currentTime.innerHTML = dateTime

    // check the value in console para if may problem ay madebug agad

}



setInterval(RealTime, 1000)