# Importing required libraries.
import random
from pynode.main import *
import time

# Creating a function to check if the edge already exists.
def checkEdge(node1, node2, edges):
    exists = False # set exists to false by default.
    # All the edges in the list edges are gone throught, and if the edge does exist, the values of exists is set to true and the loop is broken.
    for edge in edges: 
        if (node1 == edge[0] and node2 == edge[1]) or (node1 == edge[1] and node2 == edge[0]):
            exists = True
            break
    return exists

# The custom operation for dictionary called TOTAL is defined (refer to documentation for what it does):
def total(d):
    # For every value in the dictionary d, it check if the value is a dictionary.
    for value in d.values():
        if isinstance(value, dict):
            # If the value is a dictionary, is use the total function on the value.
            yield from total(value)
        else:
            # If the value is not a dictionary, then the function returns the value as a iterator. This function can be classifed as a generator, but we will not move throught
            # the values, but instead place all of the iterators into a list.
            yield value

# We define the function that generates the graph.
def generateGraph():
    global edges, nodes
    
    #------------------------------------------------------------Generates Nodes------------------------------------------------------------#
    #numberOfNodes = random.randint(50, 100) # The number of node is randomly pick from a number inbetween 50 and 100 inclusive.
    numberOfNodes = 20
    
    # The deviceTypes dataset is defined.
    deviceTypes = ['Desktop', 'Mobile', 'Tablet', 'Smartwatch', 'Data server', 'Wifi router', 'Laptop', 'Smart TV', 'Smart camera', 'Smart light'] 
    
    # The platforms dataset is defined.
    platforms = {'Desktop': ['Windows 10', 'MacOS', 'Linux'],
                 'Mobile': ['Android', 'iOS'],
                 'Tablet': ['Android', 'ipadOS'], 
                 'Smartwatch': ['Wear OS', 'Tizen OS', 'WatchOS'],
                 'Data server': ['Linux', 'Windows server'],
                 'Wifi router': ['Linux'],
                 'Laptop': ['Windows 10', 'Windows 10X', 'Linux', 'MacOS'],
                 'Smart TV': ['Android TV', 'Tizen OS', 'tvOS'],
                 'Smart camera': ['Custom'],
                 'Smart light': ['Custom']}
    
    # The viruses dataset is defined.
    viruses = ['File-infecting virus', 'Marco virus', 'Browser hijacker', 'Boot sector virus', 'Polymorphic virus', 'Multipartite virus']
    
    # The user is asked to pick a virus in the terminal. The while loop is not required. I have just added it in to prevent error from 
    # occuring when the user doesn't enter a integer
    while True:
        try:
            virusSelected = int(input('Select the type of virus:\n'
                                ' 1 - File-infecting virus\n'
                                ' 2 - Marco virus\n'
                                ' 3 - Browser hijacker\n'
                                ' 4 - Boot sector virus\n'
                                ' 5 - Polymorphic virus\n'
                                ' 6 - Multipartite virus\n'
                                'Enter number here: ')) - 1
            if 1 <= virusSelected + 1 <= 6:
                break
            else:
                print('_________________________________________')
                print('Please enter a number in between 1 and 6.')
                print('_________________________________________')
        except:
            print('______________________________________________')
            print('You did not enter a integer. Please try again.')
            print('______________________________________________')
    
    # The timesInfectingNodes dataset is defined.
    timeInfectingNodes = {'File-infecting virus':   {'Desktop': {'Windows 10': 45, 'MacOS': 55, 'Linux': 60},
                                                    'Mobile': {'Android': 50, 'iOS': None},
                                                    'Tablet': {'Android': 50, 'ipadOS': 80},
                                                    'Smartwatch': {'Wear OS': 0, 'Tizen OS': 0, 'WatchOS': 10},
                                                    'Data server': {'Linux': 60, 'Windows server': 50},
                                                    'Wifi router': {'Linux': 60},
                                                    'Laptop': {'Windows 10': 45, 'Windows 10X': 70, 'Linux': 60, 'MacOS': 55},
                                                    'Smart TV': {'Android TV': 35, 'Tizen OS': 0, 'tvOS': 20},
                                                    'Smart camera': {'Custom': 38},
                                                    'Smart light': {'Custom': 38}},
                            'Marco virus':          {'Desktop': {'Windows 10': 10, 'MacOS': 20, 'Linux': 15},
                                                    'Mobile': {'Android': 80, 'iOS': 80},
                                                    'Tablet': {'Android': 80, 'ipadOS': 80},
                                                    'Smartwatch': {'Wear OS': None, 'Tizen OS': None, 'WatchOS': None},
                                                    'Data server': {'Linux': 15, 'Windows server': 18},
                                                    'Wifi router': {'Linux': 15},
                                                    'Laptop': {'Windows 10': 10, 'Windows 10X': 11, 'Linux': 15, 'MacOS': 20},
                                                    'Smart TV': {'Android TV': 90, 'Tizen OS': 100, 'tvOS': 95},
                                                    'Smart camera': {'Custom': None},
                                                    'Smart light': {'Custom': None}},
                            'Browser hijacker':     {'Desktop': {'Windows 10': 0, 'MacOS': 0, 'Linux': 10},
                                                    'Mobile': {'Android': 50, 'iOS': None},
                                                    'Tablet': {'Android': 50, 'ipadOS': 80},
                                                    'Smartwatch': {'Wear OS': 0, 'Tizen OS': 0, 'WatchOS': 10},
                                                    'Data server': {'Linux': 10, 'Windows server': 50},
                                                    'Wifi router': {'Linux': 10},
                                                    'Laptop': {'Windows 10': 0, 'Windows 10X': 0, 'Linux': 10, 'MacOS': 0},
                                                    'Smart TV': {'Android TV': 10, 'Tizen OS': 20, 'tvOS': 30},
                                                    'Smart camera': {'Custom': None},
                                                    'Smart light': {'Custom': None}},
                            'Boot sector virus':    {'Desktop': {'Windows 10': 10, 'MacOS': 30, 'Linux': 50},
                                                    'Mobile': {'Android': 0, 'iOS': 0},
                                                    'Tablet': {'Android': 0, 'ipadOS': 0},
                                                    'Smartwatch': {'Wear OS': 70, 'Tizen OS': 65, 'WatchOS': 90},
                                                    'Data server': {'Linux': 50, 'Windows server': 75},
                                                    'Wifi router': {'Linux': 50},
                                                    'Laptop': {'Windows 10': 10, 'Windows 10X': 15, 'Linux': 50, 'MacOS': 30},
                                                    'Smart TV': {'Android TV': 0, 'Tizen OS': 0, 'tvOS': 0},
                                                    'Smart camera': {'Custom': 100},
                                                    'Smart light': {'Custom': 100}},
                            'Polymorphic virus':    {'Desktop': {'Windows 10': 0, 'MacOS': 0, 'Linux': 0},
                                                    'Mobile': {'Android': 0, 'iOS': 0},
                                                    'Tablet': {'Android': 0, 'ipadOS': 0},
                                                    'Smartwatch': {'Wear OS': 0, 'Tizen OS': 0, 'WatchOS': 0},
                                                    'Data server': {'Linux': 0, 'Windows server': 0},
                                                    'Wifi router': {'Linux': 0},
                                                    'Laptop': {'Windows 10': 0, 'Windows 10X': 70, 'Linux': 0, 'MacOS': 0},
                                                    'Smart TV': {'Android TV': 0, 'Tizen OS': 0, 'tvOS': 0},
                                                    'Smart camera': {'Custom': 0},
                                                    'Smart light': {'Custom': 0}},
                            'Multipartite virus':   {'Desktop': {'Windows 10': 63, 'MacOS': 54, 'Linux': 86},
                                                    'Mobile': {'Android': 79, 'iOS': None},
                                                    'Tablet': {'Android': 79, 'ipadOS': None},
                                                    'Smartwatch': {'Wear OS': 110, 'Tizen OS': 100, 'WatchOS': 95},
                                                    'Data server': {'Linux': 86, 'Windows server': 67},
                                                    'Wifi router': {'Linux': 86},
                                                    'Laptop': {'Windows 10': 63, 'Windows 10X': 63, 'Linux': 86, 'MacOS': 54},
                                                    'Smart TV': {'Android TV': None, 'Tizen OS': 80, 'tvOS': 90},
                                                    'Smart camera': {'Custom': 0},
                                                    'Smart light': {'Custom': 0}}        
    }
    
    # The times that are required to infect a node are sorted and filter.
    listOfTimes = list(total(timeInfectingNodes)) # Get iterators, each on being a value, and places them in a list.
    filteredListOfTimes = [v for v in listOfTimes if type(v) == int] # Filter the list of all the times and only keeps the integers.
    sortedTimes = sorted(filteredListOfTimes) # Sorts the filtered list of times into ascending order.

    # The informationSensitivityArray dataset is defined.
    informationSensitivityArray = ['Low', 'Medium', 'High']
    
    # The connectionTypes dataset is defined.
    connectionTypes = [
        [['USB A', 'Ethernet'], ['USB C'], ['USB C'], ['USB A'], ['Fibre optics'], ['Ethernet'], ['USB A', 'USB C'], ['HDMI', 'USB A'], ['USB A', 'WiFi'], ['WiFi']],
        [['USB C'], ['USB C', 'NFC', 'WiFi', 'Bluetooth'], ['USB C', 'WiFi', 'Bluetooth'], ['Bluetooth'], ['Cellular'], ['WiFi'], ['USB C', 'WiFi', 'Bluetooth'], ['Bluetooth'], ['Bluetooth', 'WiFi'], ['Bluetooh', 'WiFi']],
        [['USB C'], ['USB C', 'WiFi', 'Bluetooth'], ['USB C', 'WiFi', 'Bluetooth'], ['Bluetooth'], ['Cellular'], ['WiFi'], ['USB C', 'WiFi', 'Bluetooth'], ['Bluetooth'], ['Bluetooth', 'WiFi'], ['Bluetooh', 'WiFi']],
        [['USB A'], ['Bluetooth'], ['Bluetooth'], ['Bluetooth', 'NFC'], ['Cellular', 'WiFi'], ['WiFi'], ['Bluetooth'], ['Bluetooth'], ['Bluetooth', 'WiFi'], ['Bluetooth', 'WiFi']],
        [['Fibre optics'], ['Cellular'], ['Cellular'], ['Cellular', 'WiFi'], ['Fibre optics'], ['Fibre optics'], ['WiFi'], ['WiFi'], ['WiFi'], ['WiFi']],
        [['Ethernet'], ['WiFi'], ['WiFi'], ['WiFi'], ['Fibre optics'], ['WiFi'], ['WiFi'], ['WiFi'], ['WiFi'], ['WiFi']],
        [['USB A', 'USB C'], ['USB C', 'WiFi', 'Bluetooth'], ['USB C', 'WiFi', 'Bluetooth'], ['Bluetooth'], ['WiFi'], ['WiFi'], ['USB C', 'Bluetooth', 'WiFi'], ['HDMI', 'Bluetooth'], ['WiFi', 'Bluetooth'], ['WiFi', 'Bluetooth']],
        [['HDMI', 'USB A'], ['Bluetooth'], ['Bluetooth'], ['Bluetooth'], ['WiFi'], ['WiFi'], ['HDMI', 'Bluetooth'], ['HDMI', 'Bluetooth'], ['Bluetooth', 'WiFi'], ['Bluetooth', 'WiFi']],
        [['USB A', 'WiFi'], ['Bluetooth', 'WiFi'], ['Bluetooh', 'WiFi'], ['Bluetooth', 'WiFi'], ['WiFi'], ['WiFi'], ['WiFi', 'Bluetooth'], ['Bluetooth', 'WiFi'], ['WiFi'], ['WiFi']],
        [['WiFi'], ['Bluetooth', 'WiFi'], ['Bluetooh', 'WiFi'], ['Bluetooth', 'WiFi'], ['WiFi'], ['WiFi'], ['WiFi', 'Bluetooth'], ['Bluetooth', 'WiFi'], ['WiFi'], ['WiFi']]
    ]
    
    # This for loop repeat the code the number of node we define earlier.
    for i in range(0, numberOfNodes):
        node = graph.add_node(id=i) # Creates a node with id of the i the for loop is at.
        
        randomDeviceType = random.choice(deviceTypes) # randomly picks a device type.
    
        randomPlatform = random.choice(platforms[randomDeviceType]) # Randomly picks a platform.
        
        # Checks to make sure that the time required to infect is a integer.
        if type(timeInfectingNodes[viruses[virusSelected]][randomDeviceType][randomPlatform]) is int:
            # Add an element of randomness to the time required to infect.
            time = timeInfectingNodes[viruses[virusSelected]][randomDeviceType][randomPlatform] + random.randint(-10, 10) 
            
            # If the time goes below 0, it be default back to 0.
            if time < 0:
                time = 0
            
            index = 0 # The index is defaulted to 0.
            # Keeps looping the code until broken.
            while True:
                value = sortedTimes[index] # gets the value at index [whatever the value of the variable index is] and set the variable, value, to that value.
                # If value is greater than time, substrates 1 from the index and breaks the while loop.
                if value > time:
                    index -= 1
                    break
                # Otherwise, if value is equal to time, the breaks the while.
                elif value == time:
                    break
                
                # If the lenght of the list, sortedTimes, is the greater then index+1, then adds on to the index.
                if len(sortedTimes) > index+1:
                    index += 1
                # If the lenght of the list, sortedTimes, is equal to index+1, then breaks the while loop.
                elif len(sortedTimes) == index+1:
                    break
        
            # Do math to find the percentile the time is in.
            percentile = int((index/len(listOfTimes))*100)
            # Divide the percentile by 10 to find the rating.
            rating = percentile/10
            
        # If the time required to infect the node is not a integer, then set the time to 'None', make the node black in colour and sets the rating to 10.
        else:
            time = 'None' 
            node.set_color(color=Color.BLACK)
            rating = 10
        
        # The sensitivity level is randomly selected
        sensitivityLevel = random.choice(informationSensitivityArray)

        # All the properties of the node are placed into a dictionary
        nodeData = {'Device type': randomDeviceType,
                    'Platform': randomPlatform,
                    'Time required to infect': time,
                    'Security rating': rating,
                    'Sensitivity of information present': sensitivityLevel,
                    'Visited': False,
                    'Sensor': False}

        # The dictionary contianing properites of the node is placed into a dictionary with the key as the nodes id
        nodes[i] = nodeData
        
        # Set all the labels of the node
        node.set_label(nodeData['Security rating'], label_id=0)
        node.set_label(nodeData['Platform'], label_id=1)
        node.set_value(nodeData['Device type'])
        
        
        #------------------------------------------------------------Generates Edges------------------------------------------------------------#
        
        # We are not on the first node    
        if i > 0:
            node1Index = deviceTypes.index(graph.node(i).value()) # Gets the index of the device type of node with the id i in the list, deviceTypes.
            node2Index = deviceTypes.index(graph.node(i-1).value()) # Gets the index of the device type of node with the id i-1 in the list, deviceTypes.
            # A random value from all the possible connection types between the two device types of i and i-1.
            connectionType = random.choice(connectionTypes[node1Index][node2Index])
            
            # The properties of a edge is placed into a dictionary.
            edgeData = {'Connection Type': connectionType, 
                        'Weight': random.randint(1, 60),
                        'Transversed': False}
            edge = graph.add_edge(i, i-1, weight=edgeData['Weight']) # Creates an edge between i and i-1
            edges.append([i, i-1, edgeData]) # Add the information about the edge to the list, edges.
            
            # If there are more then 3 edges in list, nodes.
            if len(nodes) > 3:
                # Create either 0, 1 or 2 edges.
                for j in range(0, random.randint(0, 2)):
                    x = 0 # set x to 0
                    # Allow me to try the follow code 10 times
                    while x < 10:
                        x += 1
                        
                        randomNode = random.choice(list(nodes.keys())) # Gets a random node
                        
                        nodeIndex = deviceTypes.index(graph.node(i).value()) # Gets the index of the device type of node with the id i in the list, deviceTypes.
                        randomNodeIndex = deviceTypes.index(graph.node(randomNode).value()) # Gets the index of the device type of node with the id i-1 in the list, deviceTypes.
                        # A random value from all the possible connection types between the two device types of i and i-1.
                        connectionType = random.choice(connectionTypes[nodeIndex][randomNodeIndex])
                        
                        # The properties of a edge is placed into a dictionary.
                        edgeData = {'Connection Type': connectionType, 
                                    'Weight': random.randint(1, 60),
                                    'Transversed': False}
                        
                        # If the edge doesn't already exist and the random node selected has less then 3 edges connected to it and i and randomNode are not the same.
                        if checkEdge(i, randomNode, edges) == False and graph.node(randomNode).degree() < 3 and i != randomNode:
                            edge = graph.add_edge(i, randomNode, weight=edgeData['Weight']) # Creates an edge between i and random node selected
                            edges.append([i, randomNode, edgeData]) # Add the information about the edge to the list, edges.
                            #pause(500) # Pauses for 0.5 seconds or 500 milliseconds to make generation look smoother
                            break # break out of the while loop
        
        #pause(500) # Add a 500 milliseconds delay to make the generation smoother
 
# This block of code allow sensors to be added. 
def addSensor(node): # Defines the addSensor function
    global nodes # Imports the global variable nodes.
    nodeID = node.id() # This get the node ID and places it in the variable nodeID
    nodes[nodeID]['Sensor'] = True # This labels the node as a sensor
    nodes[nodeID]['Time required to infect'] = None # This makes the node uninfectable
    nodes[nodeID]['Security rating'] = 10 # This sets the security rating to 10
    node.set_color(color=Color(128,0,128)) # This changes thr color to purple
    node.set_label(10, label_id=0) # This change the security rating displayed on the graph to 10

def tranverse(startingNode):
    global speed, edges, nodes # Imports the global variables speed, edges and nodes
    
    startingNodeID = startingNode.id() # This gets the ID of the node that was clicked one and places it in the variable startingNodeID
    startingNodeData = nodes[startingNodeID] # This gets the data for node and places it in the variable startingNodeData
    timer = 0 # Sets the timer to zero
    timeDifference = 0 # Sets the time difference to zero
    queue = [] # Creates a list (I will call it the list from now on)

    if type(startingNodeData['Time required to infect']) is int and nodes[startingNodeID]['Visited'] == False: # Makes sure the node we clicked cann be infected and has not already been infected
        queue.append(['node', startingNode, startingNodeData['Time required to infect']]) # Add the nodes to the list 
        nodes[startingNodeID]['Visited'] = True # Labels the node as visited
        startingNode.set_color(color=Color.BLUE) # Colors the node blue
    
    # This while loop run the block of code below while the list is not 
    while queue:
        t0 = time.time_ns() # This get the current time in nanoseconds
    
        for i in queue: # This iterates throught all the elements in the list
            if i[2] <= timer: # If the item in the list has run out time
                if i[0] == 'node': # If the element represents a node
                    # The 6 lines of code below change the color of node infect based on the senstivity of information present
                    if nodes[i[1].id()]['Sensitivity of information present'] == 'Low':
                        i[1].set_color(color=Color.YELLOW)
                    elif nodes[i[1].id()]['Sensitivity of information present'] == 'Medium':
                        i[1].set_color(color=Color(255,165,0)) 
                    elif nodes[i[1].id()]['Sensitivity of information present'] == 'High':
                        i[1].set_color(color=Color(255,0,0))
                    for j in i[1].incident_edges(): # This runs through all the edge going out of the node
                        index = [n for n, val in enumerate(edges) if (val[0] == j.source().id() and val[1] == j.target().id())][0] # This gets the index for edge data between the two edges
                        edgeData = edges[index][2] # This put the edge data into the a variable edgeData
                        if edgeData['Transversed'] is False: # If the edge has not been tranversed yet
                            queue.append(['edge', j, edgeData['Weight'] + timer + 1, i[1], j.other_node(i[1])]) # Add the edge to the list
                            j.set_color(color=Color.BLUE) # Makes the edge blue
                            edges[index][2]['Transversed'] = True # Label the edge as transversed 
                        
                elif i[0] == 'edge': # If the element is a edge
                    if nodes[i[4].id()]['Visited'] is False: # If the node we are moving to has not be visited
                        if nodes[i[4].id()]['Sensor'] is True: # If the node we are moving to to is a sensor
                            i[1].traverse(initial_node=i[3], color=Color.DARK_GREY, keep_path=True) # Play transversal animation 
                            nodes[i[4].id()]['Visited'] = True # Label the node we are moving to as visited
                            adjacentNodes = i[4].adjacent_nodes() # Get the nodes adjacent to the node we are moving to
                            i[4].set_color(color=Color(255, 192, 203)) # Change the color of the node
                            for j in adjacentNodes: # Goes through all the list of adjacent nodes
                                if nodes[j.id()]['Visited'] is False: # If the node has not been visited yet
                                    # The code below makes the node immune to the virus and set the time required to infect as 'Protected'
                                    j.set_color(color=Color(146, 210, 226))
                                    nodes[j.id()]['Time required to infect'] = 'Protected'
                                    nodes[j.id()]['Security rating'] = 10
                                    j.set_label(10, label_id=0)
                                    graph.edges_between(i[4], j, directed=False)[0].set_color(color=Color(146, 210, 226)) # Plays tranversal animation
                        elif type(nodes[i[4].id()]['Time required to infect']) is int: # If the time required to infect is a integar
                            i[1].traverse(initial_node=i[3], color=Color.DARK_GREY, keep_path=True) # Play transversal animation 
                            queue.append(['node', i[4], nodes[i[4].id()]['Time required to infect'] + timer + 1]) # Add node we are moving to to the list
                            i[4].set_color(color=Color.BLUE) # Change color of the node we are moving to to blue
                            nodes[i[4].id()]['Visited'] = True # Label the node are moving to as visited
                        elif nodes[i[4].id()]['Time required to infect'] == 'Protected': # If the node we are moving has been provided immunity by a sensor
                            i[1].traverse(initial_node=i[3], color=Color.DARK_GREY, keep_path=True) # Play transversal animation
                            i[4].set_color(color=Color(	2, 88, 57)) # Change the color of the node we are moving to
                            nodes[i[4].id()]['Visited'] = True # Label the node we are moving to as visited
                        else: # Otherwise
                            i[1].traverse(initial_node=i[3], color=Color.DARK_GREY, keep_path=True) # Play transversal animation 
                            i[4].set_color(color=Color.GREEN) # Change colour of node we are moving to to green
                            nodes[i[4].id()]['Visited'] = True # Label the node we are moving to as visited
                    elif nodes[i[4].id()]['Visited'] is True: # If the node we are moving to has been visited
                            i[1].set_color(color=Color.LIGHT_GREY) # Set the color of the edge to light grey
                            i[1].traverse(initial_node=i[4], color=Color.DARK_GREY, keep_path=False) # Play the transversal animation
                queue.remove(i) # Remove the element from the list
                    
        timer += 1 # Add one to the timer
        pause(int((1000-timeDifference)/speed)) # Pause accounting for the extra time that the code ran for in the last pause       
        t1 = time.time_ns() # Get the current time in nanoseconds
        timeDifference = (t1-t0)/1000000 - (1000/speed) # Find the extra time the code required to run

    if timer > 0: # If the timer is more than 1
        # Get the device type and platform of the starting node
        deviceType = startingNodeData['Device type'] 
        platform = startingNodeData['Platform']
        # Print the time take for this instance to infect all the possible nodes.
        print(f'\nIt took {timer} seconds for the virus deployed at the node with the ID {startingNodeID}, which is a {deviceType} running {platform} to infect all the nodes it possibly could.')
            
# Creates a list to store all the edges.
edges = []
# Creates a dictionary to store all the nodes.
nodes = {}
      
# Set sensor, virus and speed to None   
sensor = None
virus = None
speed = None
                
# Runs when the 'run' button in pynode is clicked.
def run(): 
    global speed, sensor, virus # Imports the global variables speed, edges and nodes
    
    generateGraph() # Runs the function that generates the graph.

    speed = int(input('Please enter how many second you want 1 second to equal in the simulation: ')) # Gets user to import the speed

    # Run the block of code below infinitely
    while True:
        optionSelected = int(input('Enter [1] to deploy sensor, [2] to deploy virus: ')) # Gets user to select whether they want to deploy sensors or viruses
        if optionSelected == 1: # If 1 is selected
            register_click_listener(addSensor) # Deploy sensor to the node that is clicked on
        if optionSelected == 2: # If 2 is selected
            register_click_listener(tranverse) # Deploy virus to the node that is clicked on
    
    
begin_pynode(run) # Runs pynode.