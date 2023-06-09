// window.addEventListener('scroll', function() {
//   var addButton = document.getElementById('add_button123');
//   var currentPosition = window.pageYOffset; // current scroll position
//
//   if (currentPosition > 0) {
//     addButton.style.bottom = '0px'; // moves the button to the bottom
//   } else {
//     addButton.style.bottom = '-50px'; // hides the button below the viewport
//   }
// });

$(document).ready(function(){
    var buttonTop = $('#add_button123').offset().top;

    $(window).scroll(function(){
        if ($(window).scrollTop() > buttonTop){
            $('#add_button123').addClass('sticky');
        } else {
            $('#add_button123').removeClass('sticky');
        }
    });
});
