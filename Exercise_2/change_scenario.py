'''
This file is intended for the manipulation of scenario files for Vadere
In the current version one pedestrian is placed at 
'''
import json
import re
##TODO: some code to get name of inputfile from commandline

##optional: some code to get position of the new pedestrian from commandline

##optional: some code to handle multiple pedestrians

#inputfile = ".\vadere.v1.0.windows\Exercise_2\scenarios\rimea_06_corner_copy.scenario"
inputfile = "rimea_06_corner_copy.scenario"
with open(inputfile) as json_file:
	data = json.load(json_file)
	pedestrian = {"source" : None, "targetIds" : [ ], "position" : {"x" : 5.7, "y" : 2.2}, "velocity" : {"x" : 0.0, "y" : 0.0}, "nextTargetListIndex" : 0, "freeFlowSpeed" : 1.420734624122518, "attributes" : {"id" : -1, "radius" : 0.195, "densityDependentSpeed" : False, "speedDistributionMean" : 1.34, "speedDistributionStandardDeviation" : 0.26, "minimumSpeed" : 0.5, "maximumSpeed" : 2.2, "acceleration" : 2.0}, "idAsTarget" : -1, "modelPedestrianMap" : { }, "isChild" : False, "isLikelyInjured" : False, "groupIds" : [ ], "trajectory" : {"footSteps" : [ ]}, "type" : "PEDESTRIAN", "groupSizes" : [ ]}#more features like in figure 4 of exercise 2?
	#reach scenario -> topography -> dynamicElements and append pedestrian
	data['scenario']['topography']['dynamicElements'].append(pedestrian)
	#change position of appended pedestrian
	x = 12
	y = 2
	data['scenario']['topography']['dynamicElements'][-1]['position'] = {"x" : x, "y" : y}
	#set targetIds
	targetId = 1
	data['scenario']['topography']['dynamicElements'][-1]['targetIds'] = [targetId]
	#set own id for tracking
	##optional: if position is not hard coded in pedstr but stored in an array or passed via command line
	#create filename without ending
	name = re.sub(r'\..*$', "", inputfile) + '_modified'
	#change document name in json field name
	data['name'] = name
	#append ending to filename
	outputfile = name + '.scenario'
	with open(outputfile, 'w') as outfile:
		json.dump(data, outfile, indent=2)