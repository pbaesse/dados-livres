$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});


$(document).ready(function () {
  var titles = [

  ];

  function loadTitles() {
    $.getJSON('/_autocomplete', function (data, status, xhr) {
      for (var i = 0; i < data.length; i++) {
        titles.push(data[i].title);
      }
    });
  };

  loadTitles();

  $('#autocomplete').autocomplete({
    source: titles
  });
});


$(document).ready(function () {
  var tags = [

  ];

  function loadTags() {
    $.getJSON('/_tag', function (data, status, xhr) {
      for (var i = 0; i < data.length; i++) {
        tags.push(data[i].tag);
      }
    });
  };

  loadTags();

});
