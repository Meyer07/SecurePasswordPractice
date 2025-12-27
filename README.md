This repo is contains a server file,client file and a sample passwords file that each serve a role in creating an environment which makes securing passwords realistic and effective way

Server file-this file acts as a version of a server in order to bridge the client file and the sample passwords file. this file transmits the information about if the password given with
a specified user name was successful 

client file- this file acts as a client asking for a specific username and password and then sends that data the server file which checks with the userdatabase created in the samplepassword
file and checks if they match and if they match it returns a successful login and if not to returns an unsuccessful login message

samplepassword-this file creates a database called userdatabse and makes three entries for the database, with an id,username and password, the database stores the user unhashed and the password
as hashed data and stores the data until it needs to be retrieved.


This project serves as two goals, it taught me much about how login pages work for not only webapplications but also as mobile applications go as well, not only how they work but also taught me 
things like sql and more network package imports in Python which will be very useful in CyberSecurity. The second goal is for any future project I want there to be a account system 
I can run and operate a system that accomplishes the goal of safely storing and securing passwords in a database.
