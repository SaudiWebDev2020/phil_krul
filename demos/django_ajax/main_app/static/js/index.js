// -----------------------------------------------------------------------------------------------
// https://docs.djangoproject.com/en/2.2/ref/csrf/#ajax
// used to retreive the CSRF token set as a cookie
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
// -----------------------------------------------------------------------------------------------

// AJAX request
xhttp.open("post", "process", true);
// set token header
xhttp.setRequestHeader("X-CSRFToken", csrftoken);
// set form datatype
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
// send post info
xhttp.send(`first_name=Phil&last_name=Krull&csrfmiddlewaretoken=${csrftoken}`);

const xhttp = new XMLHttpRequest();
// handle async response
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
    }
}