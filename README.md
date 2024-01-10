# Django Music Player

Django Music Player is an open-source web application built with Django that allows users to upload, manage, and play music files. With this application, users can create playlists, search for songs, and enjoy their favorite music.

## Features

- User authentication: Users can create accounts, log in, and manage their own music library.
- Music Upload: Users can upload their music files and add them to their library.
- Playlists: Users can create and manage playlists, add songs to playlists, and play songs from the playlists.
- Song Search: Users can search for songs by title, artist, or album.
- Responsive Design: The application is designed to be responsive and compatible with different screen sizes.

## Installation

1. Clone the repository:

   
bash
   git clone https://github.com/reza72rg/Django-MusicPlayer.git
   
2. Change into the project directory:

   
bash
   cd django-music-player
   
3. Create a virtual environment:

   
bash
   python -m venv env
   
4. Activate the virtual environment:

   - On macOS and Linux:

     
bash
     source env/bin/activate
     
   - On Windows:

     
bash
     .\env\Scripts\activate
     
5. Install the project dependencies:

   
bash
   pip install -r requirements.txt
   
6. Apply database migrations:

   
bash
   python manage.py migrate
   
7. Start the development server:

   
bash
   python manage.py runserver
   
8. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Contributing

Contributions to the Django Music Player project are welcome! If you discover any bugs or have suggestions for new features, please open an issue or submit a pull request on the GitHub repository.

Before contributing, please review the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

