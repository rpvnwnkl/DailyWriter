#What this is:

__I need a tool which will automatically login, write, and submit my daily words for me when I cannot.__

##How:

1. Load login page
2. Enter login credentials
3. Submit credentials 
4. Load writing page
5. Select form for text entry
6. Enter at least 750 words of text
7. Submit filled form

##Methods:

* From what I have gathered the load page and login will be able to be completed using a combination of Mechanize and [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/), both libraries which will be new to me. [PSF Mechanize Page](https://pypi.python.org/pypi/mechanize/); [3rd Party Mechanize Docs](joesourcecode.com/Documentation/mechanize0.2.5/); The [Mechanize Sourceforge Site](http://wwwsearch.sourceforge.net/mechanize/) is down right now. 

* Entering the text should be a simple implementation of loading a string into the form field, using Mechanize. 

* Eventually it would be interesting to use a neural network script to generate the words for the text field

* The site seems to auto save but to be sure we will use Mechanize to click stats link page

* If there is some way to verify the words have been accepted then we will try to do that too

###Word Generation:

See this website for RNN resources: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
And for the basics of Neural Networks in Python: http://iamtrask.github.io/2015/07/12/basic-python-network/

###Relevant Stack Overflow questions:
* http://stackoverflow.com/questions/2050705/python-fill-out-a-form-and-confirm-with-a-button-click
* http://stackoverflow.com/questions/1170120/web-scraping-to-fill-out-and-retrieve-search-forms 
