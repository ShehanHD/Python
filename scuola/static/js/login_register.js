$("index.temp.html").ready(function () {
    $('#register').on('click', function() {
        name1 = $("#name").val();
    $.ajax({
        type: "GET",
        url: "req_register/register",
        data: {
            name : $("#name").val(),
            surname : $('#surname').val(),
            csrfmiddlewaretoken : "{{ csrf_token }}"
        },
        success: function (response) {
            console.log(response);
        },
        error: function (response){
            console.error(response);
        }
    });
	});
});