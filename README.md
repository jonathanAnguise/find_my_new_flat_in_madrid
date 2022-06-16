# find_my_new_flat_in_madrid
I want to find a good apartment, but I have neither the time nor the motivation to contact the corresponding apartment owners. So here is a python project that will create a marckdown file with all the apartments that match my criteria to help me in my search.
## How to Use

### Set up the project.
1. clone project:
   ```bash
   git clone https://github.com/jonathanAnguise/find_my_new_flat_in_madrid.git
   ```
2. Ask for api keys here: [https://developers.idealista.com/access-request](https://developers.idealista.com/access-request)
3. Create .env file with api credentials
   ```bash
   echo 'APIKEY="api_key_here"'>.env
   echo 'SECRET="your_secret_here"'>>.env
   ```
4. Create virtual env and install requirements
   ```bash
   python -m venv
   pip install -r requirements.txt
   ```
5. Edit in main.py filters_param for your personal flat choice and location

### How to run

   ```bash
   python3 main.py
   ```
### Project structure
- already_sent.txt --> text file where is registered flat unique id
- api_idealista.py --> file managing api request with idealista.com
- data_manager.py --> file managing answer from api
- .env --> file **to create** in order to load APIKEY="xxxxxx" and SECRET="xxxxxxxx" to access Oauth idealista api
- flat_report.md --> report generated 
- main.py --> file to execute
- README.md --> Current file
- request_answer.json --> example of request for debug mode

