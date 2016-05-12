function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// init the side nav
$('.button-collapse').sideNav();

var foot_height = 0;
var window_height = window_height = window.innerHeight;

var refresh_height = function($body, new_height){
    // Top nav is 64px
    if (new_height == window_height) return;
    window_height = new_height;
    $body.transition({
        height: window_height - 64 - foot_height
    });
};

$(document).ready(function(){
    // stretch the main body to fill screen
    foot_height = $( 'footer', this ).outerHeight();
    $body = $('#main_container', this);
    $body.css('bottom', foot_height);
    $(window).resize(function(){
        refresh_height($body, window.innerHeight);
    });
});
