const purchaseButton = document.getElementById('purchaseButton');

purchaseButton.addEventListener('click', function () {
    const csrftoken = getCookie('csrftoken'); // Получаем токен CSRF для защиты от межсайтовой подделки запроса

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'cart', true); // Отправляем POST запрос на сервер
    xhr.setRequestHeader('X-CSRFToken', csrftoken); // Устанавливаем токен CSRF в заголовке запроса
    xhr.send(); // Отправляем запрос на сервер без тела, так как для подтверждения покупки может не потребоваться отправлять данные

    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.response);
            alert(response.message); // Обрабатываем успешный ответ
        } else {
            alert('Ошибка. Статус:', xhr.status); // Обрабатываем ошибку
        }
    };

});


const delReservButtons = document.querySelectorAll('.delReservButton');

delReservButtons.forEach(button => {
    button.addEventListener('click', function (event) {
        const csrftoken = getCookie('csrftoken');
        event.preventDefault(); // Отменяем стандартное действие отправки формы

        var delxhr = new XMLHttpRequest();
        var reservationId = this.parentElement.getAttribute('action').split('/').reverse()[1]; // Получаем ID резервации из URL
        delxhr.open('POST', `delete_reservations/${reservationId}/`, true);
        delxhr.setRequestHeader('X-CSRFToken', csrftoken); // Устанавливаем токен CSRF в заголовке запроса
        delxhr.send();

        // Определяем функцию обратного вызова для обработки ответа
        delxhr.onload = function () {
            if (delxhr.status === 200) {
                var response = JSON.parse(delxhr.responseText);
                alert(response.message);
                window.location.reload();
            } else {
                alert('Произошла ошибка. Пожалуйста, попробуйте снова.');
            }
        };
    });
});
