# M3EOP-Rmarti20
Open Ended Project Module 3
Ryan Martin
Installations: Spotipy

Summary: So this program uses spotipy to go into my own spotify data to retieve my 
top tracks. These top tracks are then printed on a website. Spotipy's funtions are 
in python. So python is used to retirve the top tracks, then print them to the corresponding 
files. From the main program in python, webpage.php is called. webpage.php calles wrapped.c++
which iterates through the files and prints the html code to the website.

Bugs: No known bugs. Some more css could be added to the webpage to make it clearer, but thats it.

Citations: In main.py some of the code for the fucntions was borrowed or guided by https://jman4190.medium.com/build-your-own-spotify-wrapped-with-python-spotify-and-glide-apps-493dc7da20b <-- this website
Specifically guidence for the get_track_ids fucntion and the get_track_features function
Also the idea to use a dataframe was borrowed from the website 

Future Work: There is a lot I could add to this, mainly uploading more data to the site. Also making the site more detailed with some possible user interaction.

Grade:
There are three programing langauges used. C++, Python, and PHP
There are two non programming langauges used: html and css
Python calls the php file, which calls the c++ file to iterate through the files 
made from main.py, and prints to the website via html

The main program doesnt have much user iteraction, the one interaction is user validated.
Python was chosen for the main fucntion because spotify is coded in python. Php was used to 
produce the web page, c++ was used to iterate through the files and print to the web page.

The other programming languges (php and python) are implemented in ways that make sense, and are free of bugs. 40pts

The main prgram is complex but lacks user interaction as the priority was the website. 30pts

The other languages CSS and html are implemented well and in a way that makes sense 20pts

Information is passed via files for larger data sets 2pts

https://rmarti20.w3.uvm.edu/M3EOP-Rmarti20/webpage.php <----- My Wrapped Webpage Link 

