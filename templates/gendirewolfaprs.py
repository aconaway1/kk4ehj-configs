#####
#
# This script takes the Direwolf APRS beacon template and generates a
#   working version.  It takes arguments from the command line and applies
#   those values to a Jinja2 template.
#
#####
from jinja2 import Template
import sys

# Print the usage
def printusage():
	print("Usage: " + sys.argv[0] + " CALLSIGN LATITUDE LONGITUDE")
	print("  Where:")
	print("    CALLSIGN is your amateur radio call (duh!)")
	print("    LATITUDE and LONGITUDE are like XX^YY.ZZN or AAA^BB.CCW")

# If you didn't give the right number of arguments
if len(sys.argv) < 4:
	print("Not the right number of arguments.")
	printusage()
	sys.exit()

if len(sys.argv) == 5:
	comment = sys.argv[4]
else:
	comment = "Raspberry Pi Beacon"

# The template file to use
template_file = "./direwolf-aprsbeacon-template.py"
# The output file
output_file = "./direwolf-aprsbeacon-" + sys.argv[1].upper()
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
output = t.render(callsign=sys.argv[1].upper(),lat=sys.argv[2],long=sys.argv[3], comment=comment)

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
print("Wrote to " + output_file + ". This is what you want to copy to ")
print("  /etc/direwolf.conf")
