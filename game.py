<html>
<head>
  <style>
    body {
      background: #fef3c7;
      font-family: sans-serif;
      text-align: center;
      padding: 2rem;
    }

    #cookie {
      width: 150px;
      height: 150px;
      background: url('https://upload.wikimedia.org/wikipedia/commons/7/7e/Chocolate_chip_cookie.png') no-repeat center;
      background-size: cover;
      border: none;
      cursor: pointer;
      margin-bottom: 1rem;
    }

    #score {
      font-size: 2rem;
      color: #92400e;
    }

    .upgrade {
      margin-top: 1rem;
      padding: 0.5rem 1rem;
      background: #fbbf24;
      border: none;
      cursor: pointer;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <h1>🍪 Cookie Clicker</h1>
  <button id="cookie"></button>
  <div id="score">Cookies: 0</div>
  <button class="upgrade" onclick="buyUpgrade()">Buy Upgrade (Cost: 50)</button>

  <script>
    let cookies = 0;
    let multiplier = 1;

    const scoreDisplay = document.getElementById("score");
    const cookieButton = document.getElementById("cookie");

    cookieButton.onclick = () => {
      cookies += multiplier;
      updateScore();
    };

    function buyUpgrade() {
      if (cookies >= 50) {
        cookies -= 50;
        multiplier += 1;
        updateScore();
        alert("Upgrade purchased! 🍪 x" + multiplier);
      } else {
        alert("Not enough cookies!");
      }
    }

    function updateScore() {
      scoreDisplay.textContent = "Cookies: " + cookies;
    }
  </script>

</body>
</html>
