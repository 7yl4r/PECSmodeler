PECSmodeler
===========

A framework designed to aid in the implementation of PECS-style agent (based on the work of Bernd Schmidt et al.). This framework is designed to be theory-independent, extensible, and very easy to use. Please see the [wiki page](https://github.com/7yl4r/PECSmodeler/wiki) for additional documentation.

Installation & Setup
--------------------
Simply download and import the package to get started. For more hints take a look at the included example scripts.

Dependencies
-------------
* Python (v2.7 preferred, others may work)
* [PyLab](http://wiki.scipy.org/PyLab)

_Feature-dependent dependencies:_
* The horizonGraph plotter requires an install of the matplotlib add-on from [thomaskern/horizongraph_matplotlib](https://github.com/thomaskern/horizongraph_matplotlib).
* viewing informationFlow graphs using requires [graphViz](http://www.graphviz.org/). Simply install with "sudo apt-get graphviz".

_Included Packages (no work needed, these are just FYI)_
* [pydot](https://code.google.com/p/pydot/) for creating informationFlow graphs
* [ddeint](http://zulko.wordpress.com/2013/03/01/delay-differential-equations-easy-with-python/) for solving delay differential equations

Package Structure
-----------------
If you would like to add functions or data objects to the agent, it is best to keep them nested in their proper location in following package structure. Please try to refrain from changing the existing data objects and only add if absolutely necessary. If you are going to add a piece of information to one of the components, use the dataObject() class in __util/agentData.py. The idea here is to build up a complete data structure for behavior modeling and allow the functions associated with each piece of information to be swapped out easily.
		myScript.py (run any scripts or start python here)
		src/
			PECSagent/
				agent.py
				settings.py
				inputs/
					inputs.py
					(implementation packages here)
				state/
					state.py
					(implementation packages here)
				motive/
					motive.py
					(implementation packages here)
				output/
					output.py
					(implementation packages here)

Components
-----------
The agent model is split into the following components in an attempt to make flow of information through the agent more organized. Please see [the wiki page on information flow](https://github.com/PIELab/behaviorSim/wiki/information-flow) for more information, and consider the following descriptions of model components.
### Inputs ###
Inputs represent the context of the agent. This input comes from the environment exterior to the agent or from past actions of the agent.

### State ###
This component represents the internal state of the agent. All information here should be a property of the agent. These states are separated into the four componenents which give the PECS model its name: Physical, Emotional, Cognitive, and Social.

### Motive ###
The motives of an agent are analagous to the 'dependent variables' of the PECS reference model, and represent the motivations, drives, and intentions of the agent.

### Output ###
The output of the agent shows the agent's behavior as determined from motives, states, and inputs.

Adding to the Model
--------------------
The PECS model framework is designed to be extended to allow for the exploration of many behavior models. The following steps should be take to add to the model:
> 1. *Add your package to the applicable component.* 
> For instance, a new input definition, your package should be added to PECSagent/Inputs/. 
> 2. *Adjust component definition.* 
> The contents of the default component definition should be adjusted to use your new package or to add your new variables. For example: if you intend to add a new state variable, you must add the variable to PECSagent/state/state.py. If you are just changing the way an existing state variable is calculated, you can just change the import statement at the top of the file or load your custom function in a script.
>*NOTE*: only add to the component definitions; never remove variables. Ideally, your package can use existing variables but all state variables are not yet incorporated. Please add variables with caution and use descriptive names to enable re-use by other packages.
