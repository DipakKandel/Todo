# 🚀 Todo App - Django Full-Stack Application

A modern, feature-rich todo application built with Django, featuring user authentication, AI-powered summaries, and a responsive Bootstrap UI. Perfect for showcasing full-stack development skills.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## ✨ Features

### 🔐 User Management

- **User Registration & Authentication** - Secure login system with custom user model
- **Guest Mode** - Use the app without registration (tasks saved in browser session)
- **Session Management** - Persistent data for registered users across devices

### 📝 Task Management

- **Add Tasks** - Quick task creation with real-time updates
- **Edit Tasks** - Inline editing with modal interface
- **Mark Complete** - One-click task completion
- **Delete Tasks** - Remove unwanted tasks
- **Revert Tasks** - Move completed tasks back to todo list
- **Smart Ordering** - New tasks appear at the top of the list

### 🤖 AI Integration

- **OpenAI GPT-3.5 Turbo** - AI-powered daily task summaries
- **Smart Analysis** - Automatic insights about your productivity
- **Error Handling** - Graceful fallback when AI service is unavailable

### 🎨 Modern UI/UX

- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Bootstrap 5** - Modern, clean interface with glass morphism effects
- **Real-time Updates** - Instant feedback for all user actions
- **Accessibility** - Proper ARIA labels and keyboard navigation

## 🛠️ Technologies Used

### Backend

- **Django 5.2.4** - Full-stack web framework
- **Python 3.x** - Core programming language
- **SQLite** - Lightweight database
- **Django ORM** - Database abstraction layer

### Frontend

- **HTML5/CSS3** - Semantic markup and styling
- **Bootstrap 5** - Responsive UI framework
- **JavaScript** - Interactive functionality
- **Font Awesome** - Professional icons

### AI & APIs

- **OpenAI API** - GPT-3.5 Turbo for intelligent summaries
- **Environment Variables** - Secure API key management

### Development Tools

- **Git** - Version control
- **CSRF Protection** - Security measures
- **Session Management** - User state handling

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/DipakKandel/Todo.git
   cd Todo
   ```

2. **Create virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:

   ```env
   SECRET_KEY=your-secret-key-here
   OPENAI_API_KEY=your-openai-api-key-here  # Optional for AI summaries
   ```

5. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

## 📱 Usage

### Guest Mode

- Start using the app immediately without registration
- Tasks are saved in your browser session
- Perfect for quick task management

### Registered Users

- Create an account for permanent task storage
- Access your tasks from any device
- Enjoy AI-powered daily summaries

## 🔧 Configuration

### Environment Variables

| Variable         | Description                     | Required |
| ---------------- | ------------------------------- | -------- |
| `SECRET_KEY`     | Django secret key               | Yes      |
| `OPENAI_API_KEY` | OpenAI API key for AI summaries | No       |

### Database

The app uses SQLite by default, which is perfect for development and small deployments. For production, consider using PostgreSQL or MySQL.

## 🏗️ Project Structure

```
Todo/
├── accounts/          # User authentication app
├── tasks/            # Task management app
├── todo_main/        # Main project settings
├── templates/        # HTML templates
├── static/          # Static files (CSS, JS, images)
├── requirements.txt  # Python dependencies
└── manage.py        # Django management script
```

## 🔒 Security Features

- **CSRF Protection** - Cross-site request forgery protection
- **User Authentication** - Secure login system
- **Input Validation** - Proper form validation and sanitization
- **SQL Injection Protection** - Django ORM prevents SQL injection
- **XSS Protection** - Template escaping prevents XSS attacks

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

## 🚀 Deployment

### Local Development

```bash
python manage.py runserver
```

### Production Deployment

1. Set `DEBUG = False` in settings.py
2. Configure your production database
3. Set up a production WSGI server (Gunicorn, uWSGI)
4. Configure your web server (Nginx, Apache)
5. Set up environment variables securely

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Dipak Kandel**

- GitHub: [@DipakKandel](https://github.com/DipakKandel)
- LinkedIn: [Your LinkedIn]
- Portfolio: [Your Portfolio]

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive UI framework
- OpenAI for the AI integration capabilities
- Font Awesome for the beautiful icons

---

⭐ **Star this repository if you found it helpful!**

🔗 **Live Demo**: [Add your deployed link here]

📧 **Contact**: [Your email]
