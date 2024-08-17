const generateVideoButton = document.getElementById('fetchVideoButton');
function changeToLoading() {
    const generateVideoDiv = document.getElementById('containerForButton');
    generateVideoDiv.innerHTML = '<button id="fetchVideoButton" class="fetchVideoButton" style="background-color:Red;"><span class="loader">L &nbsp; ading</span></button>';
}
function changeToRegenerate() {
    const generateVideoDiv = document.getElementById('containerForButton');
    generateVideoDiv.innerHTML = '<button id="fetchVideoButton" class="fetchVideoButton"><i class="fa fa-refresh" style="font-size:24px"></i> Regenerate</button>';
}
generateVideoButton.addEventListener('click', async () => {
    try {
        changeToLoading();
        const videoElement = document.getElementById('videoElement');
        const textField = document.getElementById('text');
        const response = await fetch('https://hook.eu2.make.com/1gsmoulbtrw9hwpdi7679oo8cmucyxra', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ request: 'getVideo', content: textField.value})
        });
        console.log(111);
        const data = await response.json();
        if (data.url) {
            changeToRegenerate();
            console.log(222);
            videoElement.loop = false;
            videoElement.src = data.url;
            document.getElementById('videoContainer').style.display = 'block';
            videoElement.play();
            console.log(333);
        } else {
            console.error('No video URL returned');
        }
    } catch (error) {
        console.error('Error fetching video:', error);
    }
});

function toggleMenu() {
    const sideMenu = document.querySelector('.side-menu');
    sideMenu.classList.toggle('hidden');
}


document.head.insertAdjacentHTML('beforeend', `
<style>
    .side-menu.hidden {
        transform: translateX(-100%);
        transition: transform 0.3s ease;
    }
</style>
`);


function myFunction(x) {
    x.classList.toggle("change");
    toggleMenu();
  }