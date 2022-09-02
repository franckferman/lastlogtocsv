<div id="top"></div>

<div id="top" align="center">

[![Contributors][contributors-shield]](https://github.com/franckferman/lastlogtocsv/graphs/contributors)
[![Forks][forks-shield]](https://github.com/franckferman/lastlogtocsv/network/members)
[![Stargazers][stars-shield]](https://github.com/franckferman/lastlogtocsv/stargazers)
[![Issues][issues-shield]](https://github.com/franckferman/lastlogtocsv/issues)
[![MIT License][license-shield]](https://github.com/franckferman/lastlogtocsv/blob/main/LICENSE)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/franckferman)

</div>

<br />

<div align="center">
  <a href="https://github.com/franckferman/lastlogtocsv">
    <img src="https://raw.githubusercontent.com/franckferman/lastlogtocsv/main/img/logo.svg" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">lastlogtocsv</h3>

  <p align="center">
    Convert lastlog Linux file to CSV file, with Python 3.
    <br />
    <a href="https://github.com/franckferman/lastlogtocsv/blob/main/README.md"><strong>Explore the full documentation »</strong></a>
    <br />
    <br />
    <a href="https://asciinema.org/">View Demo</a>
    .
    <a href="https://github.com/franckferman/lastlogtocsv/issues">Report Bug</a>
    ·
    <a href="https://github.com/franckferman/lastlogtocsv/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#tested-on">Tested on</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![asciicast](https://asciinema.org/)](https://asciinema.org/)

This project was created for a specific need.

The lastlog file contains the last login times for system accounts. Login information is read from the file /var/log/lastlog.

lastlogtocsv allows the conversion of a lastlog file into a csv file.

<p align="right">(<a href="#top">back to top</a>)</p>

### Tested On

This program has been tested on different operating systems:
* - [x] [Microsoft Windows 11 Pro](https://www.microsoft.com/en-us/windows/get-windows-11), [Python 3](https://www.python.org/)
* - [x] [Debian 11](https://www.debian.org/), [Python 3](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This course is not intended to teach you how to use your Windows or Linux terminal or also Python. However, I will simply show you (for beginners) how to easily download my script and run it.

I don't think a tutorial would be very useful to teach you how to use the script as it was designed to be naturally intuitive, you should be able to find your way around quite easily.

### Prerequisites

* You can easily install my script with pip.
```sh
pip install lastlogtocsv
```

* If you do not wish to use pip to install my script, first of all you have to install the dependencies of my script.
 ```sh
pip install -r requirements.txt
```

Please note that my script must be placed where you want your machines to be stored.

* For example, on Windows, if you want them to be in your C:\ directory, issue the following command from your PowerShell terminal:
```sh
Start-BitsTransfer -Source https://raw.githubusercontent.com/franckferman/lastlogtocsv/lastlogtocsv/__main__.py -Destination "C:\" -DisplayName "lastlogtocsv - Downloading function - Franck FERMAN." -Description "Downloading the script."
```

Of course, you can change the desired destination path. To do this, you just have to change the argument of the -Destination parameter.

* For example:
```sh
Start-BitsTransfer -Source https://raw.githubusercontent.com/franckferman/lastlogtocsv/lastlogtocsv/__main__.py -Destination "D:\" -DisplayName "lastlogtocsv - Downloading function - Franck FERMAN." -Description "Downloading the script."
```

* For example, on Linux, if you want them to be in your home folder, issue the following command from your terminal:
```sh
curl https://raw.githubusercontent.com/franckferman/lastlogtocsv/lastlogtocsv/__main__.py -o ~/main.py
```

Of course, you can change the desired destination path. To do this, you just have to change the argument of the -o parameter.

* For example:
```sh
mkdir ./lastlogtocsv&&curl https://raw.githubusercontent.com/franckferman/lastlogtocsv/lastlogtocsv/__main__.py  -o ./lastlogtocsv/main.py
```

<!-- USAGE EXAMPLES -->
## Usage

* On Windows, to run the program, simply go to the program installation path and run the program:
```sh
Set-Location -Path "C:\";python.exe .\__main__.py
```

* If you have installed the script with pip, simply use the command:
```sh
python3 -m lastlogtocsv
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Project Link: [https://github.com/franckferman/lastlogtocsv](https://github.com/franckferman/lastlogtocsv)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/franckferman/lastlogtocsv.svg?style=for-the-badge
[contributors-url]: https://github.com/franckferman/lastlogtocsv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/franckferman/lastlogtocsv.svg?style=for-the-badge
[forks-url]: https://github.com/franckferman/lastlogtocsv/network/members
[stars-shield]: https://img.shields.io/github/stars/franckferman/lastlogtocsv.svg?style=for-the-badge
[stars-url]: https://github.com/franckferman/lastlogtocsv/stargazers
[issues-shield]: https://img.shields.io/github/issues/franckferman/lastlogtocsv.svg?style=for-the-badge
[issues-url]: https://github.com/franckferman/lastlogtocsv/issues
[license-shield]: https://img.shields.io/github/license/franckferman/lastlogtocsv.svg?style=for-the-badge
[license-url]: https://github.com/franckferman/lastlogtocsv/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/franckferman
[product-screenshot]: images/screenshot.png
