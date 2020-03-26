function draw(name,armor,stamina,skill,stats,damage,accuracy){
  var data = [
    {
      className: name, // optional can be used for styling
      axes: [
        {axis: "Armor", value: armor,yOffset:-10}, 
        {axis: "Stamina", value: stamina,xOffset:-55}, 
        {axis: "Skill", value: skill,yOffset:5,xOffset:-25},  
        {axis: "Damage", value: damage,yOffset:5,xOffset:57},  
        {axis: "Accuracy", value: accuracy,xOffset:64}
      ]
    }
  ];
  var chart = RadarChart.chart();

  RadarChart.defaultConfig.color = function() {};
  RadarChart.defaultConfig.radius = 3;
  RadarChart.defaultConfig.maxValue = 7;
  RadarChart.defaultConfig.levels = 7;
  // RadarChart.defaultConfig.w=300;
  RadarChart.defaultConfig.h=350;
  RadarChart.defaultConfig.tooltipFormatValue= function(d) {
    labels = ['F','D','C','B','A','S','SS']
    return labels[d-1];
  }

  var cfg = chart.config(); // retrieve default config
  var svg = d3.select('#chart').append('svg')
    .attr('width',cfg.w)
    .attr('height',cfg.h+50);
  svg.append('text')
    .attr('x',240)
    .attr('y',351)
    .text('SS')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',244)
    .attr('y',333)
    .text('S')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',243)
    .attr('y',312)
    .text('A')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',244)
    .attr('y',292)
    .text('B')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',243)
    .attr('y',273)
    .text('C')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',243)
    .attr('y',255)
    .text('D')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',243)
    .attr('y',235)
    .text('F')
    .attr('fill','grey');
  svg.append('g')
    .attr('transform',function(d, i){return 'translate(-55,35)';})
    .classed('single',1)
    .datum(data)
    .call(chart);

  d3.selectAll("."+name).classed('creature',true);

  var data = [
    {
      className: name, // optional can be used for styling
      axes: [
        {axis: "Strength", value: stats[0],yOffset:-10}, 
        {axis: "Dexterity", value: stats[1],xOffset:-55}, 
        {axis: "Constitution", value: stats[2],xOffset:-73},  
        {axis: "Intelligence", value: stats[3],yOffset:12},  
        {axis: "Wisdom", value: stats[4],xOffset:54},  
        {axis: "Charisma", value: stats[5],xOffset:64}
      ]
    }
  ];

  var chart = RadarChart.chart();

  RadarChart.defaultConfig.color = function() {};
  RadarChart.defaultConfig.radius = 3;
  RadarChart.defaultConfig.maxValue = 7;
  RadarChart.defaultConfig.levels = 7;
  // RadarChart.defaultConfig.w=300;
  RadarChart.defaultConfig.h=325;
  RadarChart.defaultConfig.tooltipFormatValue= function(d) {
    labels = ['F','D','C','B','A','S','SS']
    return labels[d-1];
  }

  var cfg = chart.config(); // retrieve default config
  var svg = d3.select('#chart-two').append('svg')
    .attr('width',cfg.w)
    .attr('height',cfg.h+50);
  svg.append('text')
    .attr('x',290)
    .attr('y',357)
    .text('SS')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',295)
    .attr('y',333)
    .text('S')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',294)
    .attr('y',310)
    .text('A')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',295)
    .attr('y',287)
    .text('B')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',294)
    .attr('y',263)
    .text('C')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',294)
    .attr('y',243)
    .text('D')
    .attr('fill','grey');
  svg.append('text')
    .attr('x',295)
    .attr('y',223)
    .text('F')
    .attr('fill','grey');
  svg.append('g')
    .attr('transform',function(d, i){return 'translate(0,35)';})
    .classed('single',1)
    .datum(data)
    .call(chart);

  d3.selectAll("."+name).classed('creature',true);
}
document.getElementById("creature_image").click();
// document.getElementById("creature_image")