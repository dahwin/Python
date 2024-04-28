from pyngrok import ngrok

# Setting an auth token allows us to open multiple
# tunnels at the same time
ngrok.set_auth_token("2R1tsuod04ayFPLUINN1J0J5qpJ_89tdxKVwtCs9F7kvG1uhv")

# Start ngrok with the custom configuration file
ngrok_tunnel2 = ngrok.connect(8000, bind_tls=True)
print(ngrok_tunnel2)
from fastapi import FastAPI, UploadFile
import os
import uvicorn
# Init App
app = FastAPI()

# Save uploaded files in the current working directory
upload_directory = './'

# Ensure the upload directory exists
os.makedirs(upload_directory, exist_ok=True)

@app.post("/file/upload")
async def upload_file(file: UploadFile):
    # Generate a unique filename for the uploaded file
    file_path = os.path.join(upload_directory, file.filename)

    # Save the uploaded file to the specified directory
    with open(file_path, 'wb') as file_object:
        file_object.write(file.file.read())

    # Return a response indicating the filename and content type
    return {"filename": file.filename, "content_type": file.content_type}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)