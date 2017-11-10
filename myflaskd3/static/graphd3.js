var WINDOW_OFFSET = 50;
var IMAGE_SIZE = 50;

var svg = d3.select("svg")
    .attr("width", window.innerWidth)
    .attr("height", window.innerHeight);

var width = +svg.attr("width");
var height = +svg.attr("height");

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.name; })
           .strength(1)
           .distance(100))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(width / 2, height / 2));

graph = JSON.parse(myjson);

var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
    .attr("stroke-width", function(d) { return 5; })
    .attr("stroke", "black")
    .attr("stroke-dasharray", function(d)
    {
        if (d.wire == "Straight")
        {
            return "0";
        }
        else if (d.wire == "Crossover")
        {
            return "15, 5";
        }
    });

var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("g")
    .data(graph.nodes)
    .enter().append("g");

var vertices = node.append("image")
    .attr("height", IMAGE_SIZE + "px")
    .attr("width", IMAGE_SIZE + "px")
    .attr("href", function(d)
    {
        if (d.kind == "Host")
        {
            return 'media/computer.png';
        }
        else if (d.kind == "Switch")
        {
            return 'media/switch.png';
        }
        else if (d.kind == "Router")
        {
            return 'media/router.png'
        }
    })
    .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

labels = node.append("text")
    .text(function(d)
    {
        return d.name;
    })
    .attr("stroke-width", 0.3)
    .attr("stroke", "black")
    .attr("fill", "#EB5900");

simulation
    .nodes(graph.nodes)
    .on("tick", ticked)

simulation.force("link")
    .links(graph.links);


function bound(val, type)
{
    if (type == "horiz")
    {
        val = Math.min(val, width - WINDOW_OFFSET);
    }
    else if (type == "vertic")
    {
        val = Math.min(val, height - WINDOW_OFFSET);
    }
    val = Math.max(val, WINDOW_OFFSET);
    
    return val;
}

function ticked()
{
    console.log('ticked');
    vertices
        .attr("x", function(d)
        {
            d.x = bound(d.x, "horiz");
            return d.x - Math.floor(IMAGE_SIZE / 2);
        })
        .attr("y", function(d)
        {
            d.y = bound(d.y, "vertic");
            return d.y - Math.floor(IMAGE_SIZE / 2);
        });

    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });
    
    labels
        .attr("x", function(d) { return d.x - Math.floor(IMAGE_SIZE / 2); })
        .attr("y", function(d) { return d.y - Math.floor(IMAGE_SIZE / 2); });
}


function dragstarted(d)
{
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}


function dragged(d)
{
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}


function dragended(d)
{
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
}


window.addEventListener("resize", function()
{
    svg.attr("height", window.innerHeight);
    svg.attr("width", window.innerWidth);
    height = +svg.attr("height");
    width = +svg.attr("width");
    simulation
        .force("center", d3.forceCenter(width / 2, height / 2));
    simulation.alpha(1).restart();
});
