# ReceiptsScanner
Python project using OCR to track expenses and receipts for budgeting and for personal use

Made by: Sebastian Kopec, Rehan Ayub, Richard Yang, and Shyam Hari

## Inspiration
Initially, our goal was to implement something using computer vision. Since finance was a central theme of this hackathon, we centered our ideation around that. After some thought, we realized that the process of keeping track of purchases through receipts physically was a tedious and unfavorable process. It was also noticed that receipts are the most detailed way to keep track of expenses as a credit statement does not specifically list the items you bought. This project is meant to be a way for people to track their expenses and categorically tell people the nature of expenses they make over a given time period. This would include categorizing groceries, restaurants, and clothing into categories of expenditure. 

## What it does
The manager uses an OCR API to recover the contents of a receipt and track the price per item, as well as the total price for the receipt. The receipt is then stored locally for the user with the data in a CSV file. The project has a simple front-end built with Flask for users to upload their receipts.  

## How We built it
The receipts are stored locally on the user's computer. We built it such that there we've integrated an OCR API that receives an image path from the user's local system and returns a JSON file with text. Using a keyword search and a parsing algorithm to determine the variance in JSON, item values and receipt total values are extracted from the image and the data is used to make a profile about the user. It was then optimized by using different OCR engines to extract the most data from input images. 

## Challenges We ran into
Oh, where to start. Firstly, the API we ended up using was poorly documented, and the only means of extracting syntax from the API was looking at other people's code, who had managed to figure it out. There are probably still functionalities from this API we are not sure about. Secondly, the next issue we encountered was a size limit on the file size that the API received. The maximum file size the API could receive was 1 Megabyte. Our solution for this was to implement a resizing algorithm in order to trim the image down to just under 1mb if it was over the limit. In the process of designing the backend database in Contentful a CMS, API documentation issues were prevalent. Sending a POST request to our database to create links for each of our images was difficult since there was no documentation outlining how to do that. To still maintain a PerContact Database, we pivoted our database to be stored on the users' local systems. Finally, while designing the front-end model for our program, we decided to build it in Flask. Due to our limited understanding of Flask, time was lost designing the proper architecture needed to make a seamless app.

## Accomplishments that we are proud of
To begin with, we are proud of the fact that we were able to build the full project out with the initial vision that we had for it. Since it was our first time using OCR technologies we believe our grasp and problem-solving abilities helped to tackle the challenges and our learning curve for it was far better than we imagined. When problems arose that seemed like they had no solution, we believe that our teamwork and collaboration in those situations definitely helped us move forward in the project and not just give up or stop trying. We were also very happy with the pair programming methodology that we employed when a person seemed like they did not have work to do. This definitely sped up the process of debugging and developing new features and the synergy between us was amazing.  

## What I learned
We think the most important thing we learned is the limitations of new technologies. For example, OCR is not perfect and so image quality was one of the greatest limiting factors we had. We think that the most important lesson we learned was to employ creative solutions to the limitations in the technologies that we were using, given our relatively limited knowledge of them. For the next hackathon or project that we work on, either individually or again in a group, one of the most important takeaways is having a set plan about the program's architecture before jumping in and starting to code. Once you jump in and find limitations that you're not aware of, its hard to just scrap whatever you have and start with something else. 

## What's next for My Receipt Manager
For the next stage of this project, we would like to refactor it in react-native so that we can have Android and iOS support due to the higher convenience and usability with mobile phones. We also want to implement more personalization with each account for example, Google Account Services. 
