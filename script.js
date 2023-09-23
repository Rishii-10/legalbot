const chatbox = document.querySelector(".chatbox");
const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const voiceButton = document.getElementById("voice-button");
const fileInput = document.getElementById('file-input');
const fileUploadLabel = document.querySelector('.file-upload label');

let userMessage = null; // Variable to store user's message
const API_KEY = "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"; // Paste your API key here
const inputInitHeight = chatInput.scrollHeight;

fileLabel.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', handleFileUpload);

function handleFileUpload(e) {
  const selectedFile = e.target.files[0];
  if (selectedFile) {
    // You can access the selected file using `selectedFile`
    // Here, you can upload the file to your server or perform other actions
    console.log('Selected File:', selectedFile.name);
  }
}

const createChatLi = (message, className) => {
    // Create a chat <li> element with passed message and className
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", `${className}`);
    let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
    chatLi.innerHTML = chatContent;
    chatLi.querySelector("p").textContent = message;
    return chatLi; // return chat <li> element
}

function handleFileUpload(e) {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      // You can access the selected file using `selectedFile`
      // Here, you can upload the file to your server or perform other actions
      console.log('Selected File:', selectedFile.name);
    }
  }
  
function handleDragOver(e) {
    e.preventDefault();
    fileUploadLabel.classList.add('drag-over');
  }
  
function handleDragLeave(e) {
    e.preventDefault();
    fileUploadLabel.classList.remove('drag-over');
  }
  
function handleFileDrop(e) {
    e.preventDefault();
    fileUploadLabel.classList.remove('drag-over');
  
    const droppedFiles = e.dataTransfer.files;
    if (droppedFiles.length > 0) {
      // You can access the dropped files using `droppedFiles`
      // Here, you can upload the files to your server or perform other actions
      console.log('Dropped Files:', droppedFiles);
    }
  }

function startVoiceRecognition() {
    const recognition = new webkitSpeechRecognition(); // Create a recognition instance
    recognition.continuous = false; // Set to true for continuous recognition
    recognition.lang = "en-US"; // Set the recognition language
  
    recognition.onresult = function (event) {
      const transcript = event.results[0][0].transcript;
      chatInput.value = transcript; // Set the chat input to the recognized text
    };
  
    recognition.start(); // Start listening
}
// Function to handle voice output (text-to-speech)
function speak(text) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);
    synth.speak(utterance);
  }
  
  // Add a click event listener to the voice button
  voiceButton.addEventListener("click", function () {
    startVoiceRecognition();
  });
// Modify the handleChat function to also speak the user's message
function handleChat() {
    userMessage = chatInput.value.trim();
    if (!userMessage) return;
  
    // ... (rest of the handleChat function as before)
  
    // After generating the response, speak it
    const responseText = incomingChatLi.querySelector("p").textContent;
    speak(responseText);
  }
const generateResponse = (chatElement) => {
    const API_URL = "https://api.openai.com/v1/chat/completions";
    const messageElement = chatElement.querySelector("p");

    // Define the properties and message for the API request
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{role: "user", content: userMessage}],
        })
    }

    // Send POST request to API, get response and set the reponse as paragraph text
    fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        messageElement.textContent = data.choices[0].message.content.trim();
    }).catch(() => {
        messageElement.classList.add("error");
        messageElement.textContent = "Oops! Something went wrong. Please try again.";
    }).finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
}

const handleChat = () => {
    userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
    if(!userMessage) return;

    // Clear the input textarea and set its height to default
    chatInput.value = "";
    chatInput.style.height = `${inputInitHeight}px`;

    // Append the user's message to the chatbox
    chatbox.appendChild(createChatLi(userMessage, "outgoing"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
    
    setTimeout(() => {
        // Display "Thinking..." message while waiting for the response
        const incomingChatLi = createChatLi("Thinking...", "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(incomingChatLi);
    }, 600);
}

chatInput.addEventListener("input", () => {
    // Adjust the height of the input textarea based on its content
    chatInput.style.height = `${inputInitHeight}px`;
    chatInput.style.height = `${chatInput.scrollHeight}px`;
});

chatInput.addEventListener("keydown", (e) => {
    // If Enter key is pressed without Shift key and the window 
    // width is greater than 800px, handle the chat
    if(e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
    }
});

sendChatBtn.addEventListener("click", handleChat);
