# Weather Notification System

A Python script that uses the OpenWeatherMap API to check for rain forecasts and sends SMS alerts using Twilio.

## 🌦️ Features
- **Weather Forecast:** Fetches the next 4 weather updates for your location.
- **Rain Alert:** Sends SMS alerts if rain is predicted.
- **SMS Integration:** Uses Twilio to deliver weather notifications directly to your phone.

## 🛠️ Tech Stack
- **Python 3**
- **Requests Library**
- **Twilio API**
- **OpenWeatherMap API**

## 📦 Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Weather-Notifier.git
   cd Weather-Notifier
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys:**
   - Get an API key from [OpenWeatherMap](https://openweathermap.org/api).
   - Sign up for a [Twilio](https://www.twilio.com/) account and get your Account SID and Auth Token.

## 💡 Usage
1. **Configure the Script:**
   - Replace the placeholders for `API_KEY`, `account_sid`, `auth_token`, `MY_LAT`, and `MY_LONG` with your actual credentials.

2. **Run the Script:**
   ```bash
   python weather_notifier.py
   ```

## 📋 Requirements
- Python 3.x
- Requests
- Twilio

## 📜 License
This project is licensed under the MIT License.

---
**Stay Updated with the Weather! 🌦️**

