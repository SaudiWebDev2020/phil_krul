function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    console.log('cookieValue', cookieValue);
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$.ajax({
    url: 'process',
    method: 'post',
    data: {
        'first_name': 'Phil',
        'last_name': 'Krull'
    },
    headers:{"X-CSRFToken": csrftoken},
    success: function(response) {
        console.log(response)
    }
})