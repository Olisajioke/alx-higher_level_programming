// Adds a new <li> element to UL.my_list when clicking on DIV#add_item

$('#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
