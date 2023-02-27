"""String Formatiing"""
myCode = 1117
myName = "Scaler"
myVar = 1234
myStr = "Variable is {2} and Code of {0} is {1}".format(myName, myCode, myVar)
print(myStr)
##################################################################
myCode = 1117
myName = "Scaler"
myStr = "Code of %s is %d" % (myName, myCode)
print(myStr)
##################################################################
myCode = 1117
myName = "Scaler"
myStr = f"Code of {myName} is {myCode}"
print(myStr)

############################################################
myCode = 1117
myName = "Scaler"
myStr = "Code of {} is {}".format(myName,myCode)
print(myStr)
#########################################
myCode = 1117
myName = "Scaler"
myVar=1234
myStr = "Code of {} is {}".format(myName,myCode,myVar)
print(myStr)
################################
myCode = 1117
myName = "Scaler"
myVar=1234
#myStr = "Code of {} is {}".format(myName)
#print(myStr)

############ defatult_arguments##############
myCode = 1117
myName = "Scaler"
myVar=1234
myStr = "Code of {} is {}".format(myName,myCode)
print(myStr)

############# Positional Arguments######################
myCode = 1117
myName = "Scaler"
myVar = 1234
myStr = "Variable is {2} and Code of {0} is {1}".format(myName, myCode, myVar)
print(myStr)
#############Keyword Arguments#########################
myCode = 1117
myName = "Scaler"
myVar = 1234
myStr = "Variable is {myVar} and Code of {myName} is {myCode}".format(myName='Rao', myCode='Text', myVar='Ramoji')
print(myStr)

#######################format _Numbner######################

myNum = -1234
myStr = "Number is: {}".format(myNum)
print(myStr)

