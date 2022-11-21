Ryan Martin
Installations: Spotipy must be downlaoded in order to run this program

Summary: So this program uses spotipy to go into my own spotify data to retieve my 
top tracks. These top tracks are then printed on a website. Spotipy's funtions are 
in python. So python is used to retirve the top tracks, then print them to the corresponding 
files. From the main program in python, webpage.php is called. webpage.php calles wrapped.c++
which iterates through the files and prints the html code to the website.

The langauges used here include python, c++, and php.

The website is built using css and html.

The pyhton code uses Spotipy to pull my top tracks and get the correct IDs for them. It then 
puts all the information (artist name, song title, and album) in a dataframe whcih organizes all 
the data. The data is split into three groups. Most recent top tracks (past month), pas few months, 
and past few years. This information is then displayed on the website using a mix of php and c++, with html and css for styling. 



Bugs: No known bugs. Some more css could be added to the webpage to make it clearer, but thats it.

Citations: In main.py some of the code for the fucntions was borrowed or guided by https://jman4190.medium.com/build-your-own-spotify-wrapped-with-python-spotify-and-glide-apps-493dc7da20b <-- this website
Specifically guidence for the get_track_ids fucntion and the get_track_features function
Also the idea to use a dataframe was borrowed from the website 

Future Work: There is a lot I could add to this, mainly uploading more data to the site. Also making the site more detailed with some possible user interaction.



https://rmarti20.w3.uvm.edu/M3EOP-Rmarti20/webpage.php <----- My Wrapped Webpage Link 

