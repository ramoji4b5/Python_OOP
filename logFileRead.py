file_in = open('in/logfile.txt','r') # Read file
for line in file_in: # Loop every line
    if 'ERROR' in line: # Search for ERROR in line
        print(line) # Print line
    elif 'INFO' not in line and 'WARN' not in line: # Remove INFO and WARN lines
        print(line) # Print line