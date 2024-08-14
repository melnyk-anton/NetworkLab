function myFunction(x) {
  x.classList.toggle("change");
}

document.getElementById('fetchVideoButton').addEventListener('click', async () => {

  try {
      const textField = document.getElementById('text');
      const response = await fetch('https://hook.eu2.make.com/5nwzg8e6bvj1997v4iickjmnnsgkexat', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ request: 'getImages', content: textField.value})
      });

      if (!response.ok) {
          throw new Error('Network response was not ok');
      }

      const data = await response.json();
      if (data.image1) {
        localStorage.setItem('image1', data.image1);
        localStorage.setItem('image2', data.image2);
        localStorage.setItem('image3', data.image3);
        localStorage.setItem('image4', data.image4);
        localStorage.setItem('text1', data.text1);
        localStorage.setItem('text2', data.text2);
        localStorage.setItem('text3', data.text3);
        localStorage.setItem('text4', data.text4);
        window.location = 'secondStep.html';
      } else {
          console.error('No video URL returned');
      }
  } catch (error) {
      console.error('Error fetching video:', error);
  }

});
document.getElementById('moveToThirdStep').addEventListener('click', async () => {
  window.location = 'thirdStep.html';
});


