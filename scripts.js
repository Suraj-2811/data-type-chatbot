function addMessage(text, className) {
  let chatBox = document.getElementById("chat-box");

  let msg = document.createElement("div");
  msg.classList.add("message", className);

  chatBox.appendChild(msg);

  if (className === "bot") {
    typeEffect(msg, text); // 👈 typing animation
  } else {
    msg.innerHTML = text;
  }

  chatBox.scrollTop = chatBox.scrollHeight;
}

/* 🔥 Typing animation like ChatGPT */
function typeEffect(element, htmlText) {
  let tempDiv = document.createElement("div");
  tempDiv.innerHTML = htmlText;

  let text = tempDiv.innerText;
  let i = 0;

  element.innerHTML = "";

  let interval = setInterval(() => {
    element.innerText += text.charAt(i);
    i++;

    if (i >= text.length) {
      clearInterval(interval);
      element.innerHTML = htmlText; // restore formatting
    }
  }, 20);
}

/* Send Message */
async function sendMessage() {
  let inputField = document.getElementById("userInput");
  let input = inputField.value.trim();
  let lang = document.getElementById("language").value;

  if (input === "") return;

  addMessage(input, "user");

  try {
    let res = await fetch("http://127.0.0.1:5000/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ data: input, lang: lang })
    });

    let data = await res.json();

    let reply = `
      <b>🧠 Type:</b> ${data.type}<br><br>

      <b>📘 Definition:</b><br>${data.definition}<br><br>

      <b>💻 Code:</b>
      <pre>${data.code}</pre>

      <b>📤 Output:</b>
      <pre>${data.output}</pre>

      <b>🧩 Explanation:</b><br>
      ${data.explanation.map(step => "• " + step).join("<br>")}
    `;

    addMessage(reply, "bot");

  } catch (error) {
    addMessage("❌ Backend not connected", "bot");
  }

  inputField.value = "";
}

/* Enter key */
document.getElementById("userInput").addEventListener("keypress", function(e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});

/* Welcome message */
window.onload = function () {
  addMessage("👋 Hello! Ask me about any data type.", "bot");
};