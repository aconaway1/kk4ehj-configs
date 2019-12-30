#####
#
# This script takes the LinBQP template and generates a
#   working version.  It takes arguments from the command 
#   line and applies those values to a Jinja2 template.
#
#####
from jinja2 import Template
import sys

# Print the usage
def printusage():
	print("Usage: " + sys.argv[0] + " CALLSIGN SSID LOCATOR FREQUENCY CMSPASS LOCALPASS")
	print("  Where:")
	print("    CALLSIGN is your amateur radio call (duh!)")
	print("    SSID is your SSID (duh, again!)")
	print("    LOCATOR is your gridsquare")
	print("    FREQUENCY is your frequency in Hz (so 145MHz is 145000000)")
	print("    CMSPASS is your Winlink sysop password")
	print("    LOCALPASS is the local LinBPQ password")

# If you didn't give the right number of arguments
if len(sys.argv) < 7:
	print("Not the right number of arguments.")
	printusage()
	sys.exit()

comment = "LinBQP on RasPi"

# The template file to use
template_file = "./linbpq-template.py"
# The output file
output_file = "./linbpq-" + sys.argv[1].upper()
try:
	# Open the file
	file = open(template_file)
except:
	# Error out if you can't open the file
	print("Can't open the file " + template_file + ".")
	print("Make sure the file exists in the current directory.")
	sys.exit()

# Read the template into a variable
lines = file.read()
# Close the file
file.close()

# Create a new template object with the lines
t = Template(lines)
# Render the template
output = t.render(callsign=sys.argv[1].upper(),ssid=sys.argv[2],mapcomment=comment,locator=sys.argv[3].upper(),freq=sys.argv[4],cmspass=sys.argv[5],localpass=sys.argv[6])

try:
	# Open the output file
	outfile = open(output_file, "w")
	# Write the template
	outfile.write(output)
	# Close the output file
	outfile.close()
except:
	print("Couldn't write to " + output_file + ". Permissions?")
	sys.exit()

# Print what happened
print("Wrote to " + output_file + ". This is what you want to copy to bpq32.cfg")
