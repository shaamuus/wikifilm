 $(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.datepicker').datepicker({
        format: "yyyy",
        minDate: 01-01-1900,
        maxDate: 01-01-2050,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
  });