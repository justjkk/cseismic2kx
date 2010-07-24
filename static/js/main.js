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
});

