function draw_chart(array_to_send){
	$("#chart-container").html("");
	
    if (array_to_send){
    	var ctx = document.getElementById('voter-chart').getContext('2d');
    	var chart = new Chart(ctx, {
    	    type: 'horizontalBar',
    	    
    	    data: {
    	        labels: array_to_send[0],
    	        datasets: [{
    	            label: "Top 10 voters",
    	            backgroundColor : "rgb(67, 127, 168, 0.3)",
   	              borderColor : "#111",
    	          borderColor: "rgb(206, 172, 50)",
    	          data: array_to_send[1],
    	        }]
    	    },

    	    options: {animation: false}
    	});

    }
}

function main(){
    var ret_val = $.ajax({
        url: '/vote_manager/get_voters_top_ten',
        dataType: 'json',
        processData: false,
        error: function(){
            console.log("Error fetching voters data...");
        }
    }).done(function(data){
    	draw_chart(data);
    });
    
    /* need returning itself for 1st setInteval call (graph drawn immediately) */
    return main;
}

setInterval(main(), 1000);

