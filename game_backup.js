// give constants to elements as they dont change
const movesElement = document.querySelector("#moves");

const digitElement = document.querySelector("#digit");
const currentElement = document.querySelector("#current");
const foresight1Element = document.querySelector("#foresight_1");
const foresight2Element = document.querySelector("#foresight_2");
const foresight3Element = document.querySelector("#foresight_3");

// buttons
const newGame = document.querySelector("#new_game");

const tradeOpBtn = document.querySelector("#trade_op");
const tradeNoBtn = document.querySelector("#trade_no");

const additionBtn = document.querySelector(".addition");
const subtractionBtn = document.querySelector(".subtraction");
const multiplicationBtn = document.querySelector(".multiplication");
const divisionBtn = document.querySelector(".division");

const btns_toggle = {};
const btns = [];

function construct(){
    const card_list = document.getElementsByClassName("cards");
    // for pages that do not have cards, do not initialise cards and
    // inform the calling function that there are no cards to construct
    if (card_list.length == 0) { return false; }
    for(i=0;i<4;i++){
        btns[i] = card_list[i];
        btns_toggle[card_list[i].id] = false;
    }

    return true;
}

function add_listen(){
    const card_list = document.getElementsByClassName("cards");
    for(i=0;i<4;i++){
        let card = card_list[i];
        card.addEventListener("click", function(){
            card.className = "game_sqr cards pressed_card";
        });
        card.addEventListener("mousedown", function(){
            card.className = "game_sqr cards";
        });
    }
}

// construct cards upon loading the window
window.addEventListener('load', function (){
    // if there are no cards to make (e.g. stats or rules page), construct() returns false
    if (!construct()) return; 
    add_listen();
});

// moves counter
let movesCounter = 0; // moves counter starts at 0
let gameOver = false; // determine if the game is over, if the game is over buttons except new game will be diabled

// generate a random number between min and max, default min is 1 and max is 10
const randomNumber = (min = 1, max = 9) => {
  return Math.floor(Math.random() * max + min);
};

// resets the game & generate new random numbers
const startNewGame = () => {
  gameOver = false;
  movesCounter = 0;

  movesElement.textContent = movesCounter;

  digitElement.textContent = randomNumber(10, 100);

  currentElement.textContent = randomNumber();
  foresight1Element.textContent = randomNumber();
  foresight2Element.textContent = randomNumber();
  foresight3Element.textContent = randomNumber();
};

startNewGame();

// starts a new game
newGame.addEventListener("click", startNewGame);

// increment moves counter by 1
const incrementMovesCounter = () => {
  movesCounter++;
  movesElement.textContent = movesCounter;
};

/* Moves foresight1 to current spot, 
   foresight2 to foresight1 spot, 
   foresight3 to foresight2 spot 
   and generate a new number at foresight3
   then increment moves counter
*/
const move = () => {
  currentElement.textContent = foresight1Element.textContent;
  foresight1Element.textContent = foresight2Element.textContent;
  foresight2Element.textContent = foresight3Element.textContent;

  foresight3Element.textContent = randomNumber();

  incrementMovesCounter();
};

// update digit element
const updateDigit = (result) => {
  if (result === 0) {
    gameOver = true;
    digitElement.textContent = "You win!";
  } else {
    digitElement.textContent = result;
    move(); // perform a move
  }
};

// calculate digit based on the operator (addition, subtraction, multiplication) button clicked
const calculateDigit = (operation) => {
  if (gameOver) return; // prevent button click game over is true

  const digitText = Number(digitElement.textContent);

  if (operation === "addition") {
    const result = digitText + Number(currentElement.textContent);
    updateDigit(result);
  } else if (operation === "subtraction") {
    const result = digitText - Number(currentElement.textContent);

    updateDigit(result);
  } else if (operation === "multiplication") {
    const result = digitText * Number(currentElement.textContent);

    updateDigit(result);
  } else if (operation === "division") {
    const digitText = Number(digitElement.textContent);
    const currentText = Number(currentElement.textContent);

    // prevent click when digit is not divisible by current
    if (digitText % currentText !== 0) return;

    const result = digitText / currentText;

    updateDigit(result);
  }
};

additionBtn.addEventListener("click", () => {
  calculateDigit("addition");
});

subtractionBtn.addEventListener("click", () => {
  calculateDigit("subtraction");
});

multiplicationBtn.addEventListener("click", () => {
  calculateDigit("multiplication");
});

divisionBtn.addEventListener("click", () => {
  calculateDigit("division");
});

tradeOpBtn.addEventListener("click", () => {
  // prevent button click when digit is less than or equal to 0
  if (gameOver) return;

  const currentNumber = currentElement.textContent;
  const foresight1Number = foresight1Element.textContent;

  currentElement.textContent = foresight1Number;
  foresight1Element.textContent = currentNumber;

  incrementMovesCounter();
});

tradeNoBtn.addEventListener("click", () => {
  // prevent button click when digit is less than or equal to 0
  if (gameOver) return;

  const foresight1Number = foresight1Element.textContent;
  const foresight2Number = foresight2Element.textContent;

  foresight1Element.textContent = foresight2Number;
  foresight2Element.textContent = foresight1Number;

  incrementMovesCounter();
});

// Submit results to server
function submit_results(nMoves, wonThisGame) {
  // type check
  if (typeof(nMoves) != "number") {
      console.log("%c%s%c%s", 
                  "background-color:black; color:yellow; font-weight:bold;",
                  `submit_results:`,
                  "color:red;",
                  `nMoves must be a number but a ${typeof(nMoves)} was given!`
                 );
      return false;
  }
  if (typeof(wonThisGame) != "boolean") {
      console.log("%c%s%c%s", 
                  "background-color:black; color:yellow; font-weight:bold;",
                  `submit_results:`,
                  "color:red;",
                  `wonThisGame must be a boolean but a ${typeof(wonThisGame)} was given!`
                 );
      return false;
  }
  // all types are as expected
  location.href = `/update/?moves=${String(nMoves)}&won=${String(wonThisGame)}`;
}

// Modal variables 
var modal = document.getElementById("SignUpModal");
var loginModal = document.getElementById("LogInModal");
var btn = document.getElementById("sign_up");
var loginBtn = document.getElementById("login");
var btn2 = document.getElementById("sign2");
var loginBtn2 = document.getElementById("login2");
var span = document.getElementsByClassName("close")[0];
var span1 = document.getElementsByClassName("close1")[0]
var loginLn = document.getElementById("loginln");

// Click button, opens modal
btn.onclick = function() {
  modal.style.display = "block";
}

// Click button, opens login modal
loginBtn.onclick = function() {
    loginModal.style.display = "block";
}

//modal for dropdown sign_up
btn2.onclick = function() {
  modal.style.display = "block";
}

// model for dropdown login
loginBtn2.onclick = function() {
  loginModal.style.display = "block";
}

// Close the modal  
span.onclick = function() {
  modal.style.display = "none";
}

// Close the modal  
span1.onclick = function() {
    loginModal.style.display = "none";
  }


// Close modal if background is clicked
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Close modal (sign-up) and open login modal if link is clicked
loginLn.onclick = function() {
    modal.style.display = "none"; // close modal (sign-up)
    loginModal.style.display = "block"; // open login modal
}
