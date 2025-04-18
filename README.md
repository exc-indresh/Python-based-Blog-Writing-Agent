### **Setup Instruction**
- Clone the repository:
 ```bash
  git clone <repository-url>
- Move to project directory & activate the virtual enviroment using the below command
```bash
venv/Scripts/activate

- Install all the dependencies
```pip install -r requirements.txt```
- Add gemin_api_key and newdData_api_key in .env file
- Running the script
```python main.py "topic on which you want create blog"```
This will generate reponse files ie- response.md and response.json in output folder
