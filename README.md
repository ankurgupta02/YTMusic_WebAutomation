## 📖 Framework Description & Execution Flow

`YTMusic_WebAutomation` is a Selenium-based test automation framework designed specifically for automating and validating user interactions on [music.youtube.com](https://music.youtube.com). The primary goal is to test the **music playback experience**, including login flow, home page shelf funtionalities, video readiness, ad skipping, and control buttons like play, pause, next, and previous.

The framework covers:

- **Login flow validation**
- **Home page shelf - Randomly choose a video at run time and perform actions**
- **Video playback control**
- **Ad wait handling**
- **Playlist queue navigation**
- **Dynamic waits and JavaScript execution**
- **Logging, screenshot capture, and test reporting**

---

### 🧭 End-to-End Test Flow

Here's how the typical test flow works inside this automation suite:

---

#### 1. **Test Initialization**
- Pytest discovers tests from the `testcases/` directory.
- `conftest.py` sets up WebDriver, browser configuration, and fixtures.
- The test picks configurations like `base_url` or `credentials` from `configurations/config.ini`.

---

#### 2. **Page Interaction (Page Object Model)**

All UI interactions are handled using the **Page Object Model (POM)** in the `pages/` package.

- Locators are managed in `locators.py`.
- Static text or UI labels are stored in `elements.py`.

Each page class (like `home_page.py`, `player_page.py`, `login_page.py`) abstracts functionality such as:

- Clicking player controls (play, pause, next, previous)
- Fetching the currently playing video title
- Waiting for video readiness (`readyState >= 4`)
- Handling YouTube ads
- Scrolling or interacting with dynamic UI elements

---

#### 3. **Test Execution Flow (Example - Player Controls)**

**From `test_player_page.py`:**

1. **Open browser and navigate to music.youtube.com**
2. **Wait for the video to become ready (buffered and interactive)**
3. **Click "Play" → Auto-handle ads → Capture current title**
4. **Click "Next" → Wait → Click "Previous"**
5. **Capture new title → Assert that it matches the expected "previous" video**

---

#### 4. **Utilities**

The `utilities/` folder contains reusable helper functions like:

- Logger setup
- Explicit wait utilities
- Scroll/JavaScript helpers

---

#### 5. **Logging & Reports**

- All logs are saved in `logs/automation.log` using a custom logger.
- HTML report of each test run is generated under `reports/report.html`.
- Screenshots for failed steps (if implemented) are stored in `screenshots/`.

---
