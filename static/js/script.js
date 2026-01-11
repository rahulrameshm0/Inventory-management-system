const button = document.querySelector('.btn');
const subtract = document.querySelector('.minus');
const add = document.querySelector('.plus');
const input = document.querySelector('.qty-input');
const alerting = document.querySelector('.alerting');
const dashboardButton = document.querySelector('.btn-1');
const form = document.getElementById('product-form');

let popup = document.getElementById('popup');
let closepopup = document.getElementById('closePopup');


if(button){
    button.addEventListener('click', () => {
        button.textContent = "Loading..."
        console.log('click')
    });
}

if (add && input){
    add.addEventListener('click', () => {
        input.value = parseInt(input.value) + 1;
    });
}

if (subtract && input){
    subtract.addEventListener('click', () => {
        if (input.value > 0){
            input.value = parseInt(input.value) - 1;
        }
    });

}

// if (dashboardButton){
//     dashboardButton.addEventListener('click',(e) => {
//         e.preventDefault()
//         window.location.href = dashboardButton.dataset.url;
//         // console.log('click')
// });
// }


function openPopup(btn = null) {
    popup.classList.add('open-popup');

    // ADD MODE
    if (!btn) {
        form.reset();
        document.getElementById('quantity').value = 0;
        return;
    }

    // EDIT MODE
    document.getElementById('product_id').value = btn.dataset.product_id;
    document.getElementById('quantity').value = btn.dataset.qty;
    document.getElementById('status').value = btn.dataset.status;
    document.getElementById('product_type').value = btn.dataset.type;
    document.getElementById('vendor_name').value = btn.dataset.vendor_name;
}

function closePopup(){   
    popup.classList.remove('open-popup');
};
