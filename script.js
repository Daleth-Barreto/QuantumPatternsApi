function toggleWordInput() {
    const type = document.getElementById("patternType").value;
    document.getElementById("wordDiv").style.display = type === "word" ? "block" : "none";
}

async function generatePattern() {
    const patternType = document.getElementById("patternType").value;
    const width = parseInt(document.getElementById("width").value);
    const height = parseInt(document.getElementById("height").value);
    const word = document.getElementById("word").value;
    const toggleText = document.getElementById("toggleText");

    const data = { pattern_type: patternType, width, height };
    if (patternType === "word") data.word = word;

    // Mostrar mensaje de carga
    document.getElementById("loadingMessage").style.display = "flex";
    document.getElementById("errorMessage").style.display = "none";
    document.getElementById("resultImage").style.display = "none";

    try {
        const response = await fetch("https://quantumpatternsapi.onrender.com/patterns/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            document.getElementById("resultImage").src = url;
            document.getElementById("resultImage").style.display = "block";
        } else {
            throw new Error("Error en la respuesta");
        }
    } catch (error) {
        document.getElementById("errorMessage").style.display = "block";
    } finally {
        document.getElementById("loadingMessage").style.display = "none";
    }
}

