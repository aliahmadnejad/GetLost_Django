// PAGE OPTION SETUP PAGE
function publicInfoPage() {
    publicInfoReset();
    $('#public-info').css("display", "block");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "none");
}
function privateInfoPage() {
    privateInfoReset();
    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "block");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "none");
}
function passwordPage() {
    passwordReset();
    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "block");
    $('#language-and-currency').css("display", "none");
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
    $("#city-state").prop("disabled", true);
    $("#country").prop("disabled", true);
}
function publicInfoShow() {
    $('#public-cancel-btn').css("display", "block");
    $('#public-update-btn').css("display", "block");
    $('#public-info-modal').css("display", "none");
    $("#hostle-name").prop("disabled", false);
    $(".email").prop("disabled", false);
    $(".phone").prop("disabled", false);
    $(".address").prop("disabled", false);
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
}
function privateInfoShow() {
    $('#private-cancel-btn').css("display", "block");
    $('#private-update-btn').css("display", "block");
    $('#private-info-modal').css("display", "none");
    $("#hostle-name2").prop("disabled", false);
    $("#email2").prop("disabled", false);
    $("#phone2").prop("disabled", false);
    $("#address2").prop("disabled", false);
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
}
function passwordShow() {
    $('#pin-password-cancel-btn').css("display", "block");
    $('#pin-password-update-btn').css("display", "block");
    $('#pin-and-password-modal').css("display", "none");
    $("#master-password").prop("disabled", false);
    $("#employee-password").prop("disabled", false);
}
// LANGUAGE AND CURRENCY PAGE SETUP

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
    languageCurrencyPage();
});

jQuery(document).ready(function () {

    // Open Public Info Modal
    $('#public-info-modal').on('click', function (e) {
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
                    // console.log($(data).find("#practice-div").html());
                    // console.log($(data).find(".testing-div").html());
                    // console.log(this.data);
                    // console.log(publicInfoForm.html());
                    if ($(data).find(".testing-div").html() == 'true') {
                        console.log("it is TRUE and we did it bro");
                        publicInfoShow();
                        $('#public-modal').modal('hide');
                        console.log(publicInfoForm.serialize());
                    }
                    else {
                        console.log("it is FALSE and we still did it");
                    }
                },
                error: function (data) {
                    console.log("its super duper duper wrong");
                    console.log(publicInfoForm.serialize());
                },
            });
            return false;
        });    
    });
    $("#public-cancel-btn").on('click', function (e) {
        e.preventDefault();
        console.log("HEY");
        $('#public-cancel-btn').css("display", "none");
        $('#public-update-btn').css("display", "none");
        $('#public-info-modal').css("display", "block");
        $("#hostle-name").prop("disabled", true);
        $(".email").prop("disabled", true);
        $(".phone").prop("disabled", true);
        $(".address").prop("disabled", true);
        $("#city-state").prop("disabled", true);
        $("#country").prop("disabled", true);
    });
    $('#public-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $("#PublicInfoForm")[0].reset();
    });

    $('#public-update-btn').on('click', function (e) {
        // e.preventDefault();

        $("#public-info-form .public-info-form-input").filter(function (index, element) {
            if (jQuery.trim($(element).val()).length == 0) {
                $(element).val($(element).attr("placeholder"));
            }
        })
        $('#public-info-form').submit(function (event) {

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
});

// create functions for all resets and show pages
// new way: maybe make all submittions the same as the password submittion
// -- send form information without reloading page with success (data)
// Try using the disable method instead of the one using for all forms except password form
// -- disable empty form inputs instead of checking to see if it is empty before taking in the old value with {{}} in html and sending it to jquery to replace
// Try new way of seeing which form to save by getting the name of each input from the request
// also maybe try using class based views
// ERRORS for a wrong input just doesnt do anything. Find a way to present an error everytime an input is wrong -- e.g. if phone input is wrong then nothing will be changed in the submit