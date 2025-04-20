body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #0a192f;
    color: #ccd6f6;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
.container {
    background-color: #112240;
    padding: 3rem;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    text-align: center;
    max-width: 600px;
    width: 95%;
}
h2 {
    color: #64ffda;
    margin-bottom: 2rem;
    font-size: 2rem;
}
label {
    display: block;
    margin-bottom: 0.5rem;
    color: #a8b2d1;
    font-weight: bold;
}
input[type="number"], select, input[type="text"] {
    padding: 12px;
    margin-bottom: 1rem;
    width: calc(100% - 24px);
    font-size: 1rem;
    border-radius: 8px;
    border: 1px solid #233554;
    background-color: #1e2d4a;
    color: #ccd6f6;
    box-sizing: border-box;
}
input::placeholder {
    color: #a8b2d1;
}
button {
    background-color: #64ffda;
    color: #0a192f;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}
button:hover {
    background-color: #49ccb3;
}
#resultImage {
    margin-top: 2rem;
    width: 100%;
    height: auto;
    max-width: 100%;
    border: 2px solid #233554;
    border-radius: 8px;
    display: none;
}
#loadingMessage{
    display: none; /* Ocultar por defecto */
}
.loading-container {
    margin-top: 4rem;
    flex-direction: column;
    align-items: center;
}
.loading-container p{
    margin-top: 4rem;
}
.atom-loader {
    position: relative;
    width: 60px;
    height: 60px;
}
.nucleus {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background-color: #64ffda;
    opacity: 0.8;
    position: absolute;
    top: 0;
    left: 0;
}
.electron {
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #ccd6f6;
}
.orbit {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: 2px dashed #233554;
    animation: orbit 3s linear infinite;
}
.electron-1 {
    top: 10px;
    left: 50%;
    transform: translateX(-50%);
    animation: electron-orbit-1 3s linear infinite;
}
.electron-2 {
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    animation: electron-orbit-2 3s linear infinite;
}
.electron-3 {
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    animation: electron-orbit-3 3s linear infinite;
}
.electron-4 {
    left: 10px;
    top: 50%;
    transform: translateY(-50%);
    animation: electron-orbit-4 3s linear infinite;
}
.loading-text {
    color: #a8b2d1;
    font-size: 0.9rem;
    margin-top: 1rem;
}
#errorMessage {
    display: none;
    color: #f44336;
    font-weight: bold;
    margin-top: 2rem;
}

@keyframes orbit {
    0% { transform: translate(-50%, -50%) rotate(0deg); }
    100% { transform: translate(-50%, -50%) rotate(360deg); }
}

@keyframes electron-orbit-1 {
    0% { transform: translateX(-50%) rotate(0deg) translateY(-30px); }
    100% { transform: translateX(-50%) rotate(360deg) translateY(-34px); }
}
@keyframes electron-orbit-3 {
    0% { transform: translateX(-50%) rotate(0deg) translateY(36px); }
    100% { transform: translateX(-50%) rotate(360deg) translateY(40px); }
}
@keyframes electron-orbit-2 {
    0% { transform: translateX(-50%) rotate(0deg) translateX(42px); }
    100% { transform: translateX(-50%) rotate(360deg) translateX(38px); }
}
@keyframes electron-orbit-4 {
    0% { transform: translateX(-50%) rotate(0deg) translateX(-40px); }
    100% { transform: translateX(-50%) rotate(360deg) translateX(-35px); }
}
