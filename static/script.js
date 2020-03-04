function make_pie_plot(results, div_to_plot, title) {
    var data = [{
        values: Object.values(results),
        labels: Object.keys(results),
        type: 'pie',
        textfont: {
            family: 'sans serif',
            size: 14,
            color: '#FFFFFF'
        }
    }];

    var layout = {
        paper_bgcolor: "rgba(0,0,0,0)",
        width: 500,
        height: 500,
        plot_bgcolor: "rgba(0,0,0,0)",
        title: {
            text: title,
            font: {
             size: 20,
                color: '#FFFFFF'
            }
        },
        showlegend: true,
        legend: {
            font: {
                size: 14,
                color: '#FFFFFF'
            }
        }
    }

    Plotly.newPlot(div_to_plot, data, layout, {showSendToCloud: true});
}

function scrollTo(element, to, duration) {
    if (duration <= 0) return;
    var difference = to - element.scrollTop;
    var perTick = difference / duration * 10;

    setTimeout(function() {
        element.scrollTop = element.scrollTop + perTick;
        if (element.scrollTop === to) return;
        scrollTo(element, to, duration - 10);
    }, 10);
}

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
                make_pie_plot(data['race'], 'race_plot', 'Race')
                make_pie_plot(data['gender'], 'gender_plot', 'Gender')

                results_div = document.getElementById("results");
                scrollTo(document.documentElement, results_div.offsetTop, 600);

                let age = data['age']
                let min_age = age - 10
                let max_age = age
                resultsText.innerHTML = 'The predictions may not be perfectly accurate due to the small number of samples used for training (around 20 thousand images).';
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
    resultsText = document.querySelector("#age_text");

    imageContainer = document.querySelector("#imageContainer");

    const inputFile = document.querySelector("#image");
    inputFile.addEventListener('change', imageUploaded);
}

document.addEventListener("DOMContentLoaded", ready);

let imageContainer;
let imageClass;
let imageConfidence;

