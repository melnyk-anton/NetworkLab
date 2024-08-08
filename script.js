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

// script.js

document.addEventListener("DOMContentLoaded", function() {
    const prompts = [
        "Make a video of a feed advertisement.",
        "I want to advertise a page on Instagram",
        "Prepare a product presentation",
        "Make a review of new equipment",
        "Make a video about the company",
        "Prepare a user manual",
        "Make a video with customer reviews",
        "Prepare a promo for the event",
        "Make a video about services",
        "Make a video about promotions and discounts",
        "Make a commercial",
        "Prepare a video for YouTube",
        "Make a short teaser",
        "Make a video with experts",
        "Make a video with a product demonstration"

    ];

    const buttons = document.querySelectorAll('.promptButton');

    // Shuffle prompts array and select random prompts for buttons
    function getRandomPrompts(prompts, num) {
        let shuffled = prompts.sort(() => 0.5 - Math.random());
        return shuffled.slice(0, num);
    }

    let randomPrompts = getRandomPrompts(prompts, buttons.length);

    buttons.forEach((button, index) => {
        button.textContent = randomPrompts[index];
    });
});

