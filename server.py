from pathlib import Path
from datetime import datetime,timezone
from flask import Flask,request,jsonify,send_from_directory
app=Flask(__name__); uploads=Path('uploads'); uploads.mkdir(exist_ok=True)
@app.get('/')
def index(): return send_from_directory('.', 'index.html')
@app.post('/upload')
def upload():
    photo=request.files.get('photo')
    if not photo:return jsonify(error='No photo received.'),400
    ts=datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S_%f'); name=f'capture_{ts}.jpg'; photo.save(uploads/name)
    ua=request.headers.get('User-Agent','Unknown'); (uploads/(name+'.txt')).write_text(f'Captured: {datetime.now(timezone.utc).isoformat()}\nUser-Agent: {ua}\n',encoding='utf-8')
    return jsonify(ok=True,filename=name,user_agent=ua)
if __name__=='__main__': app.run(host='127.0.0.1',port=5000)
