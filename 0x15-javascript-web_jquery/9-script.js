$(document).ready(function () {
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (response) {
    $('DIV#hello').html(response.hello)
})
});
