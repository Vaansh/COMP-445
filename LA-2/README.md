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
  <h3 align="center">HTTP File Server.</h3>

  <p align="center">
    A file server application.
    <br />
    <a href="https://github.com/Vaansh/COMP-445/blob/main/LA-2/README.md"><strong>Explore the docs »</strong></a>
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

- Python 3.10.2+

### Installation

1. Clone this repository or download the folder from [GitHub](https://github.com/Vaansh/COMP-445/tree/main/LA-2).

```zsh
git clone https://github.com/Vaansh/COMP-445.git
cd LA-2
```

## Usage

Run `python httpfs/httpfs.py` to run the application.

Examples:

Server:

```zsh
python httpfs/httpfs.py -v
```

Client:

```zsh
python httpc/httpc.py get "http://localhost:8080" -v
python httpc/httpc.py get "http://localhost:8080/dir/get.txt" -v
python httpc/httpc.py post "http://localhost:8080/post.txt" -v -f input.txt
python httpc/httpc.py post "http://localhost:8080/dir/post.txt" -v -f input.txt
python httpc/httpc.py post "http://localhost:8080/dir/dir/test.txt" -v -f input.txt
```
