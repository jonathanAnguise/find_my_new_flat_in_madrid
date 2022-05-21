# find_my_new_flat_in_madrid
I want to find a good apartment, but I have neither the time nor the motivation to contact the corresponding apartment owners. So here is a python project that will contact the owner of the apartment and send me a summary by email every day in the afternoon.
## Structure of the project
**TODO**

I see this like that for now:
- find_flat.py (class related to find the flat and how get information)
- contact_owner.py (class related how send message to the owner)
- data_manager.py (class getting data, doing some action on it related with message action ect... and sending to contact owner and sending me a repport)
- main.py (classic main file)

## To Do
- [ ] Search if there is an API on [idealista](www.idealista.es), if not do some webscraping
- [ ] Find how to contact the guy... Get a solution to use google sms web app? WhatsApp api? only by email (email should be the last method available because it's the esiest and also, I thing other contact are more relevant and have more impact
- [ ] Find how manage messages.
- [ ] Find how execute it on a server... Python every where coud be a good solution
