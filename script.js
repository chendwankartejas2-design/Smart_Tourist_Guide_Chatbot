const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");

function sendCategory(category) {
    const city = document.getElementById("city").value;
    if (!city) {
        alert("Please select a city");
        return;
    }
    sendText(`${city} ${category}`);
}

function sendMessage() {
    const msg = input.value.trim();
    if(msg==="") return;
    sendText(msg);
    input.value="";
}

function sendText(message) {
    chatBox.innerHTML += `<div class="user-msg">${message}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch("/chat", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message})
    })
    .then(res=>res.json())
    .then(data=>{
        let html = `<div class="bot-msg">${data.reply}</div>`;

        if(data.images && data.images.length>0){
            html += `<div class="image-grid">`;
            data.images.forEach(img=>{
                html += `<img src="/static/images/${img}">`;
            });
            html += `</div>`;
        }

        chatBox.innerHTML += html;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
