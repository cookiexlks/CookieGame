<html>
<head>
  <style>
    body {
      margin: 0;
      overflow: hidden;
      background: #fff7ed;
      font-family: sans-serif;
    }

    #game {
      position: relative;
      width: 100vw;
      height: 100vh;
    }

    .cookie {
      position: absolute;
      width: 50px;
      height: 50px;
      background: url('https://upload.wikimedia.org/wikipedia/commons/7/7e/Chocolate_chip_cookie.png') no-repeat center;
      background-size: cover;
    }

    #basket {
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      width: 100px;
      height: 50px;
      background: #92400e;
      border-radius: 10px;
    }

    #score {
      position: absolute;
      top: 10px;
      left: 10px;
      font-size: 1.5rem;
      color: #92400e;
    }
  </style>
</head>
<body>

  <div id="game">
    <div id="basket"></div>
    <div id="score">Score: 0</div>
  </div>

  <script>
    let score = 0;
    const game = document.getElementById("game");
    const basket = document.getElementById("basket");
    const scoreDisplay = document.getElementById("score");

    document.addEventListener("mousemove", e => {
      basket.style.left = `${e.clientX - 50}px`;
    });

    function dropCookie() {
      const cookie = document.createElement("div");
      cookie.classList.add("cookie");
      cookie.style.left = `${Math.random() * window.innerWidth}px`;
      game.appendChild(cookie);

      let y = 0;
      const fall = setInterval(() => {
        y += 5;
        cookie.style.top = `${y}px`;

        const basketRect = basket.getBoundingClientRect();
        const cookieRect = cookie.getBoundingClientRect();

        if (
          cookieRect.bottom >= basketRect.top &&
          cookieRect.left >= basketRect.left &&
          cookieRect.right <= basketRect.right
        ) {
          score++;
          scoreDisplay.textContent = "Score: " + score;
          cookie.remove();
          clearInterval(fall);
        }

        if (y > window.innerHeight) {
          cookie.remove();
          clearInterval(fall);
        }
      }, 30);
    }

    setInterval(dropCookie, 1000);
  </script>

</body>
</html>
