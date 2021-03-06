from ....__util.attitude import attitude

import traceback	# for printing traceback on program abort

# returns a constant attitude as defined in __util.attitude  with constant value (assumed 1 if none given)
	# time-invariant? = TRUE
	# (sim)time-dependent? = FALSE
# requirements for this method to be valid:
	# requiredTimeScale = null
	# requiredTimeStep  = null
def constAttitude(data, t, value=1):
	if t < len(data):
		return data[t]
	else:
		a = attitude()
		a.behavioralBelief = value
		a.behaviorAttitude = value
		a.normativeBelief  = value
		a.subjectiveNorm   = value
		a.PBC              = value
		a.controlBelief    = value

		if len(data) == 0:
			data.append(a)
		for i in range(len(data),t+1):
			data.append(a)
		return data[t]

# returns an attitude with constant given values in all inventories except for that specified by steppedName;
# the specified inventory is given value 'beforeStep' prior to 'stepTime' and 'afterStep' post 'stepTime'
	# value    = constant value assigned to all inventories except for that specified by 'steppedName'
	# steppedName = (string) name of inventory stepped
	# stepTime = (int) time of step (units specified by settings)
	# beforeStep = value of <steppedName> prior to <stepTime>
	# afterStep  = value of <steppedName> after <stepTime>
def stepOne(t,value,steppedName,stepTime,beforeStep,afterStep):
	a = attitude()
	# set all to value
	a.behavioralBelief = value
	a.behaviorAttitude = value
	a.normativeBelief  = value
	a.subjectiveNorm   = value
	a.PBC              = value
	a.controlBelief    = value

	if t > stepTime:
		vvv = afterStep
	else:
		vvv = beforeStep
	# find & overwrite the steppedValue
	if   steppedName=='behavioralBelief':
		a.behavioralBelief = vvv
	elif steppedName=='behaviorAttitude':
		a.behaviorAttitude = vvv
	elif steppedName=='normativeBelief':
		a.normativeBelief  = vvv
	elif steppedName=='subjectiveNorm':
		a.subjectiveNorm   = vvv
	elif steppedName=='PBC':
		a.PBC              = vvv
	elif steppedName=='controlBelief':
		a.controlBelief    = vvv
	else:
		print 'ERR: unrecoginzed inventory "'+str(steppedName)+'" for theory of planned behavior given to stepOne(). Check your steppedName string. Aborting program from /PECSagent/inputs/CSEL/attitudes.'
		print '>>> traceback <<<'
 		traceback.print_exc()
		exit()

	return a
