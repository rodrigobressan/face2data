function get_prediction(image) {
    const formData = new FormData()
    formData.append('image', image);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => {
        response.json().then(data => {
            const age = data['age']
            const gender = data['gender']
            const race = data['race']

            loadingGif.style.display = "none";

            const text = `It seems that the provided picture is related to a <b>${race} ${gender}</b>, around its <b>${age} years old</b>.` +
            '<br/><br/>Take note that these predictions may not be perfectly accurate due to the small amount of samples used for training (around 20k). In case you find any issues, feel free to open an issue on the project repository.'
            resultsText.innerHTML = text;
        });
    })
    .catch(error => {
        console.log("There was an error");
    });
}

function imageUploaded(event) {
    const target = event.target;
    const image = target.files[0];

    if (!image) return;

    resultsText.innerHTML = "";

    loadingGif.style.display = "visible";
    imageContainer.src = window.URL.createObjectURL(image);

    get_prediction(image);
}

function ready() {
    resultsText = document.querySelector("#results_text");

    imageContainer = document.querySelector("#imageContainer");
    loadingGif = document.querySelector("#loadingGif");
    loadingGif.style.display = "none";

    const inputFile = document.querySelector("#image");
    inputFile.addEventListener('change', imageUploaded);
}

document.addEventListener("DOMContentLoaded", ready);

let imageContainer;
let imageClass;
let imageConfidence;
let loadingGif;