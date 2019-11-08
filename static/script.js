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

            resultAge.innerHTML = `Age: ${age}`;
            resultGender.innerHTML = `Gender: ${gender}`;
            resultRace.innerHTML = `Race: ${race}`;
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

    resultAge.innerHTML = "";
    resultGender.innerHTML = "";
    resultRace.innerHTML = "";

    loadingGif.style.display = "visible";
    imageContainer.src = window.URL.createObjectURL(image);

    get_prediction(image);
}

function ready() {
    resultAge = document.querySelector("#resultAge");
    resultGender = document.querySelector("#resultGender");
    resultRace = document.querySelector("#resultRace");

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