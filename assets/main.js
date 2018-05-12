$(document).ready(function() {
	var $custom_file_upload = $('.custom_file');
	var $custom_file_upload_btn = $('.custom_file+label>span');
	var btn_upload_original_text = $custom_file_upload_btn.text();
	$custom_file_upload.on('change', function(e) {
		var $this = $(this);
		var fileName = $this.val();

		if( fileName )
			$custom_file_upload_btn.html(fileName.split('\\').pop());
		else
			$custom_file_upload_btn.html(btn_upload_original_text);
	});

	$('#login-form').on('submit', function(e) {
		e.preventDefault();

		$.ajax({
            url: '/login/',
            type: 'POST',
            data: $('#login-form').serialize(),
            success: function(data) {
                if(data.message == "success") {
                    window.location.href = data.url;
                } else {
					console.log(message);
					$("#error-msg").show().css("display", "flex");
                }
            },
            error: function(data) {
                if(data.status == 401)
                    $("#error-msg").show().css("display", "flex");
            }
        });
	});
});