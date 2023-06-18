jQuery(document).ready(function($){
	let isLateralNavAnimating = false;
	$('.cd-nav-trigger').on('click', (e) => {
		e.preventDefault();
		if( !isLateralNavAnimating ) {
			if($(this).parents('.csstransitions').length > 0 ) isLateralNavAnimating = true; 
			$('body').toggleClass('navigation-is-open');
			$('.cd-navigation-wrapper').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', 
			() => {
				isLateralNavAnimating = false;
			});
		}
	});
});
