const button = document.querySelector('.btn');
const subtract = document.querySelector('.minus');
const add = document.querySelector('.plus');
const input = document.querySelector('.qty-input');

button.addEventListener('click', () => {
    button.textContent = "Loading..."
    console.log('click')
});

add.addEventListener('click', (e) => {
    e.preventDefault()
    input.value = parseInt(input.value) + 1;
});

subtract.addEventListener('click', (e) => {
    e.preventDefault()
    if (input.value > 0){
        input.value = parseInt(input.value) - 1;
    }
});
