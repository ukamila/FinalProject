document.addEventListener('DOMContentLoaded', function() {

    //clicking on checkout should hide order view and show checkout window
    document.querySelector('#checkout-button').addEventListener('click', () => load_checkout());
    //clicking on back to order should hide checkout window and show the order
    document.querySelector('#back-to-order').addEventListener('click', () => load_myorder());

    //by default this page should display user's order
    load_myorder();
});

function load_myorder() {

    document.querySelector('#my_order').style.display = 'block';
    document.querySelector('#checkout').style.display = 'none';
    document.querySelector('#final_checkout').style.display = 'none';
}

function load_checkout() {

    document.querySelector('#checkout').style.display = 'block';
    document.querySelector('#my_order').style.display = 'none';
    document.querySelector('#final_checkout').style.display = 'none';

    let price = 0;
    document.querySelectorAll('#price-per-one').forEach( div => {
        price += parseInt(div.innerHTML)
    });

    document.getElementById('total-price').innerHTML = price + "$";

    document.querySelector('#checkout-form').onsubmit = submit_checkout;
}

function submit_checkout() {

    const address = document.querySelector('#order-address').value;
    var price = document.getElementById('total-price').innerHTML;
    const total_price = parseInt(price.split('$')[0])

    checkout(address, total_price);
    return false;
}

function checkout(address, total_price) {

    fetch('/checkout', {
        method: 'POST',
        body: JSON.stringify({
            address: address,
            total_price: total_price,
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    });

    document.querySelector('#final_checkout').style.display = 'block';
    document.querySelector('#my_order').style.display = 'none';
    document.querySelector('#checkout').style.display = 'none';    
}