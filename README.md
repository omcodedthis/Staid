# ![target (8)](https://user-images.githubusercontent.com/119602009/224983565-4dcba114-8cf2-4ddf-8f36-4c239df2bb0f.svg) Staid

Staid is a study helper that complements the learning process for students. The name was formed by joining the words study and aid, encapsulating the meaning within. The logo is a target, representing the aim of Staid which is to help students to achieve their targets. It comes with 3 main features, the Timer, the Logbook and Study Locations Near Me (Near Me) which are explained in greater detail below. This README will be updated properly once the project is completed. 

This READ.ME is a WIP & not the final version. I will also be creating a live version for this Web App hosted on either Heroku or pythonanywhere.

## Demo

https://user-images.githubusercontent.com/119602009/226168818-e40fbeba-37d4-40c5-b68a-0091d3a3226f.mp4

Above is video showing the Web App & the usage of each feature. Each feature is explained greater in depth below. Do note that the video is sped up to meet GitHub's file limits.

## Features
<details>
<summary>Timer</summary>

![timer-gif](https://user-images.githubusercontent.com/119602009/226172679-6dc07429-0eb1-48ca-b7f8-07aa1b71f02a.gif)

The Timer is a countdown timer for users to time their study sessions. There are two input fields. The first being for the duration of the study session, in the format of hours, minutes and seconds. The second is the name of the session if the user wishes to add it to their Logbook. 

If the user wishes to log the session, the session is automatically added to their Logbook without any action required from the user. The length of this session is the duration the user had inputted and the date logged is the date of when the timer was used for this session.

Once the timer reaches the final ten seconds, the color of the Timer changes from blue to yellow. At the end, the Timer changes from yellow to red.

The accent color for this feature is blue (Hex Code: `#44A1F1`) as it is known to have a calming effect, increasing focus and productivity during a timed session.
</details>


<details>
<summary>Logbook</summary>

![logbook-gif](https://user-images.githubusercontent.com/119602009/226172690-da786437-ba8b-4f14-9f14-2f3f39780dfc.gif)

The Logbook is a log of all the user's study sessions. There are two sections. The first is for the user to add a session to the Logbook directly with three input fields, the name of the session, the duration of the session & the date of the session they wish to add. The second is the Logbook itself, in the form of a table. The columns, from left to right, are the index of the row, the name of the session, the duration of the session & the date of the session. The records of the Logbook is ordered in a reversed chronological order, with the earliest session at the top of the table. This is so to remind the user of their immediate previous session so that they can plan their next sessions more effectively.

The accent color for this feature is yellow (Hex Code: `#FFBB44`) as it is known to improve optimism and analytical skills. This increases the user's ability to analyse their sessions to improve their productivity. 
</details>

<details>
<summary>Study Locations Near You (Near Me)</summary>

The Study Locations Near You shows the user their closest study locations. There are two input fields. The user's location data is grabbed using Geo IPify's API and this data is used to generate the Map using OpenStreetMap without the user having to enter any data into the input fields. If the user wishes to search for another location or to improve the accuracy of the location data used to generate the map, the user can input their latitude and longitude in the input fields. OpenStreetMap mainly works with latitude and longitude coordinates only. This data is used to generate a new map of the inputted location which is then shown to the user.

I had originally planned to use the Google Maps API, however, I did not as it is not open-source and incurs a cost after the credit provided is exceeded.

The accent color for this green (Hex Code: `#00A266`) as it is known to give a sense of the outdoors and reduce anxiety, matching the sense of studying somewhere new.
</details>

<details>
<summary>About Page</summary>

The About page has a description of what Staid is and what it aims to achieve. The "Credits" section acknowledges the additional technologies used to create Staid.
</details>

<details>
<summary>Persistent Light/Dark Mode</summary>

![mode-gif](https://user-images.githubusercontent.com/119602009/226172785-d6745b75-247b-4757-98f1-086904117609.gif)

The toggle button in the header is a Light/Dark mode toggle for the Web App. By default, Dark Mode is selected. If the user wishes to enable Light Mode, the toggle button's color changes to white and it appears as toggled throughout, with the Light Mode persisting for the user automatically. If the user wishes to change back to Dark Mode, the user can do so, with the toggle being set back to its default state with the Dark Mode persisting throughout. 
</details>


## Credits

## Getting Started

## My Thoughts

Staid was a great learning opportunity. It allowed to me to hone my programming skills as well as taught me the importance of considering the user in my projects to build a better experience.

Through this project, I learnt an important skill in programming, the ability to search for relevant information and documentation of various libraries to implement features into my Web App.

I also got a taste of designing from an aesthetic standpoint. Looking for colors that look good in both Light/Dark Modes without causing eye strain, ensuring that each feature's color and icon was used as an accent effectively in their respective pages and spacing the contents apart evenly to make it more appealing for the user.

## WORK IN PROGRESS
