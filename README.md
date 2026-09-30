# Camera Capture Project

Consent-based camera page: the user grants camera permission, then explicitly taps Capture & Send. The Python backend stores the photo and User-Agent.

Run: `pip install -r requirements.txt` then `python server.py` and open `http://127.0.0.1:5000`.

Public camera use requires HTTPS. Telegram notification is not preconfigured; add your own bot integration and credentials securely on the server.
