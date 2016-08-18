var main = function() {

        /*  var showTab = function(tab) {
                console.log("showTab");
                $('.pane').hide();
                $('mytab.active').removeClass('active');
                $(tab).addClass('active').blur();
                var panel = $(tab).attr('href');
                $(pane).fadeIN(500);

*/



        // функция выделяет по клику мышки  выбранный топик (подменю в TAB) 
        $('.tab-pane li').click(function() {
            $this = $(this);
            console.log($this);
            var a = $($this > 'a .pane');
            console.log(a);
            $(a).removeClass('panactive');
            $(a).addClass('panactive').blur();
            $($this > '.submenu').fadeToggle("slow", "linear");
            // var submenu = $this.attr('.submenu');
            // console.log(submenu);

        }); //end click tabpanel a




        $("#navigation").navPlugin({
            'itemWidth': 253,
            'itemHeight': 'auto',
            'navEffect': "slide",
            'speed': 600
        });

    } //end main

$(document).ready(main); //end ready function