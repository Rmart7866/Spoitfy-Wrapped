#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std;


int main() {
    ifstream fileIn;
    string header;
    string songTitle;
    string band;
    string album;
    string num;
    vector<string> vec;
    //create vector of files of the top songs 
     vec.push_back("test.csv"); vec.push_back("test2.csv"); vec.push_back("test3.csv"); 
     //prints html code for the websiste 
     cout << "<table>\n<tr><th>" << "Your Top Songs" << "</th></tr>" << endl;
    //iterates trough the vector of files, prints all the information on each line on the website 
    for (int i = 0; i <= 2; i++){
        fileIn.open(vec[i]);
        //takes the dataframes header line
        if (fileIn) {
            getline(fileIn, header);
        }
        //checks which file it is, test.csv is the top songs within the past few weeks 
        if (vec[i] == "test.csv"){
            cout << "<tr><td>" << "Top Songs Past Few Weeks " << "</td></tr>" << endl;  
        }
        //test2 is teh top songs the past few months 
        if (vec[i] == "test2.csv"){
            cout << "<tr><td>" << "Top Songs Past Few Months " << "</td></tr>" << endl;  
        }
        //test3 is the top songs within the past few years 
        if (vec[i] == "test3.csv"){
            cout << "<tr><td>" << "Top Songs Past Few Years " << "</td></tr>" << endl;  
        }
        //prints the songs name, artists, and album 
        while (fileIn && fileIn.peek() != EOF){
            getline(fileIn, num, '^');
            getline(fileIn, songTitle ,'^');
            getline(fileIn, album, '^');
            getline(fileIn, band, '\n');
            cout << "<tr><td>" << songTitle << "</td><td>" << band << "</td><td>" << album <<  "</td></tr>" << endl;  
        }
        //closes file 
        fileIn.close();
        
    }
    //all this data is in a table 
    cout <<  "</table> \n "<< endl;
    return 0;
}
