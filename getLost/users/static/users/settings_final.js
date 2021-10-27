
// PAGE OPTION SETUP PAGE
function publicInfoPage() {
    publicInfoReset();
    $('#public-info').css("display", "block");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "none");
    
    $('.public-info-message').css("display", "block");
    $('.private-info-message').css("display", "none");
    $('.password-message').css("display", "none");
    $('.lang-currency-message').css("display", "none");

    $('.public-info-container').css("background-color", "#90909044");
}
function privateInfoPage() {
    privateInfoReset();
    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "block");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "none");

    $('.public-info-message').css("display", "none");
    $('.private-info-message').css("display", "block");
    $('.password-message').css("display", "none");
    $('.lang-currency-message').css("display", "none");

    $('.private-contact-container').css("background-color", "#90909044");
}
function passwordPage() {
    passwordReset();
    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "block");
    $('#language-and-currency').css("display", "none");

    $('.public-info-message').css("display", "none");
    $('.private-info-message').css("display", "none");
    $('.password-message').css("display", "block");
    $('.lang-currency-message').css("display", "none");

    $('.id-pin-container').css("background-color", "#90909044");
}
function langCurrencyPage() {
    langCurrencyReset();
    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "block");

    $('.public-info-message').css("display", "none");
    $('.private-info-message').css("display", "none");
    $('.password-message').css("display", "none");
    $('.lang-currency-message').css("display", "block");
    
    $('.lang-currency-container').css("background-color", "#90909044");
}
function languageCurrencyPage() {
    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "block");
}
// PUBLIC INFO PAGE SETUP
function publicInfoReset() {
    $('#public-cancel-btn').css("display", "none");
    $('#public-update-btn').css("display", "none");
    $('#public-info-modal').css("display", "block");
    $("#hostle-name").prop("disabled", true);
    $(".email").prop("disabled", true);
    $(".phone").prop("disabled", true);
    $(".address").prop("disabled", true);
    $("#zip-code").prop("disabled", true);
    $("#city-state").prop("disabled", true);
    $("#country").prop("disabled", true);

    $('.private-contact-container').css("background-color", "#ffffff");
    $('.id-pin-container').css("background-color", "#ffffff");
    $('.lang-currency-container').css("background-color", "#ffffff");
}
function publicInfoShow() {
    $('#public-cancel-btn').css("display", "block");
    $('#public-update-btn').css("display", "block");
    $('#public-info-modal').css("display", "none");
    $("#hostle-name").prop("disabled", false);
    $(".email").prop("disabled", false);
    $(".phone").prop("disabled", false);
    $(".address").prop("disabled", false);
    $("#zip-code").prop("disabled", false);
    $("#city-state").prop("disabled", false);
    $("#country").prop("disabled", false);
}
// PRIVATE INFO PAGE SETUP
function privateInfoReset() {
    $('#private-cancel-btn').css("display", "none");
    $('#private-update-btn').css("display", "none");
    $('#private-info-modal').css("display", "block");
    $("#hostle-name2").prop("disabled", true);
    $("#email2").prop("disabled", true);
    $("#phone2").prop("disabled", true);
    $("#address2").prop("disabled", true);
    $("#zip-code2").prop("disabled", true);
    $("#city-state2").prop("disabled", true);
    $("#country2").prop("disabled", true);
    $("#fax").prop("disabled", true);
    $("#website").prop("disabled", true);
    $("#owner-name").prop("disabled", true);
    $("#owner-phone").prop("disabled", true);
    $("#first-manager-name").prop("disabled", true);
    $("#first-manager-phone").prop("disabled", true);
    $("#first-manager-email").prop("disabled", true);
    $("#second-manager-name").prop("disabled", true);
    $("#second-manager-phone").prop("disabled", true);
    $("#second-manager-email").prop("disabled", true);

    $('.public-info-container').css("background-color", "#ffffff");
    $('.id-pin-container').css("background-color", "#ffffff");
    $('.lang-currency-container').css("background-color", "#ffffff");
}
function privateInfoShow() {
    $('#private-cancel-btn').css("display", "block");
    $('#private-update-btn').css("display", "block");
    $('#private-info-modal').css("display", "none");
    $("#hostle-name2").prop("disabled", false);
    $("#email2").prop("disabled", false);
    $("#phone2").prop("disabled", false);
    $("#address2").prop("disabled", false);
    $("#zip-code2").prop("disabled", false);
    $("#city-state2").prop("disabled", false);
    $("#country2").prop("disabled", false);
    $("#fax").prop("disabled", false);
    $("#website").prop("disabled", false);
    $("#owner-name").prop("disabled", false);
    $("#owner-phone").prop("disabled", false);
    $("#first-manager-name").prop("disabled", false);
    $("#first-manager-phone").prop("disabled", false);
    $("#first-manager-email").prop("disabled", false);
    $("#second-manager-name").prop("disabled", false);
    $("#second-manager-phone").prop("disabled", false);
    $("#second-manager-email").prop("disabled", false);
}
// PASSWORD PAGE SETUP
function passwordReset() {
    $('#pin-password-cancel-btn').css("display", "none");
    $('#pin-password-update-btn').css("display", "none");
    $('#pin-and-password-modal').css("display", "block");
    $("#master-password").prop("disabled", true);
    $("#employee-password").prop("disabled", true);

    $('.public-info-container').css("background-color", "#ffffff");
    $('.private-contact-container').css("background-color", "#ffffff");
    $('.lang-currency-container').css("background-color", "#ffffff");
}
function passwordShow() {
    $('#pin-password-cancel-btn').css("display", "block");
    $('#pin-password-update-btn').css("display", "block");
    $('#pin-and-password-modal').css("display", "none");
    $("#master-password").prop("disabled", false);
    $("#employee-password").prop("disabled", false);
}
// LANGUAGE AND CURRENCY PAGE SETUP
function langCurrencyReset() {
    $('#lang-currency-cancel-btn').css("display", "none");
    $('#lang-currency-update-btn').css("display", "none");
    $('#lang-and-currency-modal').css("display", "block");
    $("#language-input").prop("disabled", true);
    $("#currency-input").prop("disabled", true);
    $("#vat-input").prop("disabled", true);

    $('.public-info-container').css("background-color", "#ffffff");
    $('.private-contact-container').css("background-color", "#ffffff");
    $('.id-pin-container').css("background-color", "#ffffff");
}
function langCurrencyShow() {
    $('#lang-currency-cancel-btn').css("display", "block");
    $('#lang-currency-update-btn').css("display", "block");
    $('#lang-and-currency-modal').css("display", "none");
    $("#language-input").prop("disabled", false);
    $("#currency-input").prop("disabled", false);
    $("#vat-input").prop("disabled", false);
}

