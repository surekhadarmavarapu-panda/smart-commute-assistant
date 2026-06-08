## Smart Commute Assistant Agent

Smart Commute Assistant is a CLI-based Python project that helps users plan their daily commute using calendar, traffic, and weather data. It works as an agent that calls tools, reasons over results, and gives recommendations.

## Objective
* Understand user questions
* Use tools (calendar, traffic, weather)
* Process data
* Give commute suggestions

### How to Clone
`git clone https://github.com/surekhadarmavarapu-panda/smart-commute-assistant.git `

`cd smart-commute-assistant`

### Environment Setup
Before running the project, set your Gemini API key:

` export GEMINI_API_KEY="your_api_key_here"`

### How to Run

`python main.py --userid [user1/user2/user3]`

#### Optional

`python main.py --userid user2 --source Hyderabad --destination Bangalore

### Valid Users
* [user1 , user2 , user3]

### Example

#### Input:

` What time should I leave for work today? `

#### Output:

Recommended leave time based on calendar, traffic, and weather

### Run Tests
`pytest -v`

If import issue:

`PYTHONPATH=$(pwd) pytest -v`



