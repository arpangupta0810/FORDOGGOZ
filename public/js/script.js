var clsbtn = document
  .querySelector(".icon-button")
  .addEventListener("click", toggleModal);

var opnbtn = document
  .querySelector(".register")
  .addEventListener("click", toggleModal);

var modal = document.querySelector(".modal");

function toggleModal() {
  modal.classList.toggle("active");
}

var form = document.getElementById("locationForm");
var helper_modal = document.getElementById("myModal");
var modalContent = document.querySelector(".modal-content");
var span = document.getElementsByClassName("close")[0];
var nearestPeopleDiv = document.getElementById("nearestPeople");

form.addEventListener("submit", function (event) {
  event.preventDefault();
  var location = document.getElementById("location").value;

  fetch("/find-people", {
    method: "POST",
    body: new URLSearchParams({
      location: location,
    }),
  })
    .then((response) => response.text())
    .then((data) => {
      nearestPeopleDiv.innerHTML = data;
      helper_modal.style.display = "block";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

span.onclick = function () {
  helper_modal.style.display = "none";
};

window.onclick = function (event) {
  if (event.target === helper_modal) {
    helper_modal.style.display = "none";
  }
};
