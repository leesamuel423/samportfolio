# Sam Portfolio Site

## Prerequisites

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install [Docker Compose](https://docs.docker.com/compose/install/)

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/samportfolio.git
cd samportfolio
```

2. Create a `.env` file in the project root:

```
DB_HOST=mysql
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database_name
```

3. Build and start the containers:

```bash
docker compose up -d --build
```

4. Verify the containers are running:

```bash
docker ps
```

You should see containers for both the web application and MySQL running.

## Usage

Once the containers are running, you can access:

- The website at `http://localhost:5001`
- The database at `localhost:3306` (if you need to connect externally)

### Viewing Logs

To see application logs:

```bash
docker compose logs app
```

To see database logs:

```bash
docker compose logs mysql
```

### Troubleshooting

If you encounter issues:

1. Check container status:

```bash
docker ps
docker compose ps
```

2. Check logs for errors:

```bash
docker compose logs
```

3. Restart the services:

```bash
docker compose down
docker compose up -d --build
```

## Production Deployment

For production deployment:

```bash
./redeploy-site.sh
```
