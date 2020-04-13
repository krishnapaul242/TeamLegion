# COVID 19 Monitor

Objective: It takes images of potential infectious place as inputs from the end-users and analyzes the
number of people in that image. It takes covid19 status data available in online COVID related APIs.
Using the status data and image inputs, the server would assess the risk of potential infection risk on a
scale of 0-10 based on the scale of activity(determined by the number of people in image) geographical
location and time. The app will show the analyzed data to end-users and take inputs for further
continuous assessment. The risk assessment data can also be accessed by a website and REST APIs.
Implementation: The app is simple and intuitive. It will have two screens, 1. Here users will see the risk
assessment data of their present geographical location( which they can also select manually). 2. The
users will click and upload pictures in real-time. Pictures from storage cannot be selected. The server
has the following modules - 1. Data Collecting Module - This will collect COVID status data from different
open sources. 2. Activity Determining Module - This will analyze the activity in input images on a scale
of 0-10. 3. Risk Determining Module- This will assess the risk of COVID infection on the basis of
geolocation, the scale of activity and time. 4. Server Module- This will handle the APIs for mobile app and
web apps.
Application: With sufficient data, 1. People can identify high-risk areas and choose to avoid them for
their safety. 2. Law enforcement agencies can use this to identify high-risk areas and decrease the scale
of activity. 3. It can be used to trace super spreaders and local infection. 4. It can visualize the risk
factor associated with places and help the lawmakers to determine the strategy and decisionmaking. 5.
It can give a new perception of the spread of covid19.

Machine Learning Code : https://drive.google.com/open?id=1bQAQSAJ3sMJ9YW63s-r-r0NSshNBKBHV
