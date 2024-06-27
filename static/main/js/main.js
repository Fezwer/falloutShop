document.addEventListener("DOMContentLoaded", function() {
    var hoverSound = document.getElementById('hover-sound');
    var links = document.querySelectorAll('header a');
    var buttons = document.querySelectorAll('button');

    links.forEach(function(link) {
        link.addEventListener('mouseenter', function() {
            hoverSound.play();
        });
    });

    buttons.forEach(function(button) {
        button.addEventListener('mouseenter', function() {
            hoverSound.play();
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};