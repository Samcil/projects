let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
    
    if (counter % 10 === 0)
    {
        // This is JS' way of writing formatted strings
        alert(`Count is now ${counter}`);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    // Eventlistener takes in two inputs, the event to listen for and the function to apply when event is triggered
    document.querySelector('button').onclick = count;
});