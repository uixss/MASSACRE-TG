# 📊 MASSACRE TG SESSIONS

This project automates reporting users, channels, and groups on Telegram using multiple sessions. It loads session credentials, user lists, and configuration files to perform reports based on predefined criteria.

## 🚀 Features

- **Multi-Session Management**: Supports multiple Telegram sessions for reporting.
- **Automated User and Channel Reports**: Reports users and channels with specified reasons.
- **Customizable Report Reasons**: Supports various report types like spam, fake, copyright, etc.
- **Randomized Messaging**: Randomized report messages for variation.
- **Error Handling**: Handles session errors like banned numbers and unauthorized access.

## 📂 Project Structure
```plaintext
📁 sessions/        # Stores session files
📄 vars.txt         # Pickled session credentials
📄 report.json      # Configuration for report messages and types
📄 main.json        # User list to report (ID and links)
📄 script.py        # Main script
```

## 🛠️ Setup and Installation

### Dependencies

```bash
pip install telethon tabulate
```

### Prepare Session Credentials
Create a `vars.txt` file with session credentials:
```plaintext
(api_id, api_hash, phone_number)
(api_id, api_hash, phone_number)
```

### Add Users to Report
Create a `main.json` file:
```json
[
  {
    "status": "success",
    "info": {
      "id": 123456789,
      "user": "@username"
    }
  }
]
```

### Configure Report Messages
Create a `report.json` file with report reasons and messages:
```json
{
  "SPAM": ["This is spam!", "Inappropriate content", "Unwanted messages"]
}
```

## 🏃 Usage
Run the script:
```bash
python script.py
```

The script will:
1. Validate all sessions.
2. Report users or channels based on `main.json`.
3. Display the results in a tabular format.

## 📈 Results
Reports will be displayed in the terminal as a table:
```
+-------------+-------------------+-----------+
| Session     | User/Channel      | Report    |
+-------------+-------------------+-----------+
| +1234567890 | @username         | SPAM      |
+-------------+-------------------+-----------+
```

## 📝 Notes
- Ensure that `vars.txt`, `main.json`, and `report.json` exist before running the script.
- Use valid Telegram API credentials for sessions.

<div style="display: flex; justify-content: space-between; align-items: center;">
    <img src="../img/term.png" alt="MASSACRE_SESSION" width="425" height="500">
    <img src="../img/table.jpg" alt="MASSACRE_SESSION2" width="400" height="500">
</div>


## ⚠️ Disclaimer
This tool is for educational purposes only. Use responsibly and ensure compliance with Telegram's terms of service.

## 🤝 Contributing
Feel free to submit issues or pull requests to improve the project!
