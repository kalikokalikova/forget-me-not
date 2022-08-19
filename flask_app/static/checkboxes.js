console.log("javascript is running!")

// When the DOM content has loaded
document.addEventListener("DOMContentLoaded", function(){
    // if there are no items on the page
    if (document.querySelectorAll("input[type='checkbox']").length == 0) {
        // do not show the UNCHECK ITEMS button
        document.getElementById('check-uncheck').style.display = "none";
    };
});

// When input checkbox is clicked, set the value of the hidden input so unchecked inboxes get posted in the form
function toggleCheckbox(element) {
    element.previousElementSibling.value = 1-element.previousElementSibling.value
};

function checkUncheckItems(el) {
    // get all checkbox inputs on the page
    var inputs = document.querySelectorAll("input[type='checkbox']");

    // if the button says 'Uncheck All Items'
    if (el.textContent == 'Uncheck All Items') { 
        for(var i = 0; i < inputs.length; i++) { // loop through checkbox inputs
            inputs[i].checked = false; // set checkbox to unchecked
            inputs[i].previousElementSibling.value = 0; // set value of hidden input to deal with the unchecked form post problem
        };
        el.textContent = "Check All Items" // Update text on button
        return; // bail out of function before more code runs and messes everything up
    };

    if (el.textContent == "Check All Items") {
        for(var i = 0; i < inputs.length; i++) {
            inputs[i].checked = true;
            inputs[i].previousElementSibling.value = 1;
        };
        el.textContent = "Uncheck All Items"
        return;
    };
};