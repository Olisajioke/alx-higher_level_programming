/* eslint-disable */
// Fetches the translation of "hello" and displays it in DIV#hello
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
/* eslint-enable */
