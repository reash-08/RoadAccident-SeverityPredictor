const form = document.getElementById("predictForm");
const loader = document.getElementById("loader");

const severityText =
document.getElementById("severityText");

const confidenceText =
document.getElementById("confidenceText");

const recommendation =
document.getElementById("recommendation");

const progressBar =
document.getElementById("progressBar");

const historyList =
document.getElementById("historyList");

let predictionHistory = [];

form.addEventListener("submit", async function (e) {

    e.preventDefault();

    loader.style.display = "block";

    const formData = {

        road_type:
            document.querySelector(
                '[name="road_type"]'
            ).value,

        weather:
            document.querySelector(
                '[name="weather"]'
            ).value,

        road:
            document.querySelector(
                '[name="road"]'
            ).value,

        light:
            document.querySelector(
                '[name="light"]'
            ).value,

        area:
            document.querySelector(
                '[name="area"]'
            ).value,

        speed:
            document.querySelector(
                '[name="speed"]'
            ).value,

        vehicles:
            document.querySelector(
                '[name="vehicles"]'
            ).value,

        casualties:
            document.querySelector(
                '[name="casualties"]'
            ).value
    };

    try {

        const response =
        await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body:
            JSON.stringify(formData)
        });

        const data =
        await response.json();

        loader.style.display = "none";

        if (data.error) {

            severityText.innerText =
            "Prediction Error";

            confidenceText.innerText =
            data.error;

            return;
        }

        severityText.innerText =
        data.severity;

        severityText.style.color =
        data.color;

        confidenceText.innerText =
        "Confidence: " +
        data.confidence +
        "%";

        recommendation.innerText =
        data.recommendation;

        progressBar.style.width =
        data.confidence + "%";

        addToHistory(
            data.severity,
            data.confidence
        );

    } catch (error) {

        loader.style.display = "none";

        severityText.innerText =
        "Server Error";

        confidenceText.innerText =
        error.message;
    }
});

function addToHistory(
    severity,
    confidence
) {

    const item =
    document.createElement("li");

    item.innerHTML =
    severity +
    " (" +
    confidence +
    "%)";

    predictionHistory.unshift(item);

    if (
        predictionHistory.length > 5
    ) {

        predictionHistory.pop();
    }

    historyList.innerHTML = "";

    predictionHistory.forEach(
        entry =>
        historyList.appendChild(entry)
    );
}

function resetForm() {

    form.reset();

    severityText.innerText =
    "Waiting For Prediction";

    severityText.style.color =
    "white";

    confidenceText.innerText =
    "Confidence: --";

    recommendation.innerText =
    "Submit accident details to generate prediction.";

    progressBar.style.width =
    "0%";

    historyList.innerHTML = "";

    predictionHistory = [];
}