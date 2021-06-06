# Web_Scraper

This Repository is a collection of some of my webscraper scripts for several projects.

### Current List: 
  1. WGgesucht Scraper
  2. Gymshark Availability Checker



### 1.WGgesucht Scraper

This Scraper is used to create a DataFrame of the frontpage overview for a city. It Scrapes the tiles and adds them. 
Because of DoS Protection there is artificial time added between each page request.
Because of the different content types for a tile. This scraper can only read tiles for WGs and not appartments. <br>
https://www.wg-gesucht.de/wg-zimmer-in-Munster.91.0.1.1.html?category=0&city_id=91&rent_type=0&img=1&rent_types%5B0%5D=0 <br> <br>
To use this script you need to adjust the link in the script because the website iterates over the last integer before .html
For automated use I recommend WindowsTaskSceduler or CronJobs with the prefered time Intervall. <br>
https://www.jcchouinard.com/python-automation-using-task-scheduler/
<br>

Depending on the time of the year I recommend not to scrape everyday because of the limited amount of new ads. 
Before the beginning of a semester you could run the script more often. 
<br>
The goal of this script is to analyze city data of one city in particular. 
For me I want to know about the prices in Berlin as I am currently on search for a new flat.


### 2. Gymshark Availability Checker

Shoutout to my friend Marek that needed new trackpants. 
This scraper is dedicated to checking availability of a certain article of the Gymshark page.
The reason this Script was needed is because of the lacking of an email notification system. <br>
To use this script once you need to put in the link and needed size of the article. 
<br>
This Script uses Selenium because of the dynamic elements of the page that need to load before you can check for the given article and it's size.
Because this script uses selenium you should be aware of the chosen browser to open the website.
<br>
For automated use I recommend WindowsTaskSceduler or CronJobs with the prefered time Intervall.
https://www.jcchouinard.com/python-automation-using-task-scheduler/


