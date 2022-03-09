#!/usr/bin/env python
# coding: utf-8

# In[55]:


from flask import Flask


# In[56]:


app = Flask(__name__)


# In[57]:


from flask import request, render_template
from werkzeug.utils import secure_filename
import speech_recognition as sr


# In[58]:


@app.route("/", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        print(filename)
        file.save("static/"+filename)
        a = sr.AudioFile("static/"+filename)
        with a as source:
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "2"))


# In[59]:


if __name__ == "__main__":
    app.run()


# In[ ]:




