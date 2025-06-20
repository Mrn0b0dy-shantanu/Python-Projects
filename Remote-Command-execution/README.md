
# 🔧 Remote Command Execution Web App (Flask + HTTP Basic Auth)



---

# 👨‍💻 Code/Modules Used

- python3
- flask
- flask_httpauth
 
---



## 🛠️ Running the code

To run this code, follow these steps:

- Install the project's dependencies using the requirements.txt file:

```bash
pip3 install -r requirements.txt
```

- Run the Python script:

```bash
python your_script.py
```





---

### To run a command
You can add it as a parameter in the URL, along with a basic username and password authentication
Here's an example curl:
```bash
curl -u admin:password -X GET -i http://localhost:5000/?command=whoami -la
```
If the command runs successfully you are in luck 🍀.
<p> And you will see the command output in the browser.<p>
If an error occurs, you will see an error message.

  
