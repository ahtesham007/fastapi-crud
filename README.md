<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="Logo">
  </a>

<h3 align="center">FastAPI - Backend Architecture Template</h3>

  <p align="center">
    A complete comprehensive Rest API template for developing projects using FastAPI
    <br />

  </p>
</div>

<!-- TABLE OF CONTENTS -->
<!-- 

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details> 
-->



<!-- ABOUT THE PROJECT -->
# About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This project is a RESTful API for creating, reading, updating, and deleting user posts. It is built using Python and the following frameworks and libraries: FastAPI, Pydantic, SQLAlchemy, Alembic, and JWT auth.

 The API endpoints allow users to create an account, authenticate, and create, read, update, and delete posts. Users can also like and dislike posts.
 <!--`github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description` -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python 3.10
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* JWT Authentication
<!-- * [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url] -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

<!-- This is an example of how to list things you need to use the software and how to install them. -->
<!-- * npm
  ```sh
  npm install npm@latest -g
  ``` -->

  - Python 3.10
  - pip
  - Git
  - MySQL
  - Docker (If using docker image)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ahtesham007/fastapi-crud
   ```
2. Change directory to the project:
   ```sh
   cd fastapi-crud
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
# Usage

1. Run the APP:
   ```sh
   uvicorn app.main:app --reload
   ```
2. The API will be running at http://localhost:8000.
3. Use an API client (such as Postman) to interact with the API.



## Docker Image

From the Root directory:

1. Build Image and Start the container:
   ```sh
   docker-compose -f docker-compose.dev.yml up -d
   ```

## Test the APP

From the Root directory:

1. Install Pytest:
   ```sh
   pip install pytest
   ```

2. Test the app
   ```sh
   pytest
   ```

## API Endpoints

After running the app:

Check the API docs: http://localhost:8000/docs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Learning
If you are new to any of the tools or frameworks used in this project, the following resources can be helpful:

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Pydantic documentation](https://pydantic-docs.helpmanual.io/)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/)
- [Alembic documentation](https://alembic.sqlalchemy.org/)
- [JWT documentation](https://jwt.io/)

<!-- CONTACT -->
## Contact

Ahtesham Zaidi - [LinkedIn](https://www.linkedin.com/in/ahtesham-zaidi/) - zsyedahtesham@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ahtesham007/fastapi-crud.svg?style=for-the-badge
[contributors-url]: https://github.com/ahtesham007/fastapi-crud/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ahtesham007/fastapi-crud.svg?style=for-the-badge
[forks-url]: https://github.com/ahtesham007/fastapi-crud/network/members
[stars-shield]: https://img.shields.io/github/stars/ahtesham007/fastapi-crud.svg?style=for-the-badge
[stars-url]: https://github.com/ahtesham007/fastapi-crud/stargazers
[issues-shield]: https://img.shields.io/github/issues/ahtesham007/fastapi-crud.svg?style=for-the-badge
[issues-url]: https://github.com/ahtesham007/fastapi-crud/issues
[license-shield]: https://img.shields.io/github/license/ahtesham007/fastapi-crud.svg?style=for-the-badge
[license-url]: https://github.com/ahtesham007/fastapi-crud/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ahtesham-zaidi

<!-- [Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com  -->
