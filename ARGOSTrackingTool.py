#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Sophia Bryson (sab159@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

# Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

# Create a file object from the file
file_object = open(file_name, 'r') #read only

# Read contents of data file into a list
line_list = file_object.readlines()

# Close the file (it's saved into the list)
file_object.close()

# Iterate through all lines in the linelist
for lineString in line_list: #inserts value of first line into variable 'lineString'
    
    # if lineString[0] == "#" or lineString[0] == "u": continue #skips lines that are commented (header)
    if lineString[0] in ("#", "u"): continue #same as above, but using membership rules
    
    # now pull out specific items from that string - split into data items
    lineData = lineString.split() #creates list object with 18 items
    
    #then can use indices to access desired items from each row - extract items into variables
    # records (columns) of interest: UID, date, location class (quality), lat & long
    record_id = lineData[0] #record ID
    obs_date = lineData[2]  #date of observation
    obs_lc = lineData[4]    #observation location class (quality marker)
    obs_lat = lineData[6]   #observed latitude
    obs_long = lineData[7]  #observed longitude

    #print location of Sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, long:{obs_long} on {obs_date}")






