# Web-scrapping

In today’s competitive world everybody is looking for ways to innovate and make use of new technologies. Web scraping (also called web data extraction or data scraping) provides a solution for those who want to get access to structured web data in an automated fashion. Web scraping is useful if the public website you want to get data from doesn’t have an API, or it does but provides only limited access to the data.
Artificial Intelligence (AI) and Machine Learning (ML) are already being leveraged for increased efficiency and greater success in public web data-gathering operations
The web scraping process:
1.	Identify the target website
2.	Collect URLs of the pages where you want to extract data from
3.	Make a request to these URLs to get the HTML of the page
4.	Use locators to find the data in the HTML
5.	Save the data in CSV file or some other structured format
Step 1 : Install and Import libraries
Step 2 : Inspect the web page and scrape HTML content from web page
Now let’s inspect the web page first that we’re going to scrape. Go to naukri.com and search for “Python”.
The data fields I am interested in are “Title”, “Company Name”, “Ratings”, “Reviews”,and “URL” to apply for the job. We’ll create an empty dataframe to store these fields first.
df = pd.DataFrame(columns=[‘Title’,‘Company’,‘Ratings’,‘Reviews’,‘URL’])
