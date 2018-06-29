/*
 * Main chart settings
 */
var REFRESH_INT = 1000; //ms
var BARS_BG = "rgb(120, 209, 225, 0.3)";
var BARS_BR = "rgb(206, 172, 50)";
var CHART_LABEL = "Top 10 voters";

/*
 * functions definitions
 */
function draw_chart(data_obj){
	/*
	 * Defines a chart.js barchart, flushing existing div container and re-drawing it
	 * 
	 * @param data_obj: list with data and metadata
	 * - data_obj.votes <- numeric data 
	 * - data_obj.names <- labels
	 * 
	 */
		
	$("#chart-container").html("");
    	
	if (data_obj){
    	var ctx = document.getElementById('voter-chart').getContext('2d');
    	var chart = new Chart(ctx, {
    	    type: 'bar',
    	    data: {
    	        labels: data_obj.names,
    	        datasets: [{
    	            label: CHART_LABEL,
    	            backgroundColor : BARS_BG,
    	            borderColor: BARS_BR,
    	            data: data_obj.votes,
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
    
    /* need returning itself for 1st setInteval 
     * call (I need graph rendered onload) 
     */
    
    return get_chart;
}


/*
 * main loop - chart drawing
 */
setInterval(get_chart(), REFRESH_INT);

