/* eslint-disable */
$(document).ready(function () {
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  // Fetches translation when the Translate button is clicked
  $('#btn_translate').click(fetchTranslation);

  // Fetches translation when Enter key is pressed in the language code input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
/* eslint-enable */
