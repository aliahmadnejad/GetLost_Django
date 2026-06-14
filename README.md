# GetLost! — Backend API

> *The Django REST API powering the GetLost! backpacking hostel reservation platform.*

This is the server-side component of GetLost!, a same-day hostel reservation service for spontaneous travelers. It exposes REST endpoints consumed by the [Flutter mobile app](https://github.com/aliahmadnejad/GetLost_Flutter) and handles hostel listings, reservations, user accounts, and Stripe payment processing.

---

## What It Does

**Key Responsibilities**

- **Hostel listings** — serves real-time bed availability data
- **Reservations** — creates and manages same-day bookings
- **Stripe integration** — processes payments securely server-side
- **Group chat** — manages per-hostel chat rooms and user membership
- **Auth** — user registration, login, and session management

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | Django |
| Language | Python |
| Payments | Stripe API |
| Package Management | Pipenv |
| Frontend (Web) | JavaScript / HTML / CSS / SCSS |

---

## Related Repositories

- ⚙️ **This repo** — Django REST API backend
- 📱 [GetLost_Flutter](https://github.com/aliahmadnejad/GetLost_Flutter) — Flutter mobile client

---

## Getting Started

**Prerequisites:** Python 3, Pipenv, Stripe API keys

```bash
# Clone the repo
git clone https://github.com/aliahmadnejad/GetLost_Django.git
cd GetLost_Django

# Install dependencies
pipenv install -r requirements.txt

# Activate virtual environment
pipenv shell

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Add your Stripe keys and other environment variables to a `.env` file before running.

---

## Author

**Ali Ahmadnejad** · [Portfolio](https://aliahmadnejad.github.io) · [GitHub](https://github.com/aliahmadnejad)
