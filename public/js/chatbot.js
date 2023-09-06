var loader = document.getElementById("preloader");
window.addEventListener("load", function () {
  setTimeout(() => {
    loader.style.display = "none";
  }, 1000);
});

const chatbox = document.querySelector(".msger");
const buttonChat = document.querySelector(".msger-header");

buttonChat.addEventListener("click", () => {
  chatbox.classList.toggle("active");
  console.log("Clicked");
});

const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

// Icons made by Freepik from www.flaticon.com
const BOT_IMG = "https://freesvg.org/img/1538298822.png";
const PERSON_IMG =
  "https://png.pngitem.com/pimgs/s/522-5220445_anonymous-profile-grey-person-sticker-glitch-empty-profile.png";
const BOT_NAME = "Zeus";
const PERSON_NAME = "You";

msgerForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const msgText = msgerInput.value;
  if (!msgText) return;

  appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
  msgerInput.value = "";
  botResponse(msgText);
});

function appendMessage(name, img, side, text) {
  //   Simple solution for small apps
  const msgHTML = `<div class="msg ${side}-msg">
  <div class="msg-img" style="background-image: url(${img})"></div>

  <div class="msg-bubble">
    <div class="msg-info">
      <div class="msg-info-name">${name}</div>
      <div class="msg-info-time">${formatDate(new Date())}</div>
    </div>

    <div class="msg-text">${text}</div>
  </div>
</div>
`;
  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

function botResponse(rawText) {
  setTimeout(() => {
    // Bot Response
    $.get("/get", { msg: rawText }).done(function (data) {
      console.log(rawText);
      console.log(data);
      const msgText = data;
      appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
    });
  }, 1000);
}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}
