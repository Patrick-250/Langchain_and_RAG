# AI Restaurant Search and Booking Agent

An intelligent restaurant discovery assistant built with LangChain, MCP tools, and Streamlit.
The agent helps users find restaurants based on their preferences such as location, cuisine, and availability, and can assist with making reservations.

The system combines a language model with external tools to reason about user requests and retrieve relevant information.

---

## Features

* **Agent-based reasoning** using a ReAct-style workflow
* **Restaurant search** based on location, cuisine, and availability
* **Tool integration**

  * MCP tools for restaurant data and reservations
  * Tavily search for additional online information
* **Streamlit interface** for interacting with the agent
* **Async tool execution** for handling MCP tools efficiently

---

## Technology Stack

* Python
* LangChain
* LangGraph-style agents
* Model Context Protocol (MCP)
* OpenAI models
* Tavily Search
* Streamlit
* AsyncIO

---

## Project Structure

```
app/
│
├── main.py          # Streamlit application
├── .env             # Environment variables
└── requirements.txt # Project dependencies
```

---

## Installation

### 1. Clone the repository

```
git clone <repository-url>
cd app
```

### 2. Create a virtual environment

```
python -m venv venv
```

Activate the environment.

**Windows**

```
venv\Scripts\activate
```

**macOS / Linux**

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```


## Environment Variables

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Running the Application

Start the Streamlit application:

```
streamlit run main.py
```


## Example Queries

Users can ask questions such as:

* Find Italian restaurants in Chicago tonight
* Show sushi restaurants near downtown
* Recommend highly rated restaurants in New York
* Find a romantic restaurant and make a reservation for two people

---

## System Workflow

1. The user enters a request through the Streamlit interface.
2. The AI agent interprets the request using a language model.
3. The agent determines which tools should be used.
4. MCP tools or Tavily search retrieve relevant information.
5. The agent synthesizes the results and returns a response.

---


## work in progress

* Integration with a restaurant database using retrieval-augmented generation (RAG)
* Integration with real reservation APIs
* User authentication
* Conversation memory
* Automatic location detection
* Improved interface and filtering options
* Deployment using Docker or cloud infrastructure

---


## Author

Patrick Tuyiringire
