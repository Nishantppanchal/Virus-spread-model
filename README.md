# Project
This project required me to model the spread of a virus within a computer network. This project was an assignment in VCE Algorithmics units 3&4.
# Documentation
Here I will talk about my model.
## Aspects of the project
### Aspects that were modelled
- Types of devices present.
- Speed of connections between the devices present.
- The platform each device run off.
- The time required to infect a computer.
- Certain devices may be invulnerable to a specific type of virus.
- Different types of viruses effecting device at different rates.
- Sensitivity of information present.
- Random generation a model.
- Connection types.

## My model
### Model of network
#### Features
- Types of devices present.
	-  This feature is critical as there is usually more than one type of device on a network. Furthermore, it allows different viruses to affect different device types at different speeds.
- Speed of connections between the devices present.
	- This feature is important as, in reality, not all connections are equal, and therefore, different kinds of connection have different speeds.
- The platform each device run off.
	- I choose this feature as it allows me to define even more specific how each virus affects each platform which each device type runs on differently
- The time required to infect different devices.
	- This allows us to specify the rate at which each virus affect different devices.
- Certain devices may be invulnerable to a specific type of virus.
	- This helps me emulate reality where some devices can’t be infected by some viruses.
- Different types of viruses.
	- This adds a diversity of viruses for the user to play with.
- Sensitivity of information present.
	- I choose to add this feature as in real life, some devices have more sensitive information than others, and therefore this helps more accurately reflect a real network.
- Random generation a model.
	- I choose to add this feature as it allows to use to see the effect of the virus on different networks that are generated randomly everything the program is run.
- Connection types.
	- I choose to add this feature as, usually, different device types can only connect through specific connection types.

## Model of virus spread
In this section I will talk about the algorithm I used to model the spread of the virus through a network.
### The algorithm
#### Steps
1. Add the starting node to a list.
2. If any of the values in the queue are nodes and have run out of time, find the edge that are connected to it and have not been traversed and add them to the list. After that, remove the value from the list.
3. If any of the values in the queue are edge and have run out of time, get the other node it is connected to and make sure the node has not been visited (if it has skip the rest of step 3). If this node is a sensor, make all the node adjacent to this node that have not been infected yet invulnerable. If the node is not, add it to the list. Otherwise, if it is vulnerable, do nothing (this still counts as visited). After that, remove the value from the list.
4. Add 1 to the timer.
5. Repeat step 2 and 4 until the list is empty.

#### Pseudocode

```
queue = list.create()
timer = 0
if the starting node has an integer value for timer required to infect and the starting node been not visited:
	queue.append(list.create(starting node, timer + time required to infect) 
	label the starting node as visited
While queue is not empty:
	for each value in queue:
		if the second element in the value (which is a list) is equal to or less than the timer:
			if the value represents a node:
				for all the edge connected to the node:
					if the edge has not been transversed:
						queue.append(list.create(edge, timer + weight + 1))
						label the edge as transversed
				remove the value from queue
			otherwise, if the value represents an edge:
				if the second value in the list is equal to the timer:
					if the node we are moving to has not been visited yet:
						if the node we are moving to is a sensor:
							label the node are moving to as visited
							for all the node adjacent to the node we are moving:
								if the node has not been visited:
									set the time required to infect to 'Protected'
						otherwise, if the time required to infect the node we are moving to is an integer:
							queue.append(list.create(node, timer + time required to infect + 1)) label the node as visited
						otherwise:
							remove the value from queue
	add 1 to timer 
```

### Key features
- This algorithm allows for there to be a wait before an edge is infected or transversed, allowing me to specific how long it takes to infect a node or transverse an edge.
- This algorithm utilises a list unlike many other transversal algorithms studied in class, which mostly utilised stacks and queues.
- This algorithm allows me to determine how long it takes to infect all the possible node without any other calculation.
- This algorithm allows multiple instances of itself to be deployed at the same time on to one graph without any conflict between the algorithms occurring. 
- This algorithm infects all the adjacent node at the same time.
- It allows for the implementation of a sensor. In my model, a sensor is piece of software which can be deployed on any device. When the virus attempts to infect the device, the sensor is deployed on, the sensor detects the Virus and prevent it from infecting the device and provides the adjacent nodes that have not been infect with immunity to the virus. 
