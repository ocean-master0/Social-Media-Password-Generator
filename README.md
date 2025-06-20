# 🔐 Social Media Password Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

> **A sophisticated, enterprise-grade password generator specifically designed for social media platforms with platform-specific rules, real-time strength analysis, and professional PDF reporting capabilities.**

---

## 🌟 Live Demo

🔗 **[View Live Website](https://your-domain.com/password-generator)**

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Technologies Used](#-technologies-used)
- [🚀 Installation](#-installation)
- [📖 Usage](#-usage)
- [📁 Project Structure](#-project-structure)
- [🌐 Platform Support](#-platform-support)
- [🤝 Contributing](#-contributing)
- [👨‍💻 Author](#-author)
- [📄 License](#-license)
- [🆘 Support](#-support)

---

## ✨ Features

### 🎯 Core Features
- ✅ **20+ Social Media Platforms**  
- ✅ **Real-Time Strength Analysis**  
- ✅ **Custom Rule Engine**  
- ✅ **PDF Report Generation**  
- ✅ **Platform-Specific Optimization**  
- ✅ **85%+ Strength Guarantee**

### 🎨 Design Features
- 🖤 **Cyberpunk Theme**
- 📱 **Responsive Design**
- 🌙 **Dark Mode Ready**
- ♿ **Accessibility First**
- 🧑‍🎨 **High Contrast Text**

### 🔒 Security Features
- 🔐 **Cryptographically Secure**
- 🚫 **No Password Storage**
- 🛡️ **CSRF Protection**
- 🧰 **Input Validation**
- 🧠 **Pattern Detection**

### 🚀 Advanced Features
- 🎞️ **Micro-Interactions**
- 🧪 **Real-Time Validation**
- 📋 **Copy to Clipboard**
- 💻 **Progressive Web App**
- 🖨️ **Print Optimization**

---

## 🛠️ Technologies Used

### 🔙 Backend
- 🐍 Python 3.8+
- 🌐 Flask 2.3+
- 🧾 Flask-WTF
- 📄 ReportLab
- 🎲 Python Secrets

### 🎨 Frontend
- 🧱 HTML5
- 🎨 CSS3
- 🧠 JavaScript (ES6+)
- 🧩 Bootstrap 5
- ⭐ Font Awesome

### 🧰 Development Tools
- 🔧 Git
- 🖥️ VS Code
- 📦 Virtual Environment
- 🧪 Chrome DevTools

---

## 🚀 Installation

### 🔧 Prerequisites
- ✅ Python 3.8 or higher  
- ✅ pip  
- ✅ Git  

### ⚡ Quick Start


# Clone the Repository
git clone https://github.com/ocean-master0/Social-Media-Password-Generator.git

# Create Virtual Environment
python -m venv password_generator_env

# Activate Environment
# Windows:
password_generator_env\Scripts\activate
# macOS/Linux:
source password_generator_env/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Run the Application
python app.py


📂 Visit: `http://localhost:5000`




---

## 📖 Usage

### 👣 Basic Steps

1. 🔘 **Select Platform**
2. ⚙️ **Configure Settings**
3. 🔁 **Generate Password**
4. 📥 **Download Report**

---

## 📁 Project Structure

```
social-media-password-generator/
│
├── app.py                        # Main Flask application
├── requirements.txt              # Dependencies
├── README.md                     # Project documentation
├── LICENSE                       # MIT License
│
├── templates/
│   └── index.html                # HTML UI
│
├── static/
│   ├── css/styles.css            # Cyberpunk styles
│   ├── js/password.js            # JS logic
│   ├── images/favicon.ico        # App favicon
│   └── fonts/                    # Fonts (optional)
│
├── utils/
│   ├── __init__.py
│   ├── password_rules.py         # Rules per platform
│   ├── password_generator.py     # Generation logic
│   └── pdf_generator.py          # PDF utilities
│
├── config/
│   └── settings.py               # App config
```

---

## 🌐 Platform Support

| Platform  | Min Length | Max Length | Requirements                 | Status |
| --------- | ---------- | ---------- | ---------------------------- | ------ |
| Facebook  | 14         | 50         | All character types          | ✅      |
| Instagram | 15         | 30         | Mixed case, numbers, symbols | ✅      |
| Twitter/X | 18         | 50         | Advanced security patterns   | ✅      |
| LinkedIn  | 16         | 200        | Professional security        | ✅      |
| YouTube   | 20         | 100        | Enterprise-grade             | ✅      |
| TikTok    | 17         | 25         | High security                | ✅      |
| WhatsApp  | 16         | 64         | Enterprise security          | ✅      |
| Snapchat  | 15         | 50         | Comprehensive protection     | ✅      |
| Pinterest | 14         | 100        | Strict character mixing      | ✅      |
| Reddit    | 19         | 128        | Ultra-high security          | ✅      |
| Discord   | 16         | 72         | Gaming security              | ✅      |
| Telegram  | 18         | 256        | Maximum encryption           | ✅      |
| Twitch    | 15         | 60         | Streaming security           | ✅      |
| Spotify   | 16         | 80         | Premium security             | ✅      |
| Netflix   | 17         | 70         | Entertainment platform       | ✅      |
| Amazon    | 20         | 100        | Financial-grade              | ✅      |
| Google    | 22         | 100        | Enterprise maximum           | ✅      |
| Microsoft | 21         | 120        | Corporate-grade              | ✅      |
| Apple     | 20         | 90         | Premium device protection    | ✅      |
| Custom    | 4          | 128        | User-defined rules           | ✅      |

---

### 🔐 Authentication

No authentication required.

### 📈 Rate Limiting

* 100 requests/minute/IP
* 1000 requests/hour/IP

### 🚫 Error Codes

* `400` – Invalid input
* `429` – Too many requests
* `500` – Server error

---

## 🤝 Contributing

We welcome contributions!
📄 See our [Contributing Guidelines](CONTRIBUTING.md) for more.

### 🧪 Development Setup


# Submit pull request


### ✍️ Code Style

* 🧼 Follow PEP 8
* 📚 Meaningful naming
* 💬 Add comments
* 🧪 Write tests



## 👨‍💻 Author

**\[Abhishek Kumar]**
🐙 GitHub: [@ocean-master0](https://github.com/ocean-master0)



## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.



## 🆘 Support

If you find any issues or need help, feel free to [open an issue](https://github.com/ocean-master0/Social-Media-Password-Generator/issues) or contact the maintainer.

