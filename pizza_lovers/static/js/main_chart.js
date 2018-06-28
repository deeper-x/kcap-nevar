/*
 * Main chart settings
 */
var REFRESH_INT = 60000; //in ms
var BARS_BG = "rgb(120, 209, 225, 0.3)";
var BARS_BR = "rgb(206, 172, 50)";
var CHART_LABEL = "Top 10 voters";

/*
 * functions definitions
 */
function draw_chart(array_to_send){
	/*
	 * Defines a chart.js barchart, flushing existing div container and re-drawing it
	 * 
	 * @param array_to_send: list with data and metadata
	 * - array_to_send[0] := numeric data 
	 * - array_to_send[1] := labels
	 * 
	 */
	$("#chart-container").html("");
    if (array_to_send){
    	var ctx = document.getElementById('voter-chart').getContext('2d');
    	var chart = new Chart(ctx, {
    	    type: 'horizontalBar',
    	    data: {
    	        labels: array_to_send[0],
    	        datasets: [{
    	            label: CHART_LABEL,
    	            backgroundColor : BARS_BG,
    	            borderColor: BARS_BR,
    	            data: array_to_send[1],
    	        }]
    	    },
    	    options: {animation: false}
    	});
    }
}

function get_chart(){
	/*
	 * Given a dataset, populate the chart
	 */
    var ret_val = $.ajax({
        url: '/vote_manager/get_voters_top_ten',
        dataType: 'json',
        error: function(){
            console.log("Error fetching voters data...");
        }
    }).done(function(data){
    	draw_chart(data);
    });
    
    /* need returning itself for 1st setInteval call (graph drawn immediately) */
    return get_chart;
}


/*
 * main loop - chart drawing
 */
setInterval(get_chart(), REFRESH_INT);

