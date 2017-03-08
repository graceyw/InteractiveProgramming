# Interactive Programming: Data Visualization
### Noah Rivkin and Gracey Wilson
#### Software Design Spring 2017


Project Proposal: https://docs.google.com/document/d/13pr2W9u3S5DBG2-iYA_RqwFVpTL5CEx4wzUfIGuZatg/edit?usp=sharing

## Project Overview
We worked with data from the International Monetary Fund and used data visualization tools in Python to create two map info-graphics that present information on global gender equality over time. The main data points presented in the info-graphics are each country’s “Gender Development Index” and "Gender Inequality Index" over time, both of which are measurements initiated by the United Nations Development Programme.

The Development Index was introduced as a gender-focused part of the Human Development Index and addresses gender gaps in life expectancy, education and income. A higher index equates to a greater balance between genders. The Inequality Index was introduced in 2010 to account for some of the shortcomings of the Development Index. It describes the loss of achievement within a country due to gender disparity and is calculated using evidence along three axes: reproductive health, educational empowerment, and labor market participation. Each country’s Inequality Index is a number between 0 and 1, with a higher number meaning more inequality and therefore more loss due to gender.

## Results

Below are screenshots of the two maps we created. One displays the Development Index and the other the Inequality Index. Users can interact with the maps by selecting the year they'd like to see and hovering over the country to see the index for that location during that time frame.

![alt text](/home/gracey/InteractiveProgramming/InequalityNorway1995.png)
Figure 1: The Gender Inequality Index Map, currently showing Norway's index in 1995.

![alt text](/home/gracey/InteractiveProgramming/InequalityNorway2010.png)
Figure 2: The Gender Inequality Index Map, currently showing Norway's index in 2010.

![alt text](/home/gracey/InteractiveProgramming/DevelopmentIndia1995.png)
Figure 3: The Gender Development Index Map, currently showing India's index in 1995.

![alt text](/home/gracey/InteractiveProgramming/DevelopmentIndia2010.png)
Figure 4: The Gender Development Index Map, currently showing India's index in 2010.


## Implementation

Our program is structured around three classes. The highest level class is the Map() class. Below that is a Location() class, and finally a Dataset() class. The Map object contains a list of Location objects, each of which contains a Dataset object. The Map object is contains the state of the program, and all the information that needs to be passed to plotly in order to render our maps. Each Location object holds the data needed to render a specific country. Each Dataset object holds a particular set of data, and information identifying the type of information stored.

One key design decision we made was the format in which we stored our data. We considered tuples, lists, dictionaries, and a number of nested structures. We eventually decided to use a list inside a dictionary. We came to the conclusion that such a format was best suited for our program, because it interfaced with the plotly library relatively conveniently.

![alt text](/home/gracey/InteractiveProgramming/UML_diagram.png)
Figure 5: UML Class Diagram.

## Reflection

We were successful in scaffolding out the program in the beginning, but could have been more successful at scoping our time out as well; the workload definitely increased as the project moved forward. In the end however, both partners spent approximately the amount of time we expected to on the project.

We knew from the start that a main struggle throughout the project would be our differences in levels of experience. We had planned to divide the work evenly, but the coding work ended up skewed towards the more experienced partner. Because both members' learning goals involved learning to work with a partner who's at a different level, we hypothesize pair programming might have supported a more effective learning experience for both partners. If we did this again, we might try more pair programming, or at least ensure that both partners have a full understanding of the program we're trying to write *before* we divide up the work.

With regards to design, we learned about the Model-View-Controller framework in the final stages of our project. We decided to finish building using our original approach, but we recognize that the MVC structure might have been a very successful approach to this project and plan on keeping it in mind for potentially cleaner implementations in future projects.
