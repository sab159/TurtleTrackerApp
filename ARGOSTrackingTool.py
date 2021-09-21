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

# first: simply copy and paste one line of data from sara.txt data file (as if we read from data)
lineString = '20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'

# now pull out specific items from that string - split into data items
# records (columns) of interest: UID, date, location class (quality), lat & long
# need string method to pull specific characters from string. Treat as delim.
lineData = lineString.split() #creates list object with 18 items

#then can use indices to access desired items from each row - extract items into variables
record_id = lineData[0] #record ID
obs_date = lineData[2]  #date of observation
obs_lc = lineData[4]    #observation location class (quality marker)
obs_lat = lineData[6]   #observed latitude
obs_long = lineData[7]  #observed longitude

#print location of Sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, long:{obs_long} on {obs_date}")


# bring data into code from sara.txt




