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
