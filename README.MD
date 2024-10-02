# Photos App

**A Django app to share photo shoots with your customers**

[![Deploy to Production](https://github.com/LuisHCK/photos-app/actions/workflows/deploy.yml/badge.svg)](https://github.com/LuisHCK/photos-app/actions/workflows/deploy.yml)

## Overview

`Photos` is a web application built using the Django framework that helps photographers manage and share their photo shoots with clients. It features a clean, user-friendly interface and a secure system for delivering photos to customers. The app enables easy customization, management, and sharing, making it an ideal solution for professional photographers.

## Stack

-   **Backend**: Django 5
-   **Database**: PostgreSQL
-   **Frontend**: Bulma CSS
-   **Containerization**: Docker

## Features

-   **Customizable Homepage**  
    Create a personalized homepage to showcase your brand and services.

-   **Admin Dashboard to Manage Photo Shoots**  
    Manage your photo shoots, upload new images, and track customer interactions through an intuitive dashboard.

-   **Share Secure Links with Customers**  
    Generate unique, secure links for each photo shoot to share with your customers. Only those with the link can access the images.

-   **Expiration Time for Photo Shoots**  
    Set an expiration time for each photo shoot. After the specified time, the photos will be erased from the server to save space, and the link will become inaccessible.

-   **Download All Photos with a Single Click**  
    Customers can download all their photos at once, making it convenient to get access to their entire album.

## Getting Started

### Prerequisites

Make sure you have the following installed:

-   Docker
-   Docker Compose

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/photos.git
    cd photos
    ```

2. Copy the `.env.example` file to `.env` and update the configuration values as needed

3. Build and start the application using Docker Compose:

    ```bash
    docker-compose up --build
    ```

4. The application will be available at `http://localhost:8000`.

## Contributing

Feel free to open issues and submit pull requests. Contributions are welcome!

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the Django, PostgreSQL, Bulma, and Docker communities for their amazing work and support.
