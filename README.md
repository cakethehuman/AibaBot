# AibaBot

AibaBot is a guide bot developed to assist members of **UKM Soushin — Tarumanagara Nihonbu** by providing information and guidance related to the organization.

## Intended Users

- **Organization:** UKM Soushin — Tarumanagara Nihonbu
- **Purpose:** Organizational guidance and information assistance

## Getting Started

Follow these steps to set up and run AibaBot locally.

### Prerequisites

Make sure you have the following installed:

- Python
- Docker
- Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AibaBot
```

Replace `<repository-url>` with your repository's URL.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Use `.env.example` as a reference to create your own `.env` file.

```bash
cp .env.example .env
```

Fill in the required environment variables in `.env` before running the application.

**Important:** Never commit your `.env` file or expose API keys and other sensitive credentials.

### 4. Run with Docker

Run the Docker image using your environment variables:

```bash
docker run --env-file .env <image-name>
```

Replace `<image-name>` with the name of your Docker image.

If you are building the image locally, run:

```bash
docker build -t aibabot .
docker run --env-file .env aibabot
```

## Project Structure

The project structure may vary depending on the implementation. A typical layout could look like this:

```text
AibaBot/
├── backend/
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## License

No license has been specified yet. Please contact the repository owner for information about usage and distribution.