publicInfoPage();
// PAGE SELECTION
// --------------
// 1. PUBLIC INFO
$('.public-info-btn').on('click', function (e) {
    publicInfoPage();
});
// 2. PRIVATE INFO
$('.private-contact-info-btn').on('click', function (e) {
    privateInfoPage();
});
// 3. PASSWORD
$('.id-and-pin-btn').on('click', function (e) {
    passwordPage();
});
// 4. LANGUAGE AND CURRENCY 
$('.language-currency-btn').on('click', function (e) {
    langCurrencyPage();
});






jQuery(document).ready(function () {

    // var input = document.querySelector("#phone");
    // console.log(input);
    // intlTelInput(input, {
    //     // any initialisation options go here
        
    //     utilsScript: "intl-tel-input-master/build/js/utils.js",
    //     // customPlaceholder: function (selectedCountryPlaceholder, selectedCountryData) {
    //     //     return "e.g. " + selectedCountryPlaceholder;
    //     // },
    //     autoPlaceholder: "1234",
        
    // });
    // var iti = intlTelInput(input)
    // var number = iti.getNumber();
    // var extension = iti.getExtension();
    // console.log(number);
    // console.log(extension);

    var input = document.querySelector("#phone");
    var iti = window.intlTelInput(input, {
        // autoPlaceholder: "+14079687740",
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.14/js/utils.js",
        // utilsScript: "{% static 'intl-tel-input-master/src/js/utils.js' %}",
        // utilsScript: "intl-tel-input-master/build/js/utils.js",
    });
    
    $('#public-modal').on('shown.bs.modal', function () {
        $('#password-input').focus();
        // $(this).find('[autofocus]').focus();
        $("#password-input").keypress(function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                $("#next-btn").click();
            }
        });
    })
    
    // Open Public Info Modal
    $('#public-info-modal').on('click', function (e) {
        // $("#password-input").trigger('focus');
        e.preventDefault();
        
        // $('#public-modal').modal('show');
        // Check Password Input 
        $('#next-btn').on('click', function (e) {
            e.preventDefault();
            var publicInfoForm = $('#PublicInfoForm');
            $.ajax({
                type: publicInfoForm.attr('method'),
                url: publicInfoForm.attr('action'),
                data: publicInfoForm.serialize(),
                success: function (data) {
                    console.log("it got here");
                    console.log($(data).find("#password-div").html());
                    console.log($(data).find(".check-div").html());
                    console.log(this.data);
                    console.log(publicInfoForm.html());
                    if ($(data).find(".check-div").html() == 'true') {
                        console.log("it is TRUE and we did it bro");
                        publicInfoShow();
                        $('#public-modal').modal('hide');
                        console.log(publicInfoForm.serialize());
                    }
                    else {
                        console.log("it is FALSE and we still did it");
                        $('#password-input').addClass('animated shake');
                        $('#password-input').val('');
                        $('#password-input').focus();
                        
                    }
                },
                error: function (data) {
                    console.log("its super duper duper wrong");
                    console.log(publicInfoForm.serialize());
                },
            });
            $('#password-input').removeClass('animated shake');
            return false;
        });
    });    
    // When Public Info Modal Closes
    $('#public-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $("#PublicInfoForm")[0].reset();
    });
    // Cancel Editting after Password Check
    $("#public-cancel-btn").on('click', function (e) {
        e.preventDefault();
        publicInfoReset();
    });
    // Update Public Info Settings Button Pressed
    $('#public-update-btn').on('click', function (e) {
        // e.preventDefault();
        
        // var iti = intlTelInput(input);
        var number = iti.getNumber();
        // var extension = $("#phone").iti("getSelectedCountryData").dialCode;
        console.log(number);
        console.log($("#phone").val());

        $("#public-info-form .public-info-form-input").filter(function (index, element) {
            if (jQuery.trim($(element).val()).length == 0) {
                
                if ($(element).attr('id') == 'phone') {
                    console.log("it is empty");
                    console.log(element);
                    $("#phone").val($(element).data("placeholder"));
                    console.log($("#phone").val());
                    // $("#phone").prop("disabled", true);
                    // iti.destroy();
                }
                else{
                    $(element).val($(element).attr("placeholder"));
                }
                
                
            }
            else {
                if ($(element).attr('id') == 'phone') {
                    console.log("it is not empty");
                    console.log($("#phone").val());
                    $("#phone").val(number);
                }

            }
        })
        $('#public-info-form').submit(function (event) {

            console.log($("#phone").val());
            var frm = $('#public-info-form');
            frm.submit(function () {
                $.ajax({
                    type: frm.attr('method'),
                    url: frm.attr('action'),
                    data: frm.serialize(),
                    success: function (data) {
                        $("#public-info").html(data);
                    },
                });
                return false;
            });
        });
    });
    $('#private-modal').on('shown.bs.modal', function () {
        $('#password-input2').focus();
        // $(this).find('[autofocus]').focus();
        $("#password-input2").keypress(function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                $("#next-btn2").click();
            }
        });
    })
    // Open Private Info Modal
    $('#private-info-modal').on('click', function (e) {
        e.preventDefault();

        $('#next-btn2').on('click', function (e) {
            e.preventDefault();
            var privateInfoForm = $('#PrivateInfoForm');
            $.ajax({
                type: privateInfoForm.attr('method'),
                url: privateInfoForm.attr('action'),
                data: privateInfoForm.serialize(),
                success: function (data) {
                    console.log("it got here");
                    if ($(data).find(".check-div2").html() == 'true') {
                        console.log("it is TRUE and we did it bro");
                        privateInfoShow();
                        $('#private-modal').modal('hide');
                        console.log(privateInfoForm.serialize());
                    }
                    else {
                        console.log("it is FALSE and we still did it");
                        $('#password-input2').addClass('animated shake');
                        $('#password-input2').val('');
                        $('#password-input2').focus();
                    }
                },
                error: function (data) {
                    console.log("its super duper duper wrong");
                    console.log(privateInfoForm.serialize());
                },
            });
            $('#password-input2').removeClass('animated shake');
            return false;
        });
    });
    
    // When Private Info Modal Closes
    $('#private-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $("#PrivateInfoForm")[0].reset();
    });
    // Cancel Editting after Password Check
    $("#private-cancel-btn").on('click', function (e) {
        e.preventDefault();
        privateInfoReset();
    });
    // Update Private Info Settings Button Pressed
    $('#private-update-btn').on('click', function (e) {
        // e.preventDefault();

        $("#private-info-form .private-info-form-input").filter(function (index, element) {
            if (jQuery.trim($(element).val()).length == 0) {
                $(element).val($(element).attr("placeholder"));
            }
        })
        $('#private-info-form').submit(function (event) {

            var frm = $('#private-info-form');
            frm.submit(function () {
                $.ajax({
                    type: frm.attr('method'),
                    url: frm.attr('action'),
                    data: frm.serialize(),
                    success: function (data) {
                        $("#private-contact-info").html(data);
                    },
                });
                return false;
            });
        });
    });
    $('#pin-password-modal').on('shown.bs.modal', function () {
        $('#password-input3').focus();
        // $(this).find('[autofocus]').focus();
        $("#password-input3").keypress(function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                $("#next-btn3").click();
            }
        });
    })
    // Open Pin and Password Info Modal
    $('#pin-and-password-modal').on('click', function (e) {
        e.preventDefault();

        $('#next-btn3').on('click', function (e) {
            e.preventDefault();
            var pinPasswordForm = $('#PinPasswordForm');
            $.ajax({
                type: pinPasswordForm.attr('method'),
                url: pinPasswordForm.attr('action'),
                data: pinPasswordForm.serialize(),
                success: function (data) {
                    console.log("it got here");
                    if ($(data).find(".check-div3").html() == 'true') {
                        console.log("it is TRUE and we did it bro");
                        passwordShow();
                        $('#pin-password-modal').modal('hide');
                        console.log(pinPasswordForm.serialize());
                    }
                    else {
                        console.log("it is FALSE and we still did it");
                        $('#password-input3').addClass('animated shake');
                        $('#password-input3').val('');
                        $('#password-input3').focus();
                    }
                },
                error: function (data) {
                    console.log("its super duper duper wrong");
                    console.log(pinPasswordForm.serialize());
                },
            });
            $('#password-input3').removeClass('animated shake');
            return false;
        });
    });
    // When Pin and Password Info Modal Closes
    $('#pin-password-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $("#PinPasswordForm")[0].reset();
    });
    // Cancel Editting after Password Check
    $("#pin-password-cancel-btn").on('click', function (e) {
        e.preventDefault();
        passwordReset();
    });
    // Update Pin and Password Info Settings Button Pressed
    $('#pin-password-update-btn').on('click', function (e) {
        // e.preventDefault();
        $("#password-form .password-form-input").filter(function (index, element) {
            if (jQuery.trim($(element).val()).length == 0) {
                $(element).prop("disabled", true);
                // $(element).val($(element).attr("placeholder"));
            }
        })
        $('#password-form').submit(function (event) {

            if (($('#master-password').is('[disabled=""]')) && ($('#employee-password').is('[disabled=""]'))) {
                console.log("They are both Empty");
                e.preventDefault();
                location.reload(true);
                //pass
            }
            else {
                var frm = $('#password-form');
                frm.submit(function () {
                    $.ajax({
                        type: frm.attr('method'),
                        url: frm.attr('action'),
                        data: frm.serialize(),
                        success: function (data) {
                            $("#pin-and-password").html(data);
                        },
                    });
                    return false;
                });

            }
            
        });
    });

    $('#language-currency-modal').on('shown.bs.modal', function () {
        $('#password-input4').focus();
        // $(this).find('[autofocus]').focus();
        $("#password-input4").keypress(function (event) {
            if (event.keyCode === 13) {
                event.preventDefault();
                $("#next-btn4").click();
            }
        });
    })

    // Open Language and Currency Info Modal
    $('#lang-and-currency-modal').on('click', function (e) {
        e.preventDefault();

        $('#next-btn4').on('click', function (e) {
            e.preventDefault();
            var currencyForm = $('#LangCurrencyForm');
            $.ajax({
                type: currencyForm.attr('method'),
                url: currencyForm.attr('action'),
                data: currencyForm.serialize(),
                success: function (data) {
                    console.log("it got here");
                    if ($(data).find(".check-div4").html() == 'true') {
                        console.log("it is TRUE and we did it bro");
                        langCurrencyShow();
                        $('#language-currency-modal').modal('hide');
                        console.log(currencyForm.serialize());
                    }
                    else {
                        console.log("it is FALSE and we still did it");
                        $('#password-input4').addClass('animated shake');
                        $('#password-input4').val('');
                        $('#password-input4').focus();
                    }
                },
                error: function (data) {
                    console.log("its super duper duper wrong");
                    console.log(currencyForm.serialize());
                },
            });
            $('#password-input4').removeClass('animated shake');
            return false;
        });
    });
    // When Language and Currency Info Modal Closes
    $('#language-currency-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $("#LangCurrencyForm")[0].reset();
    });
    // Cancel Editting after Password Check
    $("#lang-currency-cancel-btn").on('click', function (e) {
        e.preventDefault();
        langCurrencyReset();
    });


    // Update Language and Currency Info Settings Button Pressed
    $('#lang-currency-update-btn').on('click', function (e) {
        // e.preventDefault();
        console.log("we here");
        $("#language-currency-form .lang-currency-form-input").filter(function (index, element) {
            if (jQuery.trim($(element).val()).length == 0) {
                console.log("it is empty at least yo");
                $(element).val($(element).data("vat")); // because of the percentage sign in the placeholder attr
            }
        })
        $('#language-currency-form').submit(function (event) {   
            var frm = $('#language-currency-form');
            frm.submit(function () {
                $.ajax({
                    type: frm.attr('method'),
                    url: frm.attr('action'),
                    data: frm.serialize(),
                    success: function (data) {
                        $("#language-and-currency").html(data);
                    },
                });
                return false;
            });
        });
    });
});

// create functions for all resets and show pages
// new way: maybe make all submittions the same as the password submittion
// -- send form information without reloading page with success (data)
// Try using the disable method instead of the one using for all forms except password form
// -- disable empty form inputs instead of checking to see if it is empty before taking in the old value with {{}} in html and sending it to jquery to replace
// Try new way of seeing which form to save by getting the name of each input from the request
// also maybe try using class based views
// ERRORS for a wrong input just doesnt do anything. Find a way to present an error everytime an input is wrong -- e.g. if phone input is wrong then nothing will be changed in the submit