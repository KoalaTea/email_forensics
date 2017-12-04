import re

# global dictionaries
valid_email_headers = {} # Dictionary of all registered headers and their regex format
headers = {} # Dictionary of all headers/values in email
badheaders = {} # unused for now

def readHeaders():
	with open("/root/Desktop/headers") as f: #file of registered headers with IANA
		content = []
		content = f.readlines()
		content = [item.strip() for item in content]
		for line in content:
			fields = line.split(" ")
			header = fields[0] # header
			if (len(fields) == 2): # check to see if there is a regex
				regex = fields[1] # regex if exists
				valid_email_headers[header] = regex # add regex to value of Dictionary
			else:
				valid_email_headers[header] = "" # no regex available
	return


# function to check if the value of a header matches the correct fomat
# params - header - the header to be checked
#	 - value  - the value to be checked
# returns - true if valid value or false if invalid format
def checkValue(header,value):
	if (valid_email_headers[header] == ""): # is there a regex to be checked against
		return true # valid value
	pattern = re.compile(valid_email_headers[header]) # regex pattern
	print(valid_email_headers[header])
	return re.match(pattern,value) # check if value matches regex

def emailAnalysis():
	print("Input email header file.\n")	
	filename = input()
	with open(filename) as f:
		content = []    
		newlist = []                                                  
		content = f.readlines() 
		last = "" # create variable for last element
		for item in content:
			if item[0] == " ": # checks for multi lined headers
				last = last.strip() + item # adds the multi line headers to one line
			else:
				newlist.append(last)
				last = item

		newlist.append(last)

		for line in newlist:  
			if ('------=') in line: # break out once you hit the email contents and are done with email headers
				break
			elif ":" not in line: # don't add lines to the header doct without a :, all headers are [HEADER}: [VALUE]
				continue
			else:
				fields = line.split(':',1) # split on the first : in each line         
				header = fields[0] # header value          
				value = fields[1] # value                                                                      #	
				if header not in valid_email_headers.keys(): # is the header registered with IANA
					print("Found header not registered with IANA:", header) # it is not
				else:
					if not (checkValue(header,value)): # is the value correctly formatted
						print("Valid header but invalid formatted value:", header,":",value) # it is not
				headers[header] = value # add header/value to dictionary
				
def main():
	readHeaders()
	emailAnalysis()
	
main()
