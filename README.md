# Dead and Injured: A Battle of Wits in Python 🙂

Step into the engaging world of Dead and Injured, a game where sharp deduction and strategic thinking are your greatest allies! This project marks another step in my journey as a Python developer, showcasing how code can bring classic logic puzzles to life.

**The Core Challenge:**🧠

The game revolves around a secret 4-digit code composed of unique numbers (0-9). In each round, you'll take on two key roles:

1.  **The Codebreaker:** Attempt to decipher the computer's hidden 4-digit pin.
2.  **The Codemaker:** Create your own secret 4-digit pin that the computer will try to crack.

With each guess made by either you or the computer, valuable feedback will be provided in the form of "Dead" and "Injured" clues.

**Understanding the Feedback:**

* **Dead:** A digit in the guess that is absolutely correct and in the perfect position within the secret code.
* **Injured:** A digit in the guess that is present in the secret code but is located in a different position.

**How to Play:**🔥

1.  **Get Started:** Ensure you have the `dead_and_injured_module.py` file (containing the game logic) and the `arts.py` file (for the logo and welcome image) in the same directory as your main script. Run the main script.

2.  **Welcome and Setup:** You'll be greeted with a visual welcome. The game will then prompt you to enter your own secret 4-digit pin, one unique digit at a time.

3.  **The Dual Challenge:** In each round, two things happen simultaneously:
    * **Your Guess:** You will be prompted to enter your 4-digit guess for the computer's secret pin. The feedback ("Dead" and "Injured") will be displayed in a clear table.
    * **Computer's Guess:** The computer will also make a 4-digit guess in an attempt to crack your secret pin. The computer's guess and the feedback you would theoretically provide to it are shown.

4.  **The Race to Decode:** The game continues until either you correctly guess the computer's pin (4 "Dead") or the computer correctly guesses your pin (as determined by its narrowing-down strategy).

5.  **Victory and Results:** Once a winner is determined, the game will announce the victor and reveal both your secret pin and the computer's secret pin.

6.  **Play Again?:** You'll be asked if you want to play another round of this engaging battle of wits.

**My Journey as a Python Developer - Crafting This Game:**👨‍💻🚀

This project is a tangible outcome of my exploration and growth in the Python programming language. It demonstrates my understanding and application of several key concepts:

* **Modular Design:** Separating the core game logic into the `dead_and_injured_module.py` for better organization and reusability.
* **Functions:** Creating modular blocks of code (like `generate_user_pin`, `compare_guesses`, `narrow_down_guess`) to handle specific tasks.
* **Data Structures:** Utilizing lists to represent the numerical codes and guesses.
* **Input and Output:** Managing user interaction through `input()` and providing clear feedback using `print()` and formatted tables.
* **Game Loop Control:** Implementing `while` loops to manage the flow of the game and determine when it ends.
* **Randomness (`random`):** Introducing unpredictability in the computer's pin generation and initial guesses.
* **Combinatorics (`itertools`):** Leveraging permutations to form the basis of the computer's intelligent guessing strategy, allowing it to systematically narrow down possibilities.
* **Data Presentation (`prettytable`):** Enhancing the user experience by displaying guess history and feedback in an organized table.
* **External Modules (`arts`):** Integrating visual elements (like the game logo) to make the game more engaging.

Building Dead and Injured has been a valuable exercise in applying these Python skills to create an interactive and logical game. It reflects my commitment to learning and building increasingly complex and engaging applications. I hope you enjoy playing the result of this ongoing journey!
