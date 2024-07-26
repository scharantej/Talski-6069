## Flask Application Design

### HTML Files
- **index.html**: The main page of the application.
    - Content:
        - A heading for the application's title.
        - A Bootstrap form with a textarea to enter the English flashcards and a button to submit them.
        - A div to display the translated Dutch flashcards.

### Routes
- **index**: The route that handles the main page.
    - When a GET request is made to this route, it will render the **index.html** file.
- **translate**: The route that handles the translation of the flashcards.
    - When a POST request is made to this route, it will take the English flashcards from the request form, translate them to Dutch using an external API or dictionary, and return the translated Dutch flashcards in the response.