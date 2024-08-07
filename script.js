document.getElementById('fetchVideoButton').addEventListener('click', async () => {
    try {
        const response = await fetch('https://hook.eu2.make.com/h8ueajp60sdylqzom9codc8e5o4ajado', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ request: 'getVideo' })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        if (data.videoUrl) {
            const videoElement = document.getElementById('videoElement');
            videoElement.src = data.videoUrl;
            document.getElementById('videoContainer').style.display = 'block';
            videoElement.play();
        } else {
            console.error('No video URL returned');
        }
    } catch (error) {
        console.error('Error fetching video:', error);
    }
});
