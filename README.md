# ![target (8)](https://user-images.githubusercontent.com/119602009/224983565-4dcba114-8cf2-4ddf-8f36-4c239df2bb0f.svg) Staid

The Final Project of CS50x, where my task was to create a study helper, named Staid. This repository will be updated periodically as I continue to complete the project. This README will be updated properly once the project is completed. This READ.ME is a WIP & not the final version. I will also be creating a live version for this Web App hosted on either Heroku or pythonanywhere.

## Demo


https://user-images.githubusercontent.com/119602009/225231680-a2b15c1c-0d12-45ef-aee6-498e5f5e5e97.mp4
Above is video showing the Web App & the usage of each feature. Each feature is explained greater in depth below. This was taken using a development server to show the functionality of Staid. Apologies for the poor quality, I will be updating with a better quality video soon.

## Features

### Timer
The Timer is a countdown timer for users to time their study sessions. There are two input fields. The first being the duration of the study session, with the format of hours, minutes & seconds. The second is the name of this session if the user wishes to log this session. If the user wishes to log the session, the session is automatically added to their Logbook without any action required from the user. The length of this session is the duration the user had inputted and the date logged is the date of when the timer was used for this session.
Once the timer reaches the final ten seconds, the color of the timer changes from blue to yellow. At the end, the timer changes from yellow to red.

The accent color for this feature is Blue (Hex Code: '#44A1F1') as it is known to have a calming effect, increasing focus and productivity during a timed session.
 
### Logbook
The Logbook is a log of all the user's study sessions. There are two sections. The first is for the user to add a session to the Logbook directly with three input fields, the name of the session, the duration of the session & the date of the session they wish to add. The second is the Logbook itself, in the form of a table. The columns, from left to right, are the index of the row, the name of the session, the duration of the session & the date of the session. The records of the Logbook is ordered in a reversed chronological order, with the earliest session at the top of the table. This is so to remind the user of their immediate previous session so that they can plan their next sessions more effectively.

The accent color for this feature is Yellow (Hex Code: '#FFBB44') as it is known to improve optimism and analytical skills. This increases the user's ability to analyse their sessions to improve their productivity. 

### Study Locations Near You (Near Me)
The Study Locations Near You shows the user the closest study locations near them. There are two input fields. The first is for the user to enter their own geographical data and the second is the map itself. The user's location data is grabbed using Geo IPify's API & this data is used to generate the Map using OpenStreetMap without the user having to enter any data. If the user wishes to search another location or to improve the accuracy of the location data used to generate the map, the user can input their latitude and longitude in the input fields. This data is then used to generate a new map which is then shown to the user. 

I originally planned to use the Google Maps API, however, I did not as it is not open-source and incurs a cost after the credit provided is exceeded.

The accent color for this Green (Hex Code: '#00A266') as it is known to give a sense of the outdoors and reduce anxiety, matching the sense of studying somewhere new.

## My Thoughts

## Credits

## Getting Started

## WORK IN PROGRESS
