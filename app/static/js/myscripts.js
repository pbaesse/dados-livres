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
  var tagsList = [

  ];

  var split = function(val) {
      return val.split(",");
  };

  var extractLast = function(term) {
      return split(term).pop();
  };

  function loadTags() {
    $.getJSON('/_tag', function (data, status, xhr) {
      for (var i = 0; i < data.length; i++) {
        tagsList.push(data[i].keyword);
      }
    });
  };

  loadTags();

  $("#tag").on("keydown", function(event) {
    if (event.keyCode === $.ui.keyCode.TAB && $(this).autocomplete("instance").menu.active) {
      event.preventDefault();
    }
  }).autocomplete({
    source: function(request, response) {
      response( $.ui.autocomplete.filter(
        tagsList, extractLast(request.term)));
    },
    focus: function() {
      return false;
    },
    select: function(event, ui ) {
      var terms = split(this.value);
      terms.pop();
      terms.push(ui.item.value);
      terms.push("");
      this.value = terms.join(", ");
      return false;
    }
  });
});
