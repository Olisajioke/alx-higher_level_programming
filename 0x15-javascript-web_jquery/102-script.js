/* eslint-disable */
$(document).ready(function () {
  // Listens for a click on the Translate button
  $('#btn_translate').click(function () {
    // Retrieves the language code entered by the user
    const languageCode = $('#language_code').val();
    
    // Fetches the translation of "Hello" based on the entered language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      // Displays the translated "Hello" in the specified HTML tag
      $('#hello').text(data.hello);
    });
  });
});
/* eslint-enable */
