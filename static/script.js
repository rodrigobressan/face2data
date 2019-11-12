function get_prediction(image) {
    const formData = new FormData()
    formData.append('image', image);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(response => {
        response.json().then(data => {

            if (response.status == 200) {
                console.log(data['age'])
                let age = data['age']
                console.log(age)
                let gender = data['gender']
                let race = data['race']

                age = age < 0 ? 1 : age
                age = age > 100 ? 100 : age

                const text = `It seems that the provided picture is related to a <b>${race} ${gender}</b>, around its <b>${age} years old</b>.` +
                '<br/><br/>Take note that these predictions may not be perfectly accurate due to the small amount of samples used for training (around 20k). In case you find any issues, feel free to open an issue on the project repository.'

                resultsText.innerHTML = text;
             } else if (response.status == 400) {
                resultsText.innerHTML = '<h2>There was an error processing your request. Make sure you provided a valid image and try again.</h2>'
                imageContainer.style.visibility = 'hidden'
             }

        });
    })
    .catch(error => {
        resultsText.innerHTML = 'There was an error on your request. Please try again'
    });
}

function imageUploaded(event) {
    const target = event.target;
    const image = target.files[0];

    if (!image) return;

    resultsText.innerHTML = "";

    imageContainer.style.visibility = 'visible'
    imageContainer.src = window.URL.createObjectURL(image);

    get_prediction(image);
}

function ready() {
    resultsText = document.querySelector("#results_text");

    imageContainer = document.querySelector("#imageContainer");

    const inputFile = document.querySelector("#image");
    inputFile.addEventListener('change', imageUploaded);
}

document.addEventListener("DOMContentLoaded", ready);

let imageContainer;
let imageClass;
let imageConfidence;