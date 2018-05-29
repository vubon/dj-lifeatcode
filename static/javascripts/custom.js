// pie chart window.onload = function () 
window.onload = function () {
		CanvasJS.addColorSet("piecolor",
		   [//colorSet Array
		    "#418CCB",
		    "#6633cc",
		    "#2ecc71",
		    "#00A7E4",
		    "#5BBC2E",            
		    "#009a00"            
		]);

			var chart = new CanvasJS.Chart("containerchart",{
				colorSet: "piecolor",
				backgroundColor: "#ECEEF3",
				title:{
					text: "Performance sets",
					fontFamily:'Raleway-Thin',
					fontSize:20
				},
		        animationEnabled: true,
				legend:{
					verticalAlign: "bottom",
					horizontalAlign: "center"
				},
				
				data: [
				{        
					indexLabelFontSize: 20,
					indexLabelFontFamily: "Monospace",       
					indexLabelFontColor: "darkgrey", 
					indexLabelLineColor: "darkgrey",        
					indexLabelPlacement: "outside",
					type: "pie",       
					showInLegend: true,
					toolTipContent: "{y} - <strong>#percent%</strong>",
					dataPoints: [
						{  y: 95, legendText:"Coding", indexLabel: "Coding" },
						{  y: 95, legendText:"Designing", indexLabel: "Designing" },
						{  y: 95, legendText:"Creativity",exploded: true, indexLabel: "Creativity" },
						{  y: 95, legendText:"Cummunication" , indexLabel: "Cummunication"},
						{  y: 95, legendText:"Feedback", indexLabel: "Feedback" },
						{  y: 95, legendText:"Success" , indexLabel: "Success"}		
				]		
					
			}
		]
	});
	chart.render();
}