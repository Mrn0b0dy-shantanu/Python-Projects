from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
import subprocess

#setting up the flask site
app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
   "admin" : "1234"
}


@auth.get_password
#setting up authentication

def get_the_dang_pass(username):
   if username in users:
      return users.get(username)
   return None


@app.route("/")
@auth.login_required

#The actual command execution
def command_executor():
    command = request.args.get("command")
    #It fetches the "command=xyz" from the parameter 
    try:
        output = subprocess.check_output(command, shell=True)
        #It inputs the command into the device 
        return output.decode()
        #It decodes the command from bytes to strings
    except subprocess.CalledProcessError as e:
        return str(e)
       

if __name__ == "__main__":
 
 app.run()

