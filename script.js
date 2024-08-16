document.getElementById('fetchVideoButton').addEventListener('click', async () => {
    try {
        const videoElement = document.getElementById('videoElement');
        videoElement.src = "https://static.videezy.com/system/resources/previews/000/037/474/original/circle_loading.mp4";
        document.getElementById('videoContainer').style.display = 'block';
        videoElement.play();
        const textField = document.getElementById('text');
        const response = await fetch('https://hook.eu2.make.com/1gsmoulbtrw9hwpdi7679oo8cmucyxra', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ request: 'getVideo', content: textField.value})
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        if (data.url) {
            videoElement.loop = false;
            videoElement.src = data.url;
            document.getElementById('videoContainer').style.display = 'block';
            videoElement.play();
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