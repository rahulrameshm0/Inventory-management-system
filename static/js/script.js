const button = document.querySelector('.btn');

button.addEventListener('click', function(e){
    e.preventDefault()
    button.textContent = "Loading..."
    console.log('click')
});