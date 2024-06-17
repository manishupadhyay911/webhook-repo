# GitHub Actions Webhook Listener

This project consists of two repositories: `action-repo` and `webhook-repo`. The `action-repo` is a GitHub repository configured to send webhooks on specific GitHub events (push, pull request, and merge). The `webhook-repo` contains the code to handle these webhooks, store event data in MongoDB, and display the events on a web page.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
  - [Webhook Repository Setup](#webhook-repository-setup)
  - [GitHub Webhook Setup](#github-webhook-setup)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Overview

The `webhook-repo` is a Flask application that listens for GitHub webhook events, stores them in MongoDB, and displays the events in real-time on a web page. The application supports the following GitHub actions:

- Push
- Pull Request
- Merge

## Setup

### Webhook Repository Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/webhook-repo.git
    cd webhook-repo
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Flask application:**

    ```bash
    python app.py
    ```

    The application will be running at `http://127.0.0.1:5000/`.

5. **Ensure MongoDB is running:**

    - Make sure you have MongoDB installed and running on your machine. The Flask application expects MongoDB to be accessible at `mongodb://localhost:27017/`.

### GitHub Webhook Setup

1. **Go to your GitHub repository (`action-repo`) settings.**

2. **Navigate to the "Webhooks" section and click "Add webhook".**

3. **Enter the Payload URL:**

    ```
    http://your-server-address:5000/webhook
    ```

4. **Select content type as `application/json`.**

5. **Select individual events or choose to send `Just the push event` to test.**

6. **Click "Add webhook".**

## Usage

1. **Push Event:**

    - When you push changes to any branch of the `action-repo`, a push event is sent to the webhook, and the event is stored in MongoDB.

    - Example message:
        ```
        {author} pushed to {to_branch} on {timestamp}
        ```

2. **Pull Request Event:**

    - When you create a pull request in the `action-repo`, a pull request event is sent to the webhook, and the event is stored in MongoDB.

    - Example message:
        ```
        {author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}
        ```

3. **Merge Event:**

    - When a pull request is merged in the `action-repo`, a merge event is sent to the webhook, and the event is stored in MongoDB.

    - Example message:
        ```
        {author} merged branch {from_branch} to {to_branch} on {timestamp}
        ```

4. **View Events:**

    - Navigate to `http://127.0.0.1:5000/` to see the events displayed in real-time.


## Dependencies

- Flask
- pymongo

You can install the required dependencies using the command:

```bash
pip install -r requirements.txt


