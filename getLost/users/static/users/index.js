function pricePasswordInputPage() {
    $('.input-password').val('');

    $('#PricePasswordForm').css("display", "block");
    $('#ChangePriceForm').css("display", "none");

    $('#exampleModal3').on('shown.bs.modal', function (e) {
        // e.preventDefault();
        console.log("PAGE 1");
        $('#price-password-input').focus();
    });
}
function priceInputPage() {
    $('.price-change').val('');

    $('#PricePasswordForm').css("display", "none");
    $('#ChangePriceForm').css("display", "block");

    $('.price-change').focus();
    console.log("PAGE 2");
}
function bedPasswordInputPage() {
    $('.total-beds-input-password').val('');

    $('#TotalBedsPasswordForm').css("display", "block");
    $('#ChangeTotalBedsForm').css("display", "none");

    $('#exampleModal4').on('shown.bs.modal', function () {
        console.log("PAGE 1");
        $('.total-beds-input-password').focus();
    });
}
function bedInputPage() {
    $('.total-beds-change').val('');

    $('#TotalBedsPasswordForm').css("display", "none");
    $('#ChangeTotalBedsForm').css("display", "block");

    $('.total-beds-change').focus();
    console.log("PAGE 2");
}

jQuery(document).ready(function () {
    function refresh() {
        console.log("hello");
        // old = $('#reservation-box').html();
        // console.log("THE OLD");
        // console.log(old);
        $.ajax({
            type: 'GET',
            url: "/dashboard/",
            success: function (data) {
                var html = $('<div />').html(data).find('#reservation-box').html();  // THIS WORKS!!!!
                $('#reservation-box').load(location.href + " #reservation-box>*", "");
                $('#confirmed-box').load(location.href + " #confirmed-box>*", "");

                // $('#main').load(location.href + " #main>*", "");
                // $('#exampleModal').load(location.href + " #exampleModal>*", "");
                // $('#exampleModal2').load(location.href + " #exampleModal2>*", "");

                // $('#reservation-box').html(data);
                // $('#eservation-box').load(' #eservation-box', function () { $(this).children().unwrap() })
                // console.log(data);
                // var html = $(data).find('#reservation-box').html();
                // console.log("THE NEW");
                // console.log(html);
                // $('#reservation-box').load('#reservation-box');
                // var html = $(data).filter('#reservation-box').html();
                // console.log(html);
                // $('#reservation-box').html(html);
                
            }
        });
        setTimeout(refresh, 20000);
    }
    refresh();
    

    // State Variables
    var variable;
    var months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];
    // -------------------------------------------------
    // DATEPICKER SECTION ------------------------------
    // -------------------------------------------------
    $('.dp-button').click(function () {
        myFunction(this);
        variable = $(this).attr('id');
        // console.log(variable);
    });
    function myFunction(element) {
        console.log(element);
        console.log(element.id);
    };
    function getMonthName(month) {
        return months[month];
    }
    function getFormattedDate(date) {
        let year = date.getFullYear();
        let month = (1 + date.getMonth()).toString().padStart(2, '0');
        let day = date.getDate().toString().padStart(2, '0');

        return month + '-' + day + '-' + year;
    }
    function getFormattedDateString(date) {
        let year = date.getFullYear();
        let month = getMonthName(date.getMonth());
        let day = date.getDate();

        if (day == 1) {
            day = day + "st";
        }
        else if (day == 2) {
            day = day + "nd";
        }
        else if (day == 3) {
            day = day + "rd";
        }
        else {
            day = day + "th";
        }
        return day + ' ' + month + ' ' + year;
    }
    $('#datepicker').datepicker({
        format: 'mm-dd-yyyy',
        container: $(document.activeElement).parent(),
        autoHide: true
    }).on('pick.datepicker', function (e) {
        e.preventDefault(); // Prevent to pick the date
        var date = $('#datepicker').datepicker('getDate', true);
        console.log("the raw date is " + date);
        // $("input[name='something']").val(date);
        $("#exampleModal5").modal("show");
        // var resDate = new Date($('.history-item').data('date'));   // ONLY GETS FIRST RESERVATION DATE
        // console.log("The resDate is:  " + resDate);
        var newDate = new Date(date.replace(/-/g, "/")); //.replace(/\s/, 'T') + 'Z'
        console.log("The Date is " + newDate);
        newDate = getFormattedDateString(newDate);
        console.log(newDate);
        console.log("HELLO");
        var modal = $('#exampleModal5');
        // modal.find('.header-date').html(newDate);

        modal.find('#datepicker-modal').val(newDate);

        $('#history-container').find('.history-item').each(function () {
            // var innerDivId = $(this).attr('id');
            var dataDate = new Date($(this).data('date'));
            dataDate = getFormattedDate(dataDate);
         
            if (dataDate == date) {
                $(this).css("display", "block");
            }
            else {
                $(this).css("display", "none");
            }
        });     
    });

    $('#datepicker-modal').datepicker({
        format: 'mm-dd-yyyy',
        autoHide: true,
        container: $(document.activeElement).parent(),
        zIndex: 90000
    }).on('pick.datepicker', function (e) {
        e.preventDefault();
        var myDatePicker = $('#datepicker-modal').datepicker({});
        var modalDate = $('#datepicker-modal').datepicker('getDate', true);
        var newDate = new Date(modalDate.replace(/-/g, "/"));
        newDate = getFormattedDateString(newDate);
        $("#datepicker-modal").val(newDate);

        $('#history-container').find('.history-item').each(function () {
            var innerDivId = $(this).attr('id');
            var dataDate = new Date($(this).data('date')); //.replace(/-/g, "/")
            dataDate = getFormattedDate(dataDate);
            if (dataDate == modalDate) {
                $(this).css("display", "block");
            }
            else {
                $(this).css("display", "none");
            }
        });        
    });
    var keyword = "";
    $("#search-name-field").keyup(function () {
        keyword = $(this).val();
        console.log(keyword);
        var count = 0;
        $('#history-container').find('.history-item').each(function () {

            console.log("test variable check: " + variable);
            var firstDate = $('#datepicker').datepicker('getDate', true);
            firstDate = new Date(firstDate);
            firstDate = getFormattedDate(firstDate);
            var modalDate = $('#datepicker-modal').datepicker('getDate', true);
            var newDate = new Date(modalDate);
            newDate = getFormattedDate(newDate);
            var dataDate = new Date($(this).data('date'));
            dataDate = getFormattedDate(dataDate);
            var parentId = $(this).attr('id');
            var childDiv = $(this).find('.reservation-customer');
            var childId = $(this).find('.reservation-customer').attr('id');
            var name = $(childDiv).html().toLowerCase();
            var filter = keyword.toLowerCase();
            console.log("Main Date: " + dataDate);
            console.log("first Date: " + firstDate);
            console.log("modal Date: " + modalDate);

            if (dataDate == firstDate && variable == 'datepicker') {
                $(this).css("display", "block");
                console.log("PART 1");
                if ($(childDiv).text().search(new RegExp(filter, "i")) < 0) {
                    // $(this).hide();  // MY CHANGE
                    $(this).css("display", "none");
                    // Show the list item if the phrase matches and increase the count by 1     
                }
                else {
                    // $(this).show(); // MY CHANGE
                    $(this).css("display", "block");
                    count++;
                }
            }
            else if (dataDate == modalDate && variable == 'datepicker-modal') {
                $(this).css("display", "block");
                console.log("PART 2");
                if ($(childDiv).text().search(new RegExp(filter, "i")) < 0) {
                    // $(this).hide();  // MY CHANGE
                    $(this).css("display", "none");
                    // Show the list item if the phrase matches and increase the count by 1             
                }
                else {
                    // $(this).show(); // MY CHANGE
                    $(this).css("display", "block");
                    count++;
                }
            }
            else {
                $(this).css("display", "none");
            }
        });
    });
    // -------------------------------------------------
    // CHANGE PRICE MODAL ------------------------------
    // -------------------------------------------------
    $('body').on('click', '.open-modal-change-price', function (e) {
        e.preventDefault();
        function isEmpty(obj) {
            for (var key in obj) {
                if (obj.hasOwnProperty(key))
                    return false;
            }
            return true;
        }
        var currentlocation = window.location.href;
        var price = $(".price-text").data('price');
        var password = $(".input-password").data('password');

        // SET MODAL START PAGE
        pricePasswordInputPage();
        $('#next-btn').on('click', function (e) {
            e.preventDefault();
            var passwordForm = $('#PricePasswordForm');
            console.log("Check password button pressed");
            $.ajax({
                type: passwordForm.attr('method'),
                url: passwordForm.attr('action'),
                data: passwordForm.serialize(),
                success: function (data) {
                    // $("#PricePasswordForm")[0].reset();
                    if ($(data).find(".check-div").html() == 'true') {
                        console.log("it is TRUE and we did it bro");
                        priceInputPage();
                    }
                    else {
                        console.log("it is FALSE and we still did it");
                        $('#price-password-input').addClass('animated shake');
                        $('#price-password-input').val('');
                        $('#price-password-input').focus();
                    }
                },
                error: function (data) {
                    console.log("its super duper duper wrong");
                    console.log(passwordForm.serialize());
                },
            });
            $('#price-password-input').removeClass('animated shake');
            return false;
            // var inputPassword = $(".input-password").val();
            // if (password == inputPassword) {
            //     console.log("it worked");
            //     priceInputPage();
            // }
            // else {
            //     console.log("FALSE");
            //     // ERROR MESSAGE
            // }
        });
        $('.input-password').keypress(function (e) {
            
            if (e.which == 13) {//Enter key pressed
                $('#next-btn').click();//Trigger search button click event
                e.preventDefault();
            }
        });
    
        $('.price-change').keypress(function (event) {
            var $this = $(this);
            if ((event.which != 46 || $this.val().indexOf('.') != -1) &&
                ((event.which < 48 || event.which > 57) &&
                    (event.which != 0 && event.which != 8))) {
                event.preventDefault();
            }
            var text = $(this).val();
            if ((event.which == 46) && (text.indexOf('.') == -1)) {
                setTimeout(function () {
                    if ($this.val().substring($this.val().indexOf('.')).length > 3) {
                        $this.val($this.val().substring(0, $this.val().indexOf('.') + 3));
                    }
                }, 1);
            }
            if ((text.indexOf('.') != -1) &&
                (text.substring(text.indexOf('.')).length > 2) &&
                (event.which != 0 && event.which != 8) &&
                ($(this)[0].selectionStart >= text.length - 2)) {
                event.preventDefault();
            }
        });
        $('.price-change').bind("paste", function (e) {
            var text = e.originalEvent.clipboardData.getData('Text');
            if ($.isNumeric(text)) {
                if ((text.substring(text.indexOf('.')).length > 3) && (text.indexOf('.') > -1)) {
                    e.preventDefault();
                    $(this).val(text.substring(0, text.indexOf('.') + 3));
                }
            }
            else {
                e.preventDefault();
            }
        });
        $('.check-input-btn').on('click', function (e) {
            e.preventDefault();
            serializeData = $('#ChangePriceForm').serialize();
            $.ajax({
                url: currentlocation,
                data: serializeData,
                type: 'post',
                success: function (response) {
                    // window.location.reload();
                    location.reload("#myform"); 
                }
            })
        });
        $('.price-change').keypress(function (e) {

            if (e.which == 13) {//Enter key pressed
                $('.check-input-btn').click();//Trigger search button click event
                e.preventDefault();
            }
        });
    });
    // -------------------------------------------------
    // CHANGE TOTAL BEDS MODAL -------------------------
    // -------------------------------------------------
    $('body').on('click', '.open-modal-change-total-beds', function (e) {
        function isEmpty(obj) {
            for (var key in obj) {
                if (obj.hasOwnProperty(key))
                    return false;
            }
            return true;
        }
        var currentlocation = window.location.href;
        var totalBeds = $(".total-beds-text").data('price');
        var password = $(".total-beds-input-password").data('password');

        // SET MODAL START PAGE
        bedPasswordInputPage();

        $('#next-btn2').on('click', function (e) {
            e.preventDefault();
            var passwordForm = $('#TotalBedsPasswordForm');
            console.log("Check password button pressed");
            $.ajax({
                type: passwordForm.attr('method'),
                url: passwordForm.attr('action'),
                data: passwordForm.serialize(),
                success: function (data) {
                    // $("#PricePasswordForm")[0].reset();
                    if ($(data).find(".check-div").html() == 'true') {
                        console.log("it is TRUE and we did it bro");
                        console.log(passwordForm.serialize());
                        bedInputPage();
                    }
                    else {
                        console.log("it is FALSE and we still did it");
                        $('#bed-password-input').addClass('animated shake');
                        $('#bed-password-input').val('');
                        $('#price-password-input').focus();
                    }
                },
                error: function (data) {
                    console.log("its super duper duper wrong");
                    console.log(passwordForm.serialize());
                },
            });
            $('#bed-password-input').removeClass('animated shake');
            return false;
        });
        $('.total-beds-input-password').keypress(function (e) {

            if (e.which == 13) {//Enter key pressed
                $('.check-password-btn').click();//Trigger search button click event
                e.preventDefault();
            }
        });
        $('.check-input-btn').on('click', function (e) {
            e.preventDefault();
            serializeData = $('#ChangeTotalBedsForm').serialize();

            $.ajax({
                url: currentlocation,
                data: serializeData,
                type: 'post',
                success: function (response) {
                    // window.location.reload();
                    location.reload("#myform"); 
                }
            })
        });
        $('.total-beds-change').keypress(function (e) {

            if (e.which == 13) {//Enter key pressed
                $('.check-input-btn').click();//Trigger search button click event
                e.preventDefault();
            }
        });
    });
    // -------------------------------------------------
    // CONFIRM MODAL-- OPEN ----------------------------
    // -------------------------------------------------
    $('body').on('click', '.open-modal-confirm', function (event) {        
        // event.preventDefault();
        var recipient = $(this).data('customer');
        var age = $(this).data('customerage');
        var isconfirmed = $(this).data('isconfirmed');
        var profilepic = $(this).data('img');
        var currentlocation = window.location.href;
        let resID = $(this).data('resid');

        var country = $(this).data('country');
        var countryFlag = $(this).data('countryflag');
        var gender = $(this).data('gender');
        var email = $(this).data('email');
        var phone = $(this).data('phone');
        var contactName = $(this).data('contactname');
        var contactPhone = $(this).data('contactphone');


        $('.customer-info-01').css("display", "block");
        $('.customer-info-02').css("display", "none");

        if (gender == 'M') {
            gender = "Male";
        }
        else if (gender == 'F') {
            gender = "Female";
        }
        else {
            gender = "Unsure";
        }

        $.ajax({
            // url: $("myform").data('url'),
            url: currentlocation,
            beforeSend: function () {
                // Put if statement here for when you murge the confirm and check-in button
                var modal = $('#exampleModal');
                // modal.find('.modal-body input').val(recipient);
                modal.find('.name-field').text(recipient);
                modal.find('.age-field').html(age + " Yrs");
                modal.find('.profile-image').attr('src', profilepic);
                modal.find('.input-confirm').val(isconfirmed);
                modal.find('.is-confirmed2').val(isconfirmed);
                modal.find('.id-field').text(resID);
                modal.find('.reservationid').val(resID);
                modal.find('.country-field').html(country);
                modal.find('.country-flag-field').attr('src', countryFlag);
                modal.find('.gender-field').html(gender);
                modal.find('.phone-field').html(phone);
                modal.find('.email-field').html(email);
                modal.find('.emergency-contact-name-field').html(contactName + ":");
                modal.find('.emergency-contact-phone-field').html(contactPhone);
                serializeData = $('#confirmForm').serialize();

                $('.customer-info-01').css("display", "block");
                $('.customer-info-02').css("display", "none");
            }
        })  
        $(document).on("click", '.confirm-res', function (e) {
            e.preventDefault();   
            var confirmField = $('.is-confirmed-field').val();
            var conValue = $('.is-confirmed-field').data('value');
            // var cv = parseInt($('.is-confirmed2').attr('value'));
            // var cv = $('.is-confirmed2').val();
            // console.log(cv);

            if (isconfirmed == "False") {
                $('#confirmForm').find('.is-confirmed2').val("True");
            }
            else {
                console.log("its true brah");
            }
            serializeData = $('#confirmForm').serialize();
            $.ajax({
                url: currentlocation,
                data: serializeData,
                type: 'post',
                success: function (response) {
                    // $("#confirmForm").load(location.href + " #confirmForm>*", "");
                    window.location.reload();
                    // $('#myModal .modal-dialog').html($('#myModal .modal-dialog', data));
                    // $('#myModal').modal('show');
                }
            })
        });
        $('.more-btn').on('click', function (event) {
            $('.customer-info-01').css("display", "none");
            $('.customer-info-02').css("display", "block");

        });
        $('.back-btn').on('click', function (e) {

            $('.customer-info-01').css("display", "block");
            $('.customer-info-02').css("display", "none");
        });
    });
    // -------------------------------------------------
    // CHECKIN MODAL-- OPEN ----------------------------
    // -------------------------------------------------
    $('body').on('click', '.open-modal-checkin', function (event) {
        // event.preventDefault();
        var recipient = $(this).data('customer');
        var age = $(this).data('customerage');
        var isconfirmed = $(this).data('isconfirmed');
        var ischeckedin = $(this).data('ischeckedin');
        var profilepic = $(this).data('img');
        var currentlocation = window.location.href;
        let resID = $(this).data('resid');

        var country = $(this).data('country');
        var countryFlag = $(this).data('countryflag');
        var gender = $(this).data('gender');
        var email = $(this).data('email');
        var phone = $(this).data('phone');
        var contactName = $(this).data('contactname');
        var contactPhone = $(this).data('contactphone');

        console.log(resID);
        console.log("isconfirmed is: " + isconfirmed);
        console.log("ischeckedin is: " + ischeckedin);

        $('.customer-info-01').css("display", "block");
        $('.customer-info-02').css("display", "none");

        if (gender == 'M') {
            gender = "Male";
        }
        else if (gender == 'F') {
            gender = "Female";
        }
        else {
            gender = "Unsure";
        }

        $.ajax({
            // url: $("myform").data('url'),
            url: currentlocation,
            beforeSend: function () {
                // Put if statement here for when you murge the confirm and check-in button
                var modal = $('#exampleModal2');
                // modal.find('.modal-body input').val(recipient);
                modal.find('.name-field').text(recipient);
                modal.find('.age-field').html(age);
                modal.find('.profile-image').attr('src', profilepic);
                modal.find('.is-confirmed-field').text(isconfirmed);
                modal.find('.is-checkedin-field').text(ischeckedin);

                modal.find('.is-checkedin2').val(ischeckedin);


                modal.find('.id-field').text(resID);
                modal.find('.reservationid').val(resID);

                modal.find('.country-field').html(country);
                modal.find('.country-flag-field').attr('src', countryFlag);
                modal.find('.gender-field').html(gender);
                modal.find('.phone-field').html(phone);
                modal.find('.email-field').html(email);
                modal.find('.emergency-contact-name-field').html(contactName + ":");
                modal.find('.emergency-contact-phone-field').html(contactPhone);
                serializeData = $('#checkinForm').serialize();

                $('.customer-info-01').css("display", "block");
                $('.customer-info-02').css("display", "none");
                console.log(serializeData);
            }
        })
        $(document).on("click", '.checkin-res', function (e) {

            console.log(resID);

            if (ischeckedin == "False") {
                $('#checkinForm').find('.is-checkedin2').val("True");
            }
            else {
                console.log("its true brah");
            }
            serializeData = $('#checkinForm').serialize();
            console.log(serializeData);
            $.ajax({
                url: currentlocation,
                data: serializeData,
                type: 'post',
                success: function (response) {
                    // $("#confirmForm").load(location.href + " #confirmForm>*", "");
                    window.location.reload();
                    // $('#myModal .modal-dialog').html($('#myModal .modal-dialog', data));
                    // $('#myModal').modal('show');
                }
            })
        });
        $('.more-btn').on('click', function (event) {
            $('.customer-info-01').css("display", "none");
            $('.customer-info-02').css("display", "block");

        });
        $('.back-btn').on('click', function (e) {

            $('.customer-info-01').css("display", "block");
            $('.customer-info-02').css("display", "none");
        });
    });
    // -------------------------------------------------
    // CUSTOMER INFO MODAL PAGE SETUP ------------------
    // -------------------------------------------------
    $('body').on('click', '.before-btn', function (e) {
        if ($('.step-01').css('display') == 'block') {
            $('.step-01').css("display", "none");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "block");
        }
        else if ($('.step-02').css('display') == 'block') {
            $('.step-01').css("display", "block");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "none");
        }
        else if ($('.step-03').css('display') == 'block') {
            $('.step-01').css("display", "none");
            $('.step-02').css("display", "block");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "none");
        }
        else if ($('.step-04').css('display') == 'block') {
            $('.step-01').css("display", "none");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "block");
            $('.step-04').css("display", "none");
        }
        else {
            $('.step-01').css("display", "block");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "none");
        }

    });
    $('body').on('click', '.after-btn', function (e) {
        if ($('.step-01').css('display') == 'block') {
            $('.step-01').css("display", "none");
            $('.step-02').css("display", "block");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "none");
        }
        else if ($('.step-02').css('display') == 'block') {
            $('.step-01').css("display", "none");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "block");
            $('.step-04').css("display", "none");
        }
        else if ($('.step-03').css('display') == 'block') {
            $('.step-01').css("display", "none");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "block");
        }
        else if ($('.step-04').css('display') == 'block') {
            $('.step-01').css("display", "block");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "none");
        }
        else {
            $('.step-01').css("display", "block");
            $('.step-02').css("display", "none");
            $('.step-03').css("display", "none");
            $('.step-04').css("display", "none");
        }
    });
});


    // -------------------------------------------------
    // PLUS BUTTON -------------------------------------
    // -------------------------------------------------
    // This button will increment the value
    // $(document).on("click", '.qtyplus', function (e) {
    //     // Stop acting like a button
    //     e.preventDefault();
    //     // Get the field name
    //     fieldName = $(this).attr('field');
    //     var divUrl = $(this).attr('action');
    //     // Get its current value
    //     var currentVal = parseInt($('input[name=' + fieldName + ']').val());
    //     var occupiedBeds = parseInt($("div#" + fieldName).text());
    //     var totalBeds = parseInt($("div#total-beds").text());


    //     console.log(fieldName);
    //     // If is not undefined
    //     if (!isNaN(currentVal)) {
    //         // Increment
    //         if (currentVal < totalBeds) {
    //             $('input[name=' + fieldName + ']').val(currentVal + 1);
    //             // if loop here
    //             ++currentVal;
    //         }
    //         else {
    //             $('input[name=' + fieldName + ']').val(currentVal);
    //         }
    //     } else {
    //         // Otherwise put a 0 there
    //         $('input[name=' + fieldName + ']').val(0);
    //     }
    //     serializeData = $('#myform').serialize();
    //     console.log(serializeData);
    //     $.ajax({
    //         url: divUrl,
    //         data: serializeData,
    //         type: 'post',
    //         success: function (response) {
    //             location.reload("#myform");       
    //             // $("#myform").load(location.href + " #myform>*", "");
    //             // $("#roomdetail-form").load(window.location.href + " #roomdetail-form");

    //             // if (serializeData.success == false) {
    //             //     alert('error');
    //             // } else {
    //             //     // $("#roomdetail-form").load(" #roomdetail-form");
    //             //     $("#roomdetail-form").load(location.href + " #roomdetail-form>*", "");
    //             // }
    //         }
    //     })
    // });
    // -------------------------------------------------
    // MINUS BUTTON ------------------------------------
    // -------------------------------------------------
    // This button will decrement the value till 0
    // $(document).on("click", '.qtyminus', function (e) {
    // // $(".qtyminus").click(function (e) {
    //     // Stop acting like a button
    //     e.preventDefault();
    //     // Get the field name
    //     fieldName = $(this).attr('field');
    //     var divUrl = $(this).attr('action');
    //     // Get its current value
    //     var currentVal = parseInt($('input[name=' + fieldName + ']').val());
    //     // If it isn't undefined or its greater than 0
    //     if (!isNaN(currentVal) && currentVal > 0) {
    //         // Decrement one
    //         $('input[name=' + fieldName + ']').val(currentVal - 1);
    //         --currentVal;
    //     } else {
    //         // Otherwise put a 0 there
    //         $('input[name=' + fieldName + ']').val(0);
    //     }
    //     serializeData = $('#myform').serialize();
    //     $.ajax({
    //         url: divUrl,
    //         data: serializeData,
    //         type: 'post',
    //         success: function (response) {
    //             // $("#myform").load(location.href + " #myform>*", "");
    //             location.reload("#myform");       

    //         }
    //     })
    // });
    // -------------------------------------------------
    // TUTORIAL MODAL ----------------------------------
    // -------------------------------------------------
    // $('.tutorial-modal-btn').on('click', function (e) {
    //     e.preventDefault();
    //     $('.step-01').css("display", "block");
    //     $('.step-02').css("display", "none");
    //     $('.step-03').css("display", "none");
    //     $('.step-04').css("display", "none");
    // });

    // Autofocus Section
    // $('#exampleModal3').on('shown.bs.modal', function () {
    //     if ($('#PricePasswordForm').css('display') == 'block') {
    //         console.log("ITS one");
    //         $('#price-password-input').focus();
    //     }
    //     if ($('.create-price-password-form').css('display') == 'block') {
    //         console.log("ITS two");
    //         $('#create-price-password').focus();
    //     }
    //     if ($('#ChangePricePasswordForm').css('display') == 'block') {
    //         console.log("ITS three");
    //         $('#input-password-old').focus();
    //     }
    // })

    // -------------------------------------------------
// PRICE AND TOTAL BED PASSWORD -  reload page when modal is closed so form gets saved
// -------------------------------------------------
// $("#exampleModal4").on('hidden.bs.modal', function () {
//     // window.alert('hidden event fired!');
//     if ($('#ChangeTotalBedsForm').css('display') == 'none') {
//         // DONT DO ANYTHING
//     }
//     else {
//         // window.location.reload();
//         location.reload("#myform"); 
//     }
// });
// $("#exampleModal3").on('hidden.bs.modal', function () {
//     if ($('#ChangePriceForm').css('display') == 'none') {
//         // DONT DO ANYTHING
//     }
//     else {
//         // window.location.reload();
//         location.reload("#myform"); 
//     }
//     // window.alert('hidden event fired!');
// });