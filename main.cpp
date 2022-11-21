#include <iostream>
#include <string>
#include <fstream>
using namespace std;
const string python = "python";
int main(int argc, char *argv[]){
    string input;
    string command;
    //ask user if they would like to see their spotify wrapped
    cout << "Do you want to see your spotify wrapped? Y/N" << endl;
    cin>>input;
    
    //if yes run top tracks.py
    if (input == "Y" || input == "y" || input == "yes" || input == "Yes" || input == "YES" || input == "YEs" || input == "Ye" || input == "ye" || input == "yep"){
        command = python + " ../TopTracks.py ";
        system(command.c_str());
    }
    //if no close program

    return 0;
}