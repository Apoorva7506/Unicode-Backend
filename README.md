# Unicode-Backend

# task 1 :
Takes console input of binary numbers and outputs list of binary numbers from input which are divisible by 5.


# task 2:

- Created project 'spacex' and app 'dcollect'.
- Made required changes in settings.py.
- Created urls.py in dcollect 
- Created index function in views.py and linked it to urls.py in dcollect and in main folder.
- Used repuests module in index function to get data from required api. 
- Converted datestring to dateobject.
- Created a list of dictionaries having only the specified data.(l)
- Then displayed list data directly on the webpage.


# task 3:
- Created 'template' folder and created index.html and base.html.
- Edited settings.py as required.
- Rendered index.html in views.py and sent list (l) to it
and thus displayed data on the webpage using html



# task 4 first run:
- Initialized class Rdata in models.py with required fields.
- Made migrations.
- Defined a function (dataget) in models.py that:
	1. Used repuests module to get data from required api. 
	2. Converted datestring to dateobject.
	3. Created and returned a list of dictionaries having only the specified data.(l)

- Used dataget function in index function in views.py to get list and then,
using for loop  **inputted the data into the database** and displayed the data from database by rendering index.html from views.py.



# task 4 modified:
- Made some changes to index.html.(fixed a minor bug)
- Html page now shows actual images instead of link (latest update)
