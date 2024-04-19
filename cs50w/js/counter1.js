let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function () {
    // Eventlistener takes in two inputs, the event to listen for and the function to apply when event is triggered
    document.querySelector('button').onclick = count;
    
    // We are intentionally letting the count function be called every 1000 millisecond i.e. one second
    window.setInterval(count, 1000);
});