from flask import Flask, render_template_string

app = Flask(__name__)

# यह आपके सिस्टम का लुक (HTML) है
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>KING YASIR WEB SYSTEM</title>
    <style>
        body { background-color: #0f0f0f; color: #00ff00; font-family: 'Courier New', Courier, monospace; text-align: center; }
        .grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; padding: 20px; }
        .btn { background: #1a1a1a; border: 1px solid #00ff00; color: #00ff00; padding: 15px; cursor: pointer; border-radius: 5px; }
        .btn:hover { background: #00ff00; color: #000; }
        h1 { color: #32cd32; text-shadow: 0 0 10px #00ff00; }
    </style>
</head>
<body>
    <h1>👑 KING YASIR SYSTEM V3 👑</h1>
    <p>[ ONLINE CLOUD DASHBOARD ]</p>
    <div class="grid">
        <button class="btn">01 - Mobile Tracker</button>
        <button class="btn">03 - IP Tracker</button>
        <button class="btn">04 - Live Location</button>
        <button class="btn">12 - DDoS Attack</button>
        <button class="btn">21 - Phishing Link</button>
        <button class="btn">24 - WiFi Crack</button>
    </div>
    <p>System Status: <span style="color:white">Waiting for Input...</span></p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
