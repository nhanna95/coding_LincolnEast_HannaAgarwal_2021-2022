# coding_LincolnEast_HannaAgarwal_2021-2022

# ADVENTOUR

# Description

This project was made for the Nebraska FBLA SLC 2021-2022 Coding and Programming event. 
The main purpose of the program is to provide the user with possible places to visit based on six criteria: city, state, cost, type, indoor/outdoor, rating (based on Google Reviews)
Based on the user's input, we will recommend as many locations as possible and will include necessary information about each. User don't have to input all criteria, but have the option to

We used the library tkinter for the app window
We used the programming language Python for our code and developed it in VSCode

Some challenges we faced were:

  1. How to input the attractions into a list, 
  2. Search through the list if the user didn't input all the info, 
  3. Show the cities within each of the states based on the original user input of state, 
  4. How to show images as URLs,
  5. Fixing lots of bugs with the about page
  
Features we hope to implement in the future:

  1. Add a map feature,
  2. Add the about feature back to the Mac part,
  3. Add a description and latitude marking to each attraction
  
# Installation Instructions

## Windows

  1. Click on the Green Code Button on the top right of the repository and choose Download Zip
  2. Open file and extract all
  3. Open new folder in the command line by either alt clicking on folder and clicking "Open in Windows Terminal" or by first opening the terminal and type path name to downloaded folder
  4. Run `pip install -r requirementsWin.txt`
  5. Lastly run `python adventour.py`

## Mac OS
  
  1. Click on the Green Code Button on the top right of the repository and choose Download Zip
  2. Open file and extract
  3. Make sure your Mac is in light mode, otherwise the window will have dark blobs blocking the display
  3. In your terminal, run `pip install -r requirementsMac.txt`
  4. Open the mainMac.py file
  5. Lastly run the mainMac.py file
 
# Usage Instructions

  1. Enter your desired criteria. The top dropdown decides the state, the second dropdown decides the city, and the third dropdown decides the top of attraction.  
     The check mark indicates whether the attraction is indoor (checked) or outdoors (unchecked). The next slider is the maximum price and the bottommost slider is      the minimum rating. Once finished entered, click the search button.
  2. Use the back and next button to toggle through the attractions. At the bottom of the screen, you can see how many attractions match your criteria.
  3. Enjoy the attraction you choose!

# Credits

This program was written by Nixon Hanna (nhanna95) and Shrey Agarwal (ShreyAgarwal310). Our FBLA advisor is Lori Anderson-Stowe. Bhushit Agarwal helped us fix bugs and gave us the ideas for PyInstaller and how to use images. Darian Kauk designed the Adventour logo.

# License

MIT License

Copyright (c) 2021 Nixon Hanna, Shrey Agarwal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
