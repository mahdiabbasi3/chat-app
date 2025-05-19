let socket = null;

function createSocket() {
    const token = localStorage.getItem("access_token");
    if (!token) {
        redirectToLogin();
        return;
    }

    socket = new WebSocket(`ws://${window.location.host}/ws/chat/?token=${token}`);

    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log("📩 پیام دریافتی:", data);

        if (data.error) {
            alert(data.error);
            redirectToLogin();
            return;
        }

        const chatBox = document.getElementById('chat-box');
        const msg = document.createElement('div');
        msg.classList.add('message', 'mb-2');
        msg.innerHTML = `<strong>${data.user}:</strong> ${data.message}`;
        chatBox.appendChild(msg);
        chatBox.scrollTop = chatBox.scrollHeight;
    };
}

function redirectToLogin() {
    alert("❌ لطفاً ابتدا وارد شوید");
    localStorage.setItem("redirect_after_login", window.location.pathname);
    window.location.href = "/login_page/";
}

function sendMessage() {
    const input = document.getElementById('message');
    const message = input.value.trim();
    if (!message) return;

    const token = localStorage.getItem("access_token");
    if (!token) {
        redirectToLogin();
        return;
    }

    if (socket.readyState !== WebSocket.OPEN) {
        alert("❌ اتصال وب‌سوکت فعال نیست");
        return;
    }

    socket.send(JSON.stringify({ 'message': message }));
    input.value = '';
}

// وصل شدن به سوکت فقط وقتی صفحه آماده شد و توکن داریم
window.addEventListener("load", () => {
    if (localStorage.getItem("access_token")) {
        createSocket();
    } else {
        redirectToLogin();
    }
});

// ارسال با Enter
document.getElementById('message').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
