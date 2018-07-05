/*
 * Main chart settings
 */
var APP_NAME="Kcap Nevar"
var REFRESH_INT = 60000; // in ms
var BARS_BG = "rgb(120, 209, 225, 0.3)";
var BARS_BR = "rgb(206, 172, 50)";
var CHART_LABEL = APP_NAME + " - Top 10 voters";

/*
 * functions definitions
 */

function send_vote(){
	/*
	 * @summary: author user save vote, chart is updated and notification showed
	 * @return: function itself
	 */
	$.ajax({
			url: "/vote_manager/send_vote",
			success: function(data){
				// update existing chart 
				get_chart();
				
				pizza_notify({data:data});
			}
	})
	
	/* function is called in onclick handler parameter (which type is function). 
	 * see http://api.jquery.com/on
	 */
	
	return send_vote;
}


function pizza_notify(obj_input){
	/*
	 * @summary: notify wrapper
	 * @return: notification
	 * @param obj_input.data: text message [default: APP_NAME]
	 * @param obj_input.css_class: notification style. error, warning, success [default]
	 * @param obj_input.msg_position: top, bottom [default]
	 */
	
	var obj_par = {};
	obj_par.data = obj_input.data;
	obj_par.css_class = obj_input.css_class || "success";
	obj_par.msg_position = obj_input.msg_position || "bottom";
	
	
	$.notifyBar({ cssClass: obj_par.css_class, 
				  html: obj_par.data, 
				  position: obj_par.msg_position });
	
}

function draw_chart(data_obj){
	/*
	 * @summary: Defines a chart.js barchart, flushing existing div container and re-drawing it
	 * 
	 * @param data_obj: list with data and metadata
	 * [data_obj.votes]: numeric data 
	 * [data_obj.names]: labels
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
    	    options: {
			animation: false,
			        scales: {
            				yAxes: [{
                				ticks: {
                    					beginAtZero: true,
                                                        stepSize: 1
                				}
            				}]
        			}
                     }
    	});
    }
}

function get_chart(){
	/*
	 * @summary: Read async dataset, populate the chart
	 * @return: function itself
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
    
    /* function that returns itself: will be used in setInterval, 
     * so I need to be called on load, then repeated
     */
    
    return get_chart;
}


/*
 * main loop - chart drawing
 */
setInterval(get_chart(), REFRESH_INT);

