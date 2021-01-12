document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById('complete-order').addEventListener('click', () => complete_order());
    
});
function complete_order() {
    const complete_button = document.getElementById('complete-order');
    complete_button.innerHTML = 'Completed';
    complete_button.setAttribute('class', 'btn btn-outline-secondary');
    complete_button.setAttribute('id', 'completed');

    document.getElementById('completed').removeEventListener('click', () => complete_order());
    var order_id = document.getElementById('orderID').dataset.orderid;
    mark_as_completed(order_id);
}

function mark_as_completed(order_id) {

    fetch(`/completeOrder/${order_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            active: false
        })
    });

}

 