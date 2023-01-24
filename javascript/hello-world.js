const helloWorld = function(name) {
    if (name === undefined) {
        name = "World";
    }
    console.log(`Hello ${name}!`)
};

helloWorld(); // Hello World!
helloWorld('Amy'); // Hello Amy!