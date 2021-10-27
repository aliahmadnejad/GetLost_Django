jQuery(document).ready(function () {
    var phoneInput = document.querySelector("#phone");
    var phone = window.intlTelInput(phoneInput, {
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/11.0.14/js/utils.js",
    });
    $('#holder').submit(function (e) {
        e.preventDefault();
        var phoneNumber = phone.getNumber();
        $("#phone").val(phoneNumber);
        console.log($('#phone').val());
        document.getElementById("holder").submit();
    });
});