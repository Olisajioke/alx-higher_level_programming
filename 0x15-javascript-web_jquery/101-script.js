/* eslint-disable */
$(document).ready(function () {
  // Adds a new <li> element to the list when clicking on DIV#add_item
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Removes the last <li> element from the list when clicking on DIV#remove_item
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // Removes all elements from the list when clicking on DIV#clear_list
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
/* eslint-enable */
