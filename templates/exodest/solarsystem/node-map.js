//create somewhere to put the force directed graph
var svg = d3.select("svg")

const width = window.innerWidth, height = window.innerHeight;

// const root = d3.hierarchy(data);
// const links = root.links();
// const nodes = root.descendants();

var nodes_data = [
    { "name": "Sun", "type": "Star", "size": 15, "color": "#FDB813" },
    { "name": "Mercury", "type": "Planet", "size": 5, "color": "#4f4cb0" },
    { "name": "Venus", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Earth", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Mars", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Jupiter", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Saturn", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Uranus", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Neptune", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Ceres", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Pluto", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Haumea", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Makemake", "type": "Planet", "size": 5, "color": "#c1440e" },
    { "name": "Eris", "type": "Planet", "size": 5, "color": "#c1440e" },
]


//Create links data 
var links_data = [
    { "source": "Sun", "target": "Earth", "distance": 100 },
    { "source": "Sun", "target": "Mercury", "distance": 200 },
    { "source": "Sun", "target": "Venus", "distance": 300 },
    { "source": "Sun", "target": "Earth", "distance": 400 },
    { "source": "Sun", "target": "Mars", "distance": 500 },
    { "source": "Sun", "target": "Jupiter", "distance": 600 },
    { "source": "Sun", "target": "Saturn", "distance": 700 },
    { "source": "Sun", "target": "Uranus", "distance": 800 },
    { "source": "Sun", "target": "Neptune", "distance": 900 },
    { "source": "Sun", "target": "Ceres", "distance": 1000 },
    { "source": "Sun", "target": "Pluto", "distance": 1100 },
    { "source": "Sun", "target": "Haumea", "distance": 1200 },
    { "source": "Sun", "target": "Makemake", "distance": 1300 },
    { "source": "Sun", "target": "Eris", "distance": 1400 }
]


//set up the simulation 
//nodes only for now 
var simulation = d3.forceSimulation()
    //add nodes
    .nodes(nodes_data);

//add forces
//we're going to add a charge to each node 
//also going to add a centering force
simulation
    .force("charge_force", d3.forceManyBody())
    .force("center_force", d3.forceCenter(width / 2, height / 2));


//draw circles for the nodes 
var node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(nodes_data)
    .enter()
    .append("circle")
    .attr("r", function (d) { return d.size })
    .attr("fill", function (d) { return d.color });



//add tick instructions: 
simulation.on("tick", tickActions);


//Time for the links 


//Create the link force 
//We need the id accessor to use named sources and targets 

var link_force = d3.forceLink(links_data)
    .id(function (d) { return d.name; })
    .distance(function (d) { return d.distance })

//Add a links force to the simulation
//Specify links  in d3.forceLink argument   


simulation.force("links", link_force)

//draw lines for the links 
var link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(links_data)
    .enter().append("line")
    .attr("stroke-width", 2);


function tickActions() {
    //update circle positions each tick of the simulation 
    node
        .attr("cx", function (d) { return d.x; })
        .attr("cy", function (d) { return d.y; });

    //update link positions 
    //simply tells one end of the line to follow one node around
    //and the other end of the line to follow the other node around
    link
        .attr("x1", function (d) { return d.source.x; })
        .attr("y1", function (d) { return d.source.y; })
        .attr("x2", function (d) { return d.target.x; })
        .attr("y2", function (d) { return d.target.y; });

}
