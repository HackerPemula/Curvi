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
});