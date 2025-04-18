### **Setup Instruction**
- Clone the repository:
```bash
  git clone <repository-url>
```
  
- Move to project directory & activate the virtual enviroment using the below command
```bash
venv/Scripts/activate
```

- Install all the dependencies
```bash
pip install -r requirements.txt
```
- Add gemin_api_key and newdData_api_key in .env file
- Run the script
```bash
python cli.py "topic on which you want to create blog" --tone=technical
```
- tone(optional) is a parameter and its default value is "educational" to generate blog with the current tone using gemini 
- This will generate reponse files ie- response.md and response.json in output folder
