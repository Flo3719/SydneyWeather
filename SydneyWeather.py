import requests
from bs4 import BeautifulSoup
import pprint

# Copyright Florian Fahrenholz

#BEAUTIFUL SOUP

#Setup:
page = requests.get("http://www.bom.gov.au/nsw/forecasts/sydney.shtml")
soup = BeautifulSoup(page.content, "html.parser")


#temperature:
maxtempitems = soup.find_all(class_="max")
maxtemptexts = [item.get_text() for item in maxtempitems]

#Days:
Weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Find the Name of Todays Day Paragraph
contentDiv = soup.find(id="content")
Today = list(contentDiv.children)[4]
TodayP = list(Today.children)[1]
TodayPText = TodayP.get_text()

#Extract the Name of Today from the sentence "For the rest of Friday" -> "Friday"
TodayPTextWords = TodayPText.split(' ')
TodaysDay = TodayPTextWords[-1]

#Get the number of Todays Day (Monday = 0, ...)
for Day in range(0, len(Weekdays)):
	if Weekdays[Day] == TodaysDay:
		TodaysDayNr = Day

#Function to change Weekdays String order to make todays days name the first day in the string. 
def shift_left(lst, distance):
	output = lst
	for i in range(0, distance):			    
		output = output[1:] + [output[0]]  
	return output        

# Save the reordered Weekdays string to this var
WeekdaysArranged = shift_left(Weekdays, TodaysDayNr)


# Summary:
# A short desription of the weather (eg: sunny, cloudy)
summaryitems = soup.find_all(class_="summary")
summarytexts = [item.get_text() for item in summaryitems]

# output:
Forecast = []
for i in range(0, 7):
	Forecast.append({
		"DayName": WeekdaysArranged[i],
		"DayMaxTemp": maxtemptexts[i],
		"DaySummary": summarytexts[i]
	})	

print("The weather in Sydney for the next 7 days:")
pprint.pprint(Forecast)






