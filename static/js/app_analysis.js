const url = "http://127.0.0.1:5000/estimator";

/* data route */
    
d3.json(url).then (function(response){

          Plotly.newPlot('myDiv', response);
        }
    );
