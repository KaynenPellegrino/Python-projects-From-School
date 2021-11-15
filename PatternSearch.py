import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#Place all the code from the previous steps here

regex="[^a-zA-Z\d]" #this Regex(regular expression) Variable is asking to count every character in
#the string except letters and numbers, the ^ symbol in the brackets excludes characters inside the
#brackets from being counted. \d is the character for digits. it can also be written as (A-Za-z0-9)

result=re.findall(regex, lorem_ipsum)

print(len(result))

regex="sit[-:]amet"

#this is the outcome assigned to a variable like requested.

occurences_sit_amet = re.findall(regex,lorem_ipsum)

#this is the output to the console, the number of sit-amet occurences.

print(len(occurences_sit_amet))

#Replace sit:amet and sit-amet with sit amet using the sub funciton
#Assign the outcome to a variable named 'replace_results'

regex="sit[-:]amet"

#Using the findall function, get all of the instances of 'sit amet' in the string assigned to 'replace_results'

replace_results=re.sub(regex,"sit amet",lorem_ipsum)

#Assign the outcome to a variable named 'occurrance_sit_amet'

occurrence_sit_amet=re.findall(regex,lorem_ipsum)

#Output to the console, the number of sit amet occurrances.  Hint:  use the len function

print(len(occurrence_sit_amet))