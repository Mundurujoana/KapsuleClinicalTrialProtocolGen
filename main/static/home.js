// Parse JSON data
// let data = JSON.parse(jsonData);
let data = '{{ answer }}';

// Assign data to variables
let background = data.background;
let objectives = data.objectives;
let methods = data.methods;
let expectedResults = data.expectedResults;

// Insert data into HTML
document.getElementById("background").innerHTML = background;
document.getElementById("objectives").innerHTML = objectives.join("<li>");
document.getElementById("methods").innerHTML = methods;
document.getElementById("expected-results").innerHTML = expectedResults;
