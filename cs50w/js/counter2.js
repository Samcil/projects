// The counter function we had previouslys was not stateful. i.e. whenever we refresh the page the counter begins from zero
// We can make our pages stateful with access to an object called localStorage
// it comes with two methods called getItem and setItem which makes our pages stateful

if (!localStorage.getItem('counter')){
    // If there is no variable called counter, create it and initialize it to zero
    localStorage.setItem('counter', 0);
}

function count() {
    // grab the value from local storage
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    // increment counter in local storage to the new value
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    // Eventlistener takes in two inputs, the event to listen for and the function to apply when event is triggered
    document.querySelector('button').onclick = count;
    
    // We are intentionally letting the count function be called every 1000 millisecond i.e. one second
    window.setInterval(count, 1000);
});