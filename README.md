# NewsAI Agent

![Project Logo](link-to-your-logo.png)

> An intelligent NewsAI agent that searches the internet and generates insightful blog content.

## Table of Contents

- [Project Name](#newsai-agent)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Technology Stack

The NewsAI Agent leverages the following technologies:

- **CrewAI**: An AI-driven tool for managing and analyzing data.
- **Gemini**: A platform for advanced AI and machine learning tasks.
- **Serper API**: A tool for searching and retrieving internet data.
- **Python**: The programming language used to build and run the application.

## Getting Started

These instructions will help you set up the NewsAI Agent on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your local machine:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

Follow these steps to set up the project:

1. **Clone the repository**
   ```sh
   git clone https://github.com/MuhammadIsmail-khan/GenAI_Agents.git

2. **Change directory to the project folder**
   ```sh
   cd GenAI_Agents
   ```
3. **Create a virtual environment**
   ```sh
   python -m venv env
   ```
4. **Activate the virtual environment**

   For Windows:
   ```sh
   .\env\Scripts\activate
   ```

   For macOS/Linux:
   ```sh
   source env/bin/activate
   ```
5. **Install the required packages**
   ```sh
   pip install -r requirements.txt
   ```

6. **Create a `.env` file and add your API keys**
   ```sh
   touch .env
   ```
   Then add the following lines to the `.env` file:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

## Usage

To use the NewsAI Agent:

1. Ensure the virtual environment is activated.
2. Run the agent to start searching for news and generating blog content.
   ```sh
   python newsai_agent.py
   ```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Ismail Khan - [@MuhammadIsmail-khan](https://github.com/MuhammadIsmail-khan) - m.ismail110022@gmail.com

Project Link: [https://github.com/MuhammadIsmail-khan/GenAI_Agents](https://github.com/MuhammadIsmail-khan/GenAI_Agents)
