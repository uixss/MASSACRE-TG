# 📊 Telegram Reporter

Telegram Reporter is an advanced tool for automating reports on Telegram, using multiple sessions and proxies to improve efficiency and avoid blocks. This tool is ideal for handling large volumes of reports while minimizing the risk of restrictions and account blocks by Telegram.

## 🚀 Features

- ✅ **Automated Reports**: Automatically sends reports to Telegram users, groups, or channels, allowing selection of different reasons for reporting, such as spam, copyright infringement, false content, and more.
- 🌐 **Proxy Management**: Uses HTTP, HTTPS, and SOCKS proxies to avoid IP restrictions and ensure anonymity during the reporting process. Proxies are automatically verified to ensure only valid ones are used.
- 🔄 **Session Rotation**: Allows rotation of multiple Telegram sessions to minimize the risk of account blocks, distributing reports among several accounts.
- 📋 **Detailed Reports**: Retrieves detailed information about the target channels, groups, or users, including the number of members, administrators, and other relevant details.
- ⏱️ **Frequency Control**: Adjusts the delay between each report to avoid errors from exceeding usage limits (Flood Wait).
- 👥 **Entity Differentiation**: Identifies if the target is a channel, group, or user and adapts the reporting logic accordingly. If the target is a channel or group, administrators are also reported in addition to messages.

## 🔧 Internal Functionality

Telegram Reporter implements a system based on the following logic:

| Feature                     | Description                                                                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Session Loading**         | Telegram sessions are loaded from a `vars.txt` file, allowing the use of multiple accounts to distribute the reports.                           |
| **Proxy Management**        | The tool obtains proxies from services like `proxyscrape.com`, which are verified before use to ensure quality.                                  |
| **Automated Reporting**     | Uses `Telethon` to connect to Telegram and send reports to users, groups, or channels with different available reporting reasons.                 |
| **Session and Proxy Rotation** | Each session and proxy is used in rotation to avoid blocks and provide additional anonymity.                                                   |
| **Administrator Retrieval** | For groups and channels, it retrieves and reports administrators to maximize the impact of the report.                                            |
| **Entity Differentiation**  | Adapts the reporting logic depending on whether the target is a channel, group, or user. It retrieves additional details if it is a group or channel. |
| **Error Handling and Delays** | Controls Flood Wait errors by applying appropriate delays to avoid temporary account restrictions by Telegram.                                 |

## 📝 Notes

- ⚠️ **Sessions and Proxies**: Ensure sessions and proxies are properly configured to avoid errors during reporting.
- ⏳ **Flood Wait**: Excessive reporting may result in a `Flood Wait` error, temporarily blocking the account's ability to send new reports. Adjust the delay to minimize the risk.
- 🔍 **Proxy Verification**: Not all obtained proxies are valid. The tool automatically verifies them before use to ensure functionality.


## ⚙️ Requirements

- 🐍 **Python**: 3.8+
- 📚 **Required Libraries**: 
  - `telethon`: For interaction with the Telegram API.
  - `requests`: For proxy management and verification.
  - `asyncio`: For asynchronous task execution.

## 📦 Installation

1. 🔧 **Clone this repository**:

   ```sh
   git clone https://github.com/your_user/telegram-reporter.git
   cd telegram-reporter
   ```

2. 📥 **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Usage

1. 🗂️ **Place sessions in the `vars.txt` file**.
   - This file must contain the sessions serialized using `pickle`. Each session represents a Telegram account with the necessary credentials.

2. ▶️ **Run the script**:

   ```sh
   python telegram_reporter.py
   ```

3. 📝 **Provide the requested information**:
   - During execution, you will be asked to enter links to users, groups, or channels you wish to report, the number of reports, and the delay between each one.


## 🛠️ Contributions

💡 Contributions are welcome! If you have ideas to improve the tool or find any bugs, please open an *issue* or send a *pull request*. Together we can make Telegram Reporter more efficient and robust.

## 📄 License

📝 This project is licensed under the MIT License.
