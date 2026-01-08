const button = document.querySelector('.btn');
const subtract = document.querySelector('.minus');
const add = document.querySelector('.plus');
const input = document.querySelector('.qty-input');
const alerting = document.querySelector('.alerting');
const dashboardButton = document.querySelector('.btn-1');

if(button){
    button.addEventListener('click', (e) => {
        e.preventDefault()
        button.textContent = "Loading..."
        console.log('click')
    });
}

if (add && input){
    add.addEventListener('click', (e) => {
        e.preventDefault()
        input.value = parseInt(input.value) + 1;
    });
}

if (subtract && input){
    subtract.addEventListener('click', (e) => {
        e.preventDefault()
        if (input.value > 0){
            input.value = parseInt(input.value) - 1;
        }
    });

}

if (dashboardButton){
    dashboardButton.addEventListener('click',(e) => {
        e.preventDefault()
        window.location.href = dashboardButton.dataset.url;
        // console.log('click')
});
}