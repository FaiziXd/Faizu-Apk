from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Faizu Apk</title>
    <style>
        /* Basic Styling */
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
        }

        /* Animation Container */
        #animation-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: white;
            animation: fadeIn 2s ease-in-out forwards;
            height: 100vh;
            width: 100vw;
            background: black;
            justify-content: center;
        }

        /* Animation Effect */
        @keyframes fadeIn {
            0% { opacity: 0; transform: scale(0.5); }
            100% { opacity: 1; transform: scale(1); }
        }

        /* Hiding Animation after Display */
        #login-page, #options-page, #password-prompt {
            display: none;
        }

        /* Login Page Styling */
        .login-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: url('https://raw.githubusercontent.com/FaiziXd/Faizu-Apk/refs/heads/main/9c00c9c67343002135c21fbce5c7c3f5.jpg') no-repeat center center fixed;
            background-size: cover;
        }

        .login-box {
            background: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 0, 0, 0.5);
        }

        .login-box input {
            padding: 10px;
            font-size: 18px;
            border-radius: 5px;
            border: none;
            margin-bottom: 10px;
            outline: none;
            width: 80%;
            text-align: center;
        }

        .login-box button {
            padding: 10px 20px;
            font-size: 18px;
            background-color: red;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        /* Options Page Styling */
        .options-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: url('https://raw.githubusercontent.com/FaiziXd/Faizu-Apk/refs/heads/main/b4b9a65dc7d586f35b690186e2e16a3e.jpg') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
        }

        .option-button {
            padding: 15px 30px;
            margin: 10px;
            font-size: 24px;
            background: rgba(0, 0, 0, 0.8);
            color: white;
            border: 2px solid red;
            border-radius: 10px;
            cursor: pointer;
            animation: fadeInOptions 1.5s ease-in-out;
            transition: transform 0.2s;
        }

        .option-button:hover {
            transform: scale(1.05);
            box-shadow: 0px 0px 10px rgba(255, 0, 0, 0.5);
        }

        /* Password Prompt Styling */
        .password-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: url('https://raw.githubusercontent.com/FaiziXd/Faizu-Apk/refs/heads/main/b1ccc829fab0b847dab271d53123f67f.jpg') no-repeat center center fixed;
            background-size: cover;
            color: white;
            text-align: center;
        }

        .password-box {
            background: rgba(0, 0, 0, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(255, 0, 0, 0.5);
        }

        /* Animation for Options */
        @keyframes fadeInOptions {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <!-- Animation Container -->
    <div id="animation-container">
        <h1 style="font-size: 3rem; animation: glow 1s infinite alternate;">The Faizu Apk</h1>
    </div>

    <!-- Login Page -->
    <div id="login-page" class="login-container">
        <div class="login-box">
            <h2>Login</h2>
            <input type="text" id="username" placeholder="Enter Username"><br>
            <input type="password" id="password" placeholder="Enter Password"><br>
            <button onclick="showOptions()">Login</button>
        </div>
    </div>

    <!-- Options Page -->
    <div id="options-page" class="options-container">
        <h1 style="margin-bottom: 20px;">The Faizu Apk</h1>
        <div class="option-button" onclick="showPasswordPrompt('https://faizuxd.onrender.com/')">Multy Single</div>
        <div class="option-button" onclick="showPasswordPrompt('https://mone-56u0.onrender.com/')">Multy Single 2</div>
        <div class="option-button" onclick="window.location.href='https://youtube.com/@faiizuxd?si=ytoo0Gfpmmusgx6y'">YouTube 💙</div>
    </div>

    <!-- Password Prompt -->
    <div id="password-prompt" class="password-container">
        <div class="password-box">
            <h2>Enter Password To Access Faizu Apk</h2>
            <input type="password" id="passwordInput" placeholder="Enter Password"><br>
            <button onclick="checkPassword()">Submit</button>
            <button onclick="contactSupport()">Contact</button>
        </div>
    </div>

    <script>
        let selectedLink = '';

        // Animation Timeout to Show Login Page
        setTimeout(() => {
            document.getElementById('animation-container').style.display = 'none';
            document.getElementById('login-page').style.display = 'flex';
        }, 3000); // Show login page after 3 seconds

        // Show Options Page after Login
        function showOptions() {
            document.getElementById('login-page').style.display = 'none';
            document.getElementById('options-page').style.display = 'flex';
        }

        // Show Password Prompt for certain options
        function showPasswordPrompt(link) {
            selectedLink = link;
            document.getElementById('options-page').style.display = 'none';
            document.getElementById('password-prompt').style.display = 'flex';
        }

        // Check Password and Redirect
        function checkPassword() {
            const password = document.getElementById('passwordInput').value;
            if (password === 'TH3_FAIZU_H3R3') {
                window.location.href = selectedLink;
            } else {
                alert('Incorrect password! Please try again or contact support.');
            }
        }

        // Contact Support
        function contactSupport() {
            window.location.href = 'https://www.facebook.com/The.drugs.ft.chadwick.67';
        }
    </script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
