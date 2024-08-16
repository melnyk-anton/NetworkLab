document.getElementById('fetchVideoButton').addEventListener('click', async () => {
    try {
        videoElement.src = "https://static.videezy.com/system/resources/previews/000/037/474/original/circle_loading.mp4";
        document.getElementById('videoContainer').style.display = 'block';
        videoElement.play();
        const textField = document.getElementById('text');
        const response = await fetch('https://hook.eu2.make.com/7pbkrkwuqlcpme3d2hqb0mc3ytcinpsr', {
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
        if (data.videoUrl) {
            const videoElement = document.getElementById('videoElement');
            videoElement.loop = false;
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

    function getRandomPrompts(prompts, num) {
        let shuffled = prompts.sort(() => 0.5 - Math.random());
        return shuffled.slice(0, num);
    }

    let randomPrompts = getRandomPrompts(prompts, buttons.length);

    buttons.forEach((button, index) => {
        button.textContent = randomPrompts[index];

        button.addEventListener('click', async () => {
            try {
                const textField = document.getElementById('freeform');
                const response = await fetch('https://hook.eu2.make.com/7pbkrkwuqlcpme3d2hqb0mc3ytcinpsr', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ request: randomPrompts[index], content: textField.vale })
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
    });
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

function toggleMenu() {
    const sideMenu = document.querySelector('.side-menu');
    const openMenu = document.querySelector('.open-menu');

    sideMenu.classList.toggle('hidden');
    openMenu.classList.toggle('hidden');
}

document.querySelector('.close-menu').addEventListener('click', toggleMenu);
document.querySelector('.open-button').addEventListener('click', toggleMenu);

function myFunction(x) {
    x.classList.toggle("change");
    toggleMenu();
  }

