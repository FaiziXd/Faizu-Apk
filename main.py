from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Homepage (Login Page)
@app.route('/')
def index():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Faizu Apk - Login</title>
    <style>
        body { font-family: Arial, sans-serif; background: url('https://raw.githubusercontent.com/FaiziXd/Faizu-Apk/refs/heads/main/9c00c9c67343002135c21fbce5c7c3f5.jpg') no-repeat center center fixed; background-size: cover; }
        .login-container { background-color: rgba(0, 0, 0, 0.5); padding: 30px; width: 300px; margin: 100px auto; border-radius: 10px; color: white; text-align: center; }
        input[type="text"], input[type="password"] { padding: 10px; width: 100%; margin: 10px 0; border-radius: 5px; border: none; }
        button { padding: 10px 20px; background-color: #f00; border: none; color: white; width: 100%; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>The Faizu Apk</h2>
        <form method="POST" action="/options">
            <input type="text" name="username" placeholder="Enter username" required>
            <input type="password" name="password" placeholder="Enter password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
    """)

# Options Page after login
@app.route('/options', methods=['POST'])
def options():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check login credentials
    if username == 'admin' and password == 'admin123':  # Replace with your own logic
        return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Faizu Apk - Options</title>
    <style>
        body { font-family: Arial, sans-serif; background: url('https://raw.githubusercontent.com/FaiziXd/Faizu-Apk/refs/heads/main/9c00c9c67343002135c21fbce5c7c3f5.jpg') no-repeat center center fixed; background-size: cover; }
        .options-container { background-color: rgba(0, 0, 0, 0.5); padding: 30px; width: 300px; margin: 100px auto; border-radius: 10px; color: white; text-align: center; }
        button { padding: 10px 20px; background-color: #f00; border: none; color: white; width: 100%; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="options-container">
        <h2>The Faizu Apk - Choose Option</h2>
        <form method="POST" action="/password">
            <button name="link" value="https://herf-2-faizu-apk.onrender.com/">Multy Single</button>
            <button name="link" value="https://mone-56u0.onrender.com/">Multy Single 2</button>
            <button name="link" value="https://youtube.com/@faiizuxd?si=ytoo0Gfpmmusgx6y">YouTube 💙</button>
        </form>
    </div>
</body>
</html>
        """)
    else:
        return redirect(url_for('index'))  # Redirect back to login if credentials are incorrect

# Password Page for accessing specific links
@app.route('/password', methods=['POST'])
def password():
    user_password = request.form.get('passwordInput')

    if user_password == 'TH3_FAIZU_H3R3':
        return redirect(request.form.get('link'))  # Redirect to selected link if password is correct
    else:
        return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enter Password</title>
    <style>
        body { font-family: Arial, sans-serif; background: url('https://raw.githubusercontent.com/FaiziXd/Faizu-Apk/refs/heads/main/b1ccc829fab0b847dab271d53123f67f.jpg') no-repeat center center fixed; background-size: cover; }
        .password-container { background-color: rgba(0, 0, 0, 0.5); padding: 30px; width: 300px; margin: 100px auto; border-radius: 10px; color: white; text-align: center; }
        input[type="password"] { padding: 10px; width: 100%; margin: 10px 0; border-radius: 5px; border: none; }
        button { padding: 10px 20px; background-color: #f00; border: none; color: white; width: 100%; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="password-container">
        <h2>Enter Password to Proceed</h2>
        <form method="POST" action="/password">
            <input type="password" name="passwordInput" placeholder="Enter Password" required>
            <button type="submit">Submit</button>
        </form>
        {% if error %}
        <p style="color: red;">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
        """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
