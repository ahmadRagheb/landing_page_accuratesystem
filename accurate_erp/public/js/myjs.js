
$(function () {
  'use strict';


    // scrollToTop
    $(window).on("scroll", function(){
      if($(this).scrollTop() > 2000 ) {
        if($('.scrollToTop').is(':hidden')){
          $('.scrollToTop').fadeIn(500);
        }
      } else {
        $('.scrollToTop').fadeOut(100);
      }
    });

    // Click On scrollToTop
    $('.scrollToTop').click(function(e){
      e.preventDefault();
      $('html, body').animate({
        scrollTop: 0
      }, 1000);
    });

   // Smothly Scroll To Element
    $('.navbar li a').click(function (e) {

      e.preventDefault();

      $('html, body').animate({

        scrollTop: $('#' + $(this).data('scroll')).offset().top

      }, 2000);

    });

    
});
