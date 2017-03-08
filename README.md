# Interactive Programming: Data Visualization
### Noah Rivkin and Gracey Wilson
#### Software Design Spring 2017


Project Proposal: https://docs.google.com/document/d/13pr2W9u3S5DBG2-iYA_RqwFVpTL5CEx4wzUfIGuZatg/edit?usp=sharing

## Project Overview
We worked with data from the International Monetary Fund and data visualization tools in Python, to create a map info-graphic that presents information on global gender inequality over time. The main data points presented in the info-graphic are each country’s “Gender Inequality Index” and "Gender Development Index". These measurements, initiated in 2010 by the United Nations Development Programme, describes the loss of achievement within a country due to gender disparity. Each country’s index (a number between 0 and 1, with a higher number meaning more inequality and therefore more loss) is calculated using evidence along three axes: reproductive health, educational empowerment, and labor market participation. Users can interact with the info-graphic by selecting the year they'd like to see.


## Results [~2-3 paragraphs + figures/examples]

Present what you accomplished. This will be different for each project, but screenshots are likely to be helpful.

## Implementation

Our program is structured around three classes. The highest level class is the Map() class. Below that is a Location() class, and finally a Dataset() class. The Map object contains a list of Location objects, each of which contains a Dataset object. The Map object is contains the state of the program, and all the information that needs to be passed to plotly in order to render our maps. Each Location object holds the data needed to render a specific country. Each Dataset object holds a particular set of data, and information identifying the type of information stored.

One key design decision we made was the format in which we stored our data. We considered tuples, lists, dictionaries, and a number of nested structures. We eventually decided to use a list inside a dictionary. We came to the conclusion that such a format was best suited for our program, because it interfaced with the plotly library relatively conveniently.

![alt text](https://github.com/graceyw/InteractiveProgramming/blob/master/UML_diagram.png "")

## Reflection [~2 paragraphs]

From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?

Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?

We were successful in building a scaffolded python file in the beginning, but we didn't plan quite as well on the time scale
Both partners spent approximately the amount of time we expected to on the project.

We knew from the start that a main struggle throughout the project would be our difference in levels of experience. We had planned to divide the work evenly, but the coding work ended up skewed towards the more experienced partner. Because both members' learning goals involved learning to work with a partner who's at a different level, we hypothesize pair programming might have supported a more effective learning experience for both partners. If we did this again, we might try more pair programming, or at least ensure that both partners have a full understanding of the program we're trying to write *before* we divide up the work.


*Italicize*
**Bold**

ctrl shift M allows preview of markdown files
