# Automate-Notes

This Web Scraper is for <strong>Competitive Programmers</strong> who wants to participate in all the upcoming contests, but aren't
able to keep track of those contests. Therefore, this Web Scraper tells you which contests will be held in the
next two days (you could set this range).

---------------------------------------------------------------------------------------------------------------------------

# Setting up

1) Create a notes.txt (you could name it anything) and copy its absolute path.
2) Go into AutomateNote.py, you will find a variable named <strong>PATH</strong> and paste the copied path there.
3) Now, got into "Sticky Notes/sticky-notes.py", there you will find a variable named <strong>self.PATH</strong> and 
   again paste the copied path there. (OPTIONAL)
   
In AutomateNote.py, you will find a variable named <strong>TARGET_SITES</strong>, the Scrapper will only tell you
about the contests which are hosted on this sites. So, edit it according to your preferences.

Lastly, set AutomateNote.py to run on startup using Task Schedular in windows or you could write your own shell script for it.
So, now whenever you start your laptop, notes.txt will automatically get updated.

<strong>sticky-notes.py: This is just a simple Notepad GUI App, which tells you the contents of notes.txt and also allows you to edit 
notes.txt directly.</strong> 

# Dependencies
  1) bs4 (beautifulSoup)
  2) PyQt5 (optional)
  
-----------------------------------------------------------------------------------------------------------------------------

# Resource
  <a href="https://clist.by/">clist.by</a>