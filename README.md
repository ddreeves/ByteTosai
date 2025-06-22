# 🔐 failed\_login\_check.py

`failed_login_check.py` is a simple Python script designed to parse system log files and summarize failed login attempts by user. It's particularly useful for system administrators and security engineers who want a quick way to identify brute-force login attempts or unauthorized access activity in authentication logs.

---

## 🧠 Features

* Parses log files to extract failed login attempts.
* Uses regular expressions to identify entries like `LOGIN FAILED for user: <username>`.
* Aggregates and summarizes the number of failed attempts per user.
* Easy to run, with minimal dependencies.

---

## 📂 How It Works

1. The script reads a specified log file (default: `auth.log`).
2. It searches each line for failed login patterns.
3. It counts the number of times each user failed to log in.
4. Finally, it prints a summary of failed login attempts per user.

---

## 🚀 Usage

### ✅ Prerequisites

* Python 3.x
* A readable system log file that contains lines matching this format:

  ```
  LOGIN FAILED for user: <username>
  ```

### 🛠 Running the Script

1. Save the script as `failed_login_check.py`
2. Place your log file (e.g., `auth.log`) in the same directory or provide a full path.
3. Run the script:

```bash
python3 failed_login_check.py
```

> 🔧 If your log file has a different name or location, modify the `log_file` variable in the script:

```python
log_file = "/path/to/your/logfile.log"
```

---

## 📄 Example Output

```
--- Failed Login Attempts Summary ---
User: alice - Failed Attempts: 5
User: bob - Failed Attempts: 2
User: root - Failed Attempts: 1
```

---

## 🔍 Use Cases

* **Security monitoring:** Detect suspicious login behavior.
* **Incident response:** Quickly identify targeted accounts.
* **Audit readiness:** Provide data for failed authentication reviews.

---

## 📌 Notes

* This script assumes log lines follow a specific format. You may need to modify the regex pattern to match your system's log format.
* Extend the script for additional features such as:

  * Time-based filtering
  * IP address tracking
  * Exporting to CSV or JSON

---

## 📬 Contributions

Feel free to fork, enhance, and submit pull requests. If you have any suggestions or find a bug, open an issue!

---

## 📜 License

This project is licensed under the MIT License.
