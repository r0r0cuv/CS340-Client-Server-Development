
# CS 340 Client/Server Development portfolio project featuring an interactive animal rescue dashboard built with Python, MongoDB, and Dash. Includes CRUD operations, data filtering, interactive charts, and mapping for Grazioso Salvare.

Rosalie Reblora
Southern New Hampshire University
CS 340 – Client/Server Development

Project Overview

I created a dashboard for Grazioso Salvare in Python. Using MongoDB and Dash I was able to create an application that will allow Grazioso to search for animals at the animal shelter that may fit there search and rescue needs. The dashboard will allow users to search for records that may have been trained for Water Rescue, Mountain or Wilderness Rescue, Disaster or Individual Tracking. The dashboard will also display an interactive table of data and pie chart of breeds. A map that displays where the animals are located. 

## Reflection  

### How do you write programs that are maintainable, readable, and adaptable? 

By breaking down your code into smaller pieces and giving your variables/functions good names you can write programs that are readable. Another way to keep your code readable is by separating your functions out into different files. In my first project I created a python file that had CRUD functions for my mongoDB database. I was able to take that CRUD file and use it in my second project. 

This helped my dashboard be maintainable because my CRUD functions are separated from my dashboard code. If I needed to change my connection to my database I only would have to edit my CRUD python file. I could also use my CRUD file for another project that I may build in the future that deals with animal shelters. 

### How do you approach a problem as a computer scientist? 

I break down the problem and figure out what steps I need to take to complete the problem. Then I test each piece of code and see if they all work together. With my project for Grazioso Salvare I took their search and rescue criteria and figured out what information I would need from my database. I then wrote queries that I could plug into my dashboard to filter my results. 

I feel like my past programming assignments were more about writing one program or algorithm. I had to figure out how to take all these technologies and put them together to create my final product. When working on future projects I will break things down into smaller pieces and make sure I am querying my database properly. 

### What do computer scientists do, and why does it matter? 

Computer scientists help build and fix programs.  They can also find ways to improve the programs they create. By using their skills they can help people become more efficient. 

With my project I was able to create something that will help Grazioso Salvare become more efficient with their data. They will be able to use my dashboard to search through dogs that may qualify for their search and rescue program. Computer science can be used to help others in many different ways. 

## Project Artifacts  

- `ProjectTwoDashboard.ipynb`  
- `CRUD_Python_Module.py`  
- `CS340_ProjectTwo_README_Revised_Rosalie_Reblora.docx`  

## Technologies Used  

- Python  
- MongoDB  
- PyMongo  
- Dash and JupyterDash  
- Plotly Express  
- Dash Leaflet  
- Pandas  
- Jupyter Notebook  
