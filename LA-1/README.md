<!--
**       .@@@@@@@*  ,@@@@@@@@     @@@     .@@@@@@@    @@@,    @@@% (@@@@@@@@
**       .@@    @@@ ,@@          @@#@@    .@@    @@@  @@@@   @@@@% (@@
**       .@@@@@@@/  ,@@@@@@@    @@@ #@@   .@@     @@  @@ @@ @@/@@% (@@@@@@@
**       .@@    @@% ,@@        @@@@@@@@@  .@@    @@@  @@  @@@@ @@% (@@
**       .@@    #@@ ,@@@@@@@@ @@@     @@@ .@@@@@@.    @@  .@@  @@% (@@@@@@@@
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">HTTP Client Lib. & App.</h3>

  <p align="center">
    A CLI application to make GET and POST requests.
    <br />
    <a href="https://github.com/Vaansh/COMP-445/blob/main/LA-1/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

- Python 3.8.5+

### Installation

1. Clone this repository or download the folder from [GitHub](https://github.com/Vaansh/COMP-445/tree/main/LA-1).

```zsh
git clone https://github.com/Vaansh/COMP-445.git
cd LA-1
```

## Usage

Run `python httpc/httpc.py` to run the application.

Examples:

```zsh
python httpc/httpc.py help (get | post)
python httpc/httpc.py get http://httpbin.org/status/418
python httpc/httpc.py get "http://httpbin.org/get?course=networking&assignment=1%27"
python httpc/httpc.py post "http://httpbin.org/post" -h Content-Type:application/json -f input.txt
python httpc/httpc.py post "http://httpbin.org/post" -h Content-Type:application/json -f input.txt \
       -v -o post-output-verbose.txt
```
