jQuery(document).ready(function () {

    var phoneInput = document.querySelector("#phone");
    var faxInput = document.querySelector("#fax");
    var ownerPhoneInput = document.querySelector("#owner-phone");
    var firstManagerPhoneInput = document.querySelector("#first-manager-phone");
    var secondManagerPhoneInput = document.querySelector("#second-manager-phone");

    var phone = window.intlTelInput(phoneInput, {
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.14/js/utils.js",
    });
    var fax = window.intlTelInput(faxInput, {
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.14/js/utils.js",
    });
    var ownerPhone = window.intlTelInput(ownerPhoneInput, {
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.14/js/utils.js",
    });
    var firstManagerPhone = window.intlTelInput(firstManagerPhoneInput, {
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.14/js/utils.js",
    });
    var secondManagerPhone = window.intlTelInput(secondManagerPhoneInput, {
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.14/js/utils.js",
    });

    $('#body').submit(function (e) {
        e.preventDefault();
        var phoneNumber = phone.getNumber();
        var faxNumber = fax.getNumber();
        var ownerPhoneNumber = ownerPhone.getNumber();
        var firstManagerPhoneNumber = firstManagerPhone.getNumber();
        var secondManagerPhoneNumber = secondManagerPhone.getNumber();
        $("#phone").val(phoneNumber);
        $("#fax").val(faxNumber);
        $("#owner-phone").val(ownerPhoneNumber);
        $("#first-manager-phone").val(firstManagerPhoneNumber);
        $("#second-manager-phone").val(secondManagerPhoneNumber);
        console.log($('#phone').val());
        document.getElementById("body").submit();

        // var form = $('#body');
        // form.submit(function () {
        //     $.ajax({
        //         type: form.attr('method'),
        //         url: form.attr('action'),
        //         data: form.serialize(),
        //         success: function (data) {
        //             console.log("success");
                    
        //             // $("#body").html(data);
        //             // location.reload();
        //         },
        //     });
        //     return false;
        // });
        
    });
});

