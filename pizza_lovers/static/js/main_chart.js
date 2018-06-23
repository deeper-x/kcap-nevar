var array_to_send = null;

function populate_data_array(){
    var ret_val = $.ajax({
        url: '/vote_manager/get_voters_top_ten',
        dataType: 'json',
        processData: false,
        error: function(){
            console.log("Error fetching voters data...");
        }
    }).done(function(data){
        array_to_send = data;
    });
}


function draw_chart(){
    populate_data_array();

    if (array_to_send){
        $("#chart-container").html("");
        var svg_obj = d3.select("#chart-container").append("svg").attr("height","100%").attr("width","100%");

        svg_obj.selectAll("rect")
                                .data(array_to_send)
                                .enter()
                                .append("rect")
                                .attr("class", "voter-bar")
                                .attr("height",function(d, i) {return (d * 10)})
                                .attr("width","40")
                                .attr("x",function(d, i) {return i * 60 + 25;})
                                .attr("y", function(d, i) {return 400 - (d * 10)});

    }

}

function main(){
    draw_chart();
    setInterval(draw_chart, 1000);
}


main();