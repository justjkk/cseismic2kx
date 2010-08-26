$(document).ready( function() {
    $('#datepicker').datepicker({
	    inline: true
    });
    $('#news').innerfade({
        animationtype: 'fade',
    	speed: 'slow',
    	timeout: '4000',
    	type: 'sequence',
    	containerheight: '25px',
    	runningclass: 'innerfade',
    });
    $('#news').css({ visibility: "visible"});
    $('#menu').jqDock({labels: true, size: "80px"});
	var symposiumDay = new Date(2010,7,28,8,0,0);
	$('#glowingLayout').countdown({
	    until: symposiumDay,
	    compact: false,
	    layout: '<div class="image{d10}"></div><div class="image{d1}"></div>' + 
        '<div class="imageDay"></div><div class="imageSpace"></div>' + 
        '<div class="image{h10}"></div><div class="image{h1}"></div>' + 
        '<div class="imageSep"></div>' + 
        '<div class="image{m10}"></div><div class="image{m1}"></div>' + 
        '<div class="imageSep"></div>' + 
        '<div class="image{s10}"></div><div class="image{s1}"></div>'
	});
});

