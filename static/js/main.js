//removes classes to make it responsive on mobile view
$(window).on('resize load', function() {
  if ($(window).width() <= 768) { 
    $("#mobile").removeClass("row");
    $("#mobile").removeClass("row-cols-3")
  }
});