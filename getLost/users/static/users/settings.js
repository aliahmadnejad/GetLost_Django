// PUBLIC INFO SETUP
$('#public-info').css("display", "block");
$('#private-contact-info').css("display", "none");
$('#pin-and-password').css("display", "none");
$('#language-and-currency').css("display", "none");

$('#public-cancel-btn').css("display", "none");
$('#public-update-btn').css("display", "none");
$("#hostle-name").prop("disabled", true);
$(".email").prop("disabled", true);
$(".phone").prop("disabled", true);
$(".address").prop("disabled", true);
$("#city-state").prop("disabled", true);
$("#country").prop("disabled", true);

// PRIVATE INFO SETUP
$('#private-cancel-btn').css("display", "none");
$('#private-update-btn').css("display", "none");
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

// PIN AND PASSWORD SETUP
$('#pin-password-cancel-btn').css("display", "none");
$('#pin-password-update-btn').css("display", "none");
$("#master-password").prop("disabled", true);
$("#employee-password").prop("disabled", true);
// LANGUAGE AND CURRENCY SETUP


$('.public-info-btn').on('click', function (e) {

    $('#public-info').css("display", "block");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "none");

    if ($('#private-contact-info').css('display') == 'none') {
        console.log("Refresh private info");
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
    if ($('#pin-and-password').css('display') == 'none') {
        console.log("Refresh pin and password");
        $('#pin-password-cancel-btn').css("display", "none");
        $('#pin-password-update-btn').css("display", "none");
        $('#pin-and-password-modal').css("display", "block");
        $("#master-password").prop("disabled", true);
        $("#employee-password").prop("disabled", true);
    }  
    if ($('#language-and-currency').css('display') == 'none') {
        console.log("Refresh language and currency");
    }  
});
$('.private-contact-info-btn').on('click', function (e) {

    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "block");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "none");

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

    if ($('#public-info').css('display') == 'none') {
        console.log("Refresh public info");
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
    if ($('#pin-and-password').css('display') == 'none') {
        console.log("Refresh pin and password");
        $('#pin-password-cancel-btn').css("display", "none");
        $('#pin-password-update-btn').css("display", "none");
        $('#pin-and-password-modal').css("display", "block");
        $("#master-password").prop("disabled", true);
        $("#employee-password").prop("disabled", true);
    }
    if ($('#language-and-currency').css('display') == 'none') {
        console.log("Refresh language and currency");
    } 
});
$('.id-and-pin-btn').on('click', function (e) {

    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "block");
    $('#language-and-currency').css("display", "none");

    if ($('#public-info').css('display') == 'none') {
        console.log("Refresh public info");
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
    if ($('#private-contact-info').css('display') == 'none') {
        console.log("Refresh private info");
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
    if ($('#language-and-currency').css('display') == 'none') {
        console.log("Refresh language and currency");
    } 
});
$('.language-currency-btn').on('click', function (e) {

    $('#public-info').css("display", "none");
    $('#private-contact-info').css("display", "none");
    $('#pin-and-password').css("display", "none");
    $('#language-and-currency').css("display", "block");

    if ($('#public-info').css('display') == 'none') {
        console.log("Refresh public info");
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
    if ($('#private-contact-info').css('display') == 'none') {
        console.log("Refresh private info");
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
    if ($('#pin-and-password').css('display') == 'none') {
        console.log("Refresh pin and password");
        $('#pin-password-cancel-btn').css("display", "none");
        $('#pin-password-update-btn').css("display", "none");
        $('#pin-and-password-modal').css("display", "block");
        $("#master-password").prop("disabled", true);
        $("#employee-password").prop("disabled", true);
    } 
});

jQuery(document).ready(function () {

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

    $('#public-info-modal').on('click', function (e) {
        e.preventDefault();
        var password = $("#password-input").data('password');

        $('#next-btn1').on('click', function (e) {
            var inputPassword = $("#password-input").val();
            console.log(inputPassword);
            console.log(password);







            if (password == inputPassword) {
                console.log("PASSWORD IS CORRECT");
                $('#public-cancel-btn').css("display", "block");
                $('#public-update-btn').css("display", "block");
                $('#public-info-modal').css("display", "none");
                $("#hostle-name").prop("disabled", false);
                $(".email").prop("disabled", false);
                $(".phone").prop("disabled", false);
                $(".address").prop("disabled", false);
                $("#city-state").prop("disabled", false);
                $("#country").prop("disabled", false);
                $('#public-modal').modal('hide');


                

                console.log("IT AT LEAST GOES HERE");
                // var publicInfoForm = $('#PublicInfoForm');
                // publicInfoForm.submit(function () {
                //     $.ajax({
                //         type: publicInfoForm.attr('method'),
                //         url: publicInfoForm.attr('action'),
                //         data: publicInfoForm.serialize(),
                //         // data: formData.serialize(),
                //         success: function (data) {
                //             // $("#pin-and-password").html(data);
                //             // window.location.reload();

                //         },
                //     });
                //     return false;
                // });
                






            }
            else {
                console.log("PASSWORD IS FALSE");
                // ERROR MESSAGE
                var publicInfoForm = $('#PublicInfoForm');
                publicInfoForm.submit(function () {
                    $.ajax({
                        type: publicInfoForm.attr('method'),
                        url: publicInfoForm.attr('action'),
                        data: publicInfoForm.serialize(),
                        // data: formData.serialize(),
                        success: function (data) {
                            // $("#pin-and-password").html(data);
                            // window.location.reload();

                        },
                    });
                    return false;
                });
            }
        });
    });
    $('#public-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $(this)
            .find("input")
            .val('')
            .end()
            .find("input[type=password]")
            .prop("checked", "")
            .end();
    });






    $("#private-cancel-btn").on('click', function (e) {
        e.preventDefault();
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
        
    });

    $('#private-info-modal').on('click', function (e) {
        e.preventDefault();
        var password = $("#password-input2").data('password');

        $('#next-btn2').on('click', function (e) {
            var inputPassword = $("#password-input2").val();
            console.log(inputPassword);
            console.log(password);
            if (password == inputPassword) {
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
                $('#private-modal').modal('hide');
                
            }
            else {
                console.log("PASSWORD IS FALSE");
                // ERROR MESSAGE
            }
        });
    });
    $('#private-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $(this)
            .find("input")
            .val('')
            .end()
            .find("input[type=password]")
            .prop("checked", "")
            .end();
    });



    $("#pin-password-cancel-btn").on('click', function (e) {
        e.preventDefault();
        $('#pin-password-cancel-btn').css("display", "none");
        $('#pin-password-update-btn').css("display", "none");
        $('#pin-and-password-modal').css("display", "block");
        $("#master-password").prop("disabled", true);
        $("#employee-password").prop("disabled", true);
    });

    $('#pin-and-password-modal').on('click', function (e) {
        e.preventDefault();
        var password = $("#password-input3").data('password');

        $('#next-btn3').on('click', function (e) {
            var inputPassword = $("#password-input3").val();
            console.log(inputPassword);
            console.log(password);
            if (password == inputPassword) {
                $('#pin-password-cancel-btn').css("display", "block");
                $('#pin-password-update-btn').css("display", "block");
                $('#pin-and-password-modal').css("display", "none");
                $("#master-password").prop("disabled", false);
                $("#employee-password").prop("disabled", false);
                $('#pin-password-modal').modal('hide');
            }
            else {
                console.log("PASSWORD IS FALSE");
                // ERROR MESSAGE
            }
        });
    });
    $('#pin-password-modal').on('hidden.bs.modal', function () {
        console.log("CLOSE MODAL");
        $(this)
            .find("input")
            .val('')
            .end()
            .find("input[type=password]")
            .prop("checked", "")
            .end();
    });
















    // BETTER OPTIONS
    // 1) You can have one button on click sumbit multiple forms depends on if they are filled in
    // if you have 3 forms with 1 button, have them submitted within the same click but as its own form
    // as if each seperate form had its own button that the only visibal button connects together
    // 2) use Password button method - if input is empty, disable that input
    // this will remove that input from sending and you dont need to replace the blank input with the placeholder
    ////// SOLUTION NEEDED: find a way to not submit anything if the form is empty -- i may have done it
    $('#public-update-btn').on('click', function (e) {
        // e.preventDefault();
        var currentlocation = window.location.href;

        var hostleName = $("#hostle-name").attr('placeholder');
        var email = $(".email").attr('placeholder');
        var phone = $(".phone").attr('placeholder');
        var address = $(".address").attr('placeholder');
        var cityState = $("#city-state").attr('placeholder');
        var country = $("#country").attr('placeholder');

        var trimmedHostleName = jQuery.trim($('#hostle-name').val());
        var trimmedEmail = jQuery.trim($('.email').val());
        var trimmedPhone = jQuery.trim($('.phone').val());
        var trimmedAddress = jQuery.trim($('.address').val());
        var trimmedCityState = jQuery.trim($('#city-state').val());
        var trimmedCountry = jQuery.trim($('#country').val());
        
        $.ajax({
            url: currentlocation,
            beforeSend: function () {
                if (trimmedHostleName.length == 0) {
                    $("#hostle-name").val(hostleName);
                }
                if (trimmedEmail.length == 0) {
                    $(".email").val(email);
                }
                if (trimmedPhone.length == 0) {
                    $(".phone").val(phone);
                }
                if (trimmedAddress.length == 0) {
                    $(".address").val(address);
                }
                if (trimmedCityState.length == 0) {
                    $("#city-state").val(cityState);
                }
                if (trimmedCountry.length == 0) {
                    $("#country").val(country);
                }
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
                        // $(".settings-forms").html(data);
                    },
                    // error: function (data) {
                    //     $("#MESSAGE-DIV").html("Something went wrong!");
                    // }
                });
                return false;
            });
        });
    }); 
    
    $('#private-update-btn').on('click', function (e) {
        var currentlocation = window.location.href;

        var hostleName2 = $("#hostle-name2").attr('placeholder');
        var email2 = $("#email2").attr('placeholder');
        var phone2 = $("#phone2").attr('placeholder');
        var address2 = $("#address2").attr('placeholder');
        var cityState2 = $("#city-state2").attr('placeholder');
        var country2 = $("#country2").attr('placeholder');

        var fax = $("#fax").attr('placeholder');
        var website = $("#website").attr('placeholder');

        var ownerName = $("#owner-name").attr('placeholder');
        var ownerPhone = $("#owner-phone").attr('placeholder');
        
        var firstManagerName = $("#first-manager-name").attr('placeholder');
        var firstManagerPhone = $("#first-manager-phone").attr('placeholder');
        var firstManagerEmail = $("#first-manager-email").attr('placeholder');

        var secondManagerName = $("#second-manager-name").attr('placeholder');
        var secondManagerPhone = $("#second-manager-phone").attr('placeholder');
        var secondManagerEmail = $("#second-manager-email").attr('placeholder');

        var trimmedHostleName2 = jQuery.trim($('#hostle-name2').val());
        var trimmedEmail2 = jQuery.trim($('#email2').val());
        var trimmedPhone2 = jQuery.trim($('#phone2').val());
        var trimmedAddress2 = jQuery.trim($('#address2').val());
        var trimmedCityState2 = jQuery.trim($('#city-state2').val());
        var trimmedCountry2 = jQuery.trim($('#country2').val());

        var trimmedFax = jQuery.trim($('#fax').val());
        var trimmedWebsite = jQuery.trim($('#website').val());

        var trimmedOwnerName = jQuery.trim($('#owner-name').val());
        var trimmedOwnerPhone = jQuery.trim($('#owner-phone').val());

        var trimmedFirstManagerName = jQuery.trim($('#first-manager-name').val());
        var trimmedFirstManagerPhone = jQuery.trim($('#first-manager-phone').val());
        var trimmedFirstManagerEmail = jQuery.trim($('#first-manager-email').val());

        var trimmedSecondManagerName = jQuery.trim($('#second-manager-name').val());
        var trimmedSecondManagerPhone = jQuery.trim($('#second-manager-phone').val());
        var trimmedSecondManagerEmail = jQuery.trim($('#second-manager-email').val());

        $.ajax({
            url: currentlocation,
            beforeSend: function () {
                if (trimmedHostleName2.length == 0) {
                    $("#hostle-name2").val(hostleName2);
                }
                if (trimmedEmail2.length == 0) {
                    $("#email2").val(email2);
                }
                if (trimmedPhone2.length == 0) {
                    $("#phone2").val(phone2);
                }
                if (trimmedAddress2.length == 0) {
                    $("#address2").val(address2);
                }
                if (trimmedCityState2.length == 0) {
                    $("#city-state2").val(cityState2);
                }
                if (trimmedCountry2.length == 0) {
                    $("#country2").val(country2);
                }
                if (trimmedFax.length == 0) {
                    $("#fax").val(fax);
                }
                if (trimmedWebsite.length == 0) {
                    $("#website").val(website);
                }
                if (trimmedOwnerName.length == 0) {
                    $("#owner-name").val(ownerName);
                }
                if (trimmedOwnerPhone.length == 0) {
                    $("#owner-phone").val(ownerPhone);
                }
                if (trimmedFirstManagerName.length == 0) {
                    $("#first-manager-name").val(firstManagerName);
                }
                if (trimmedFirstManagerPhone.length == 0) {
                    $("#first-manager-phone").val(firstManagerPhone);
                }
                if (trimmedFirstManagerEmail.length == 0) {
                    $("#first-manager-email").val(firstManagerEmail);
                }
                if (trimmedSecondManagerName.length == 0) {
                    $("#second-manager-name").val(secondManagerName);
                }
                if (trimmedSecondManagerPhone.length == 0) {
                    $("#second-manager-phone").val(secondManagerPhone);
                }
                if (trimmedSecondManagerEmail.length == 0) {
                    $("#second-manager-email").val(secondManagerEmail);
                }
            }
        })
        $('#private-info-form').submit(function (event) {
            console.log("iot wokred");

            var frm2 = $('#private-info-form');
            frm2.submit(function () {
                $.ajax({
                    type: frm2.attr('method'),
                    url: frm2.attr('action'),
                    data: frm2.serialize(),
                    success: function (data) {
                        $("#private-contact-info").html(data);
                        // $(".settings-forms").html(data);
                    },
                    // error: function (data) {
                    //     $("#MESSAGE-DIV").html("Something went wrong!");
                    // }
                });
                return false;
            });
        });
    });

    $('#pin-password-update-btn').on('click', function (e) {
        // e.preventDefault();
        var currentlocation = window.location.href;
        var testingForm = $("#password-form :input[value='']");
        console.log(testingForm);
        
        // var employeePassword = $("#employee-password").data('password'); 
        // var trimmedEmployeePass = jQuery.trim($('#employee-password').val());       
        // $.ajax({
        //     url: currentlocation,
        //     beforeSend: function () {
        //         if (trimmedEmployeePass.length == 0) {
        //             $("#employee-password").val(employeePassword);
        //         }
        //     }
        // })

        // DISABLE EMPTY INPUT ELEMENTS
        var formData = $("#password-form .password-input").filter(function (index, element) {
            return $(element).val() == '';
        })
        console.log(formData.serialize());
        $(formData).prop("disabled", true);
        

        if (($('#master-password').is('[disabled=""]')) && ($('#employee-password').is('[disabled=""]'))) {
            console.log("They are both Empty");
            e.preventDefault();
            location.reload(true);
            //pass
        }
        else {
            $('#password-form').submit(function (event) {

                var frm3 = $('#password-form');
                frm3.submit(function () {
                    $.ajax({
                        type: frm3.attr('method'),
                        url: frm3.attr('action'),
                        data: frm3.serialize(),
                        // data: formData.serialize(),
                        success: function (data) {
                            $("#pin-and-password").html(data);
                        },
                    });
                    return false;
                });
            });
        } 
    }); 
});


