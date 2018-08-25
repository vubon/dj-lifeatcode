// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, vendor/assets/javascripts,
// or any plugin's vendor/assets/javascripts directory can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file.
//
// Read Sprockets README (https://github.com/rails/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery
//= require jquery_ujs
//= require jquery-ui
//= require bootstrap-sprockets
//= require toastr
//= require_tree .

(function ($) {
    $(document).ready(function () {

        // hide .navbar first
        $(".navbar").hide();

        // fade in .navbar
        $(function () {
            $(window).scroll(function () {
                // set distance user needs to scroll before we fadeIn navbar
                if ($(this).scrollTop() > 100) {
                    $('.navbar').fadeIn();
                } else {
                    $('.navbar').fadeOut();
                }
            });


        });



        function scrollVubon() {
            $('a').click(function () {
                //Toggle Class
                $(".active").removeClass("active");
                $(this).closest('li').addClass("active");
                var theClass = $(this).attr("class");
                $('.' + theClass).parent('li').addClass('active');
                //Animate
                $('html, body').stop().animate({
                    scrollTop: $($(this).attr('href')).offset().top - 50
                }, 1000);
                return false;
            });
            $('.scrollTop a').scrollTop();
        }

        scrollVubon();
        // price slider
        $(function () {
            $(".slider-range").slider({
                range: true,
                min: 20,
                max: 10000,
                values: [20, 10000 ],
                slide: function (event, ui) {
                    $("#amount").val("$" + ui.values[0]);
                }
            });
            $("#amount").val("$" + $(".slider-range").slider("values", 0));
        });

        // tosta notification
        toastr.options.onHidden = {

            "closeButton": true,
            "debug": false,
            "newestOnTop": false,
            "progressBar": true,
            "positionClass": "toast-top-right",
            "preventDuplicates": false,
            "onclick": null,
            "showDuration": "300",
            "hideDuration": "1000",
            "timeOut": "5000",
            "extendedTimeOut": "1000",
            "showEasing": "swing",
            "hideEasing": "linear",
            "showMethod": "fadeIn",
            "hideMethod": "fadeOut"
        }
    });

}(jQuery));


	