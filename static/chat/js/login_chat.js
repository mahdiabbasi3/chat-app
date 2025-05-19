// function login() {
//     const username = document.getElementById("username").value;
//     const password = document.getElementById("password").value;
//
//     fetch("http://127.0.0.1:8000/api/token/", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//         },
//         body: JSON.stringify({ username, password })
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error("Login failed");
//         }
//         return response.json();
//     })
//     .then(data => {
//         localStorage.setItem("access_token", data.access);
//         alert("✅ ورود موفق بود");
//
//         // برگشت به مسیر قبلی
//         const redirectPath = localStorage.getItem("redirect_after_login") || "/chat.html";
//         window.location.href = redirectPath;
//     })
//     .catch(error => {
//         alert("❌ ورود ناموفق بود");
//     });
// }
