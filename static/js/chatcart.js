// Assuming you have defined 'user' and 'csrftoken' variables somewhere in your code
// For example:
// var user = 'AnonymousUser';
// var csrftoken = 'your-csrf-token-value';

// Use querySelectorAll to select elements by class name, which returns a NodeList.
var updateBtns = document.querySelectorAll('.update-cart');

updateBtns.forEach(function(button) {
    button.addEventListener('click', function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action:', action);

        console.log('USER:', user);
        if (user === 'AnonymousUser') {
            console.log('Not logged in');
        } else {
            updateUserOrder(productId, action);
        }
    });
});

function updateUserOrder(productId, action) {
    console.log('User is logged in, sending data...');

    var url = 'update_item/';

    // Use try-catch for error handling with fetch.
    try {
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })
        })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then((data) => {
            console.log('data:', data);
            location.reload();
        })
        .catch((error) => {
            console.error('Error:', error);
            // Handle errors here, e.g., display an error message to the user.
        });
    } catch (error) {
        console.error('Error:', error);
        // Handle errors here, e.g., display an error message to the user.
    }
}
