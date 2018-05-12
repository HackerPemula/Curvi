var onSubViewLoad = {
	filter: function() {

	}
};

$(document).ready(function() {
	var $nav_main = $('#nav_main');
	var $content = $('#content');

	$nav_main.on('click', '.nav_item', function(e) {
		var $this = $(this);
		$content.load('subview/'+$this.attr('target'), onSubViewLoad[$this.attr('target')]).hide().fadeIn(200);
		$('.active').removeClass('active');
		$this.addClass('active');
	});

	$content.on('click', '.iView', function() {

	});

	$content.on('click', '.iAccept', function() {

	});

	

	$('#nav_filter').trigger('click');
});