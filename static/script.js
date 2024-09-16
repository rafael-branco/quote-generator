document.addEventListener('DOMContentLoaded', () => {
    const generateButton = document.getElementById('generate');

    if (generateButton) {
        const spinner = generateButton.querySelector('.spinner-border');

        generateButton.addEventListener('click', () => {
            // Show spinner and disable button
            if (spinner) {
                spinner.style.display = 'inline-block';
            }
            generateButton.setAttribute('disabled', true); // Disable the button during loading

            fetch('/quote')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok: ' + response.statusText);
                    }
                    return response.json();
                })
                .then(data => {
                    if (Array.isArray(data) && data.length > 0) {
                        const quoteData = data[0];

                        const quoteElement = document.getElementById('quote');
                        const authorElement = document.getElementById('made-by');

                        if (quoteElement && quoteData.quote) {
                            quoteElement.textContent = quoteData.quote;
                        } else if (quoteElement) {
                            quoteElement.textContent = 'No quote available.';
                        }

                        if (authorElement && quoteData.author) {
                            authorElement.value = quoteData.author;
                        } else if (authorElement) {
                            authorElement.textContent = 'Unknown author.';
                        }
                    } else {
                        document.getElementById('quote').textContent = 'No quote data found.';
                    }
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                    const quoteDisplay = document.getElementById('quoteDisplay');
                    if (quoteDisplay) {
                        quoteDisplay.textContent = 'Failed to fetch quote.';
                    }
                })
                .finally(() => {
                    // Hide spinner and re-enable button
                    if (spinner) {
                        spinner.style.display = 'none';
                    }
                    generateButton.removeAttribute('disabled'); // Re-enable the button
                });
        });
    }
});
