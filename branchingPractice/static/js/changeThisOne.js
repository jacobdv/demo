yourName = 'Testing';

changingElement = d3.select('#changingElement');
changingElement.text(yourName);

div = d3.select('#changingElement');
div.on('click', function() {
    // Line 9 is a ternary statement. It is the same as the commented chunk of code below.
    changingElement.text() == yourName? changingElement.text('---') : changingElement.text(yourName);

    // if (changingElement.text() == yourName) {
    //     changingElement.text(yourName);
    // } else {
    //     changingElement.text('---');
    // }
});