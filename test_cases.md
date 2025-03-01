# DemoQA Login Page - Manual Test Cases (51 Scenarios)

## **Functional Testing**

| TC ID | Scenario                   | Steps                                                                                     | Expected Result                             | Status    |
| ----- | -------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------- | --------- |
| 1     | Valid Login                | 1. Go to https://demoqa.com/login<br>2. Enter valid username/password<br>3. Click "Login" | Redirects to profile page                   | Pass/Fail |
| 2     | Invalid Username           | 1. Enter invalid username + valid password<br>2. Click "Login"                            | Error: "Invalid username or password"       | Pass/Fail |
| 3     | Invalid Password           | 1. Enter valid username + invalid password<br>2. Click "Login"                            | Error: "Invalid username or password"       | Pass/Fail |
| 4     | Empty Username             | 1. Leave username blank + enter password<br>2. Click "Login"                              | Error: "Username is required"               | Pass/Fail |
| 5     | Empty Password             | 1. Enter username + leave password blank<br>2. Click "Login"                              | Error: "Password is required"               | Pass/Fail |
| 6     | Case-Sensitive Username    | 1. Enter valid username in UPPERCASE<br>2. Enter password<br>3. Click "Login"             | Login succeeds (if case-insensitive)        | Pass/Fail |
| 7     | SQL Injection in Username  | 1. Enter `admin' --` as username<br>2. Enter any password                                 | Error: Sanitized input or login failure     | Pass/Fail |
| 8     | XSS Attack in Password     | 1. Enter `<script>alert('test')</script>` as password                                     | Error: Input sanitized, no script execution | Pass/Fail |
| 9     | Forgot Password Link       | 1. Click "Forgot Password"                                                                | Redirects to password reset page            | Pass/Fail |
| 10    | Login After Password Reset | 1. Reset password<br>2. Login with new credentials                                        | Login succeeds                              | Pass/Fail |

## **Usability Testing**

| TC ID | Scenario              | Steps                                                   | Expected Result                                       | Status    |
| ----- | --------------------- | ------------------------------------------------------- | ----------------------------------------------------- | --------- |
| 11    | UI Alignment          | 1. Check alignment of login form elements               | All elements centered and aligned                     | Pass/Fail |
| 12    | Mobile Responsiveness | 1. Resize browser to 360x640 pixels                     | Login form adjusts to screen size                     | Pass/Fail |
| 13    | Tab Navigation        | 1. Press Tab to navigate between fields                 | Focus moves sequentially: Username → Password → Login | Pass/Fail |
| 14    | Placeholder Text      | 1. Verify placeholder text for username/password fields | "UserName" and "Password" displayed                   | Pass/Fail |
| 15    | Error Message Clarity | 1. Trigger an error (e.g., invalid password)            | Error message is clear and visible                    | Pass/Fail |
| 16    | Page Title            | 1. Check browser tab title                              | Title: "ToolsQA"                                      | Pass/Fail |
| 17    | Accessibility Labels  | 1. Inspect input fields for ARIA labels                 | Labels exist for screen readers                       | Pass/Fail |
| 18    | Load Time             | 1. Measure page load time                               | Loads within 3 seconds                                | Pass/Fail |
| 19    | Button Hover Effects  | 1. Hover over "Login" button                            | Visual feedback (e.g., color change)                  | Pass/Fail |
| 20    | Browser Back Button   | 1. Login → Logout → Press browser back button           | Cannot return to logged-in page                       | Pass/Fail |

## **Security Testing**

| TC ID | Scenario               | Steps                                   | Expected Result                     | Status    |
| ----- | ---------------------- | --------------------------------------- | ----------------------------------- | --------- |
| 21    | Password Masking       | 1. Enter password                       | Password hidden (e.g., `•••••`)     | Pass/Fail |
| 22    | Session Timeout        | 1. Login → Wait 15 mins → Refresh page  | Session expired; redirect to login  | Pass/Fail |
| 23    | Brute Force Protection | 1. Enter wrong password 5 times         | Account locked or CAPTCHA triggered | Pass/Fail |
| 24    | HTTPS Encryption       | 1. Check URL protocol                   | Uses HTTPS (secure connection)      | Pass/Fail |
| 25    | Password Copy-Paste    | 1. Copy-paste password into field       | Password accepted                   | Pass/Fail |
| 26    | CSRF Token Check       | 1. Inspect login request headers        | CSRF token included                 | Pass/Fail |
| 27    | Input Max Length       | 1. Enter 255 characters in username     | Input truncated or rejected         | Pass/Fail |
| 28    | Password Special Chars | 1. Enter password with `!@#$%^&*()`     | Login succeeds                      | Pass/Fail |
| 29    | Browser Autocomplete   | 1. Check if browser saves password      | Autocomplete disabled               | Pass/Fail |
| 30    | HTTP Methods           | 1. Send POST request without CSRF token | Request rejected (405 error)        | Pass/Fail |

## **Compatibility Testing**

| TC ID | Scenario        | Steps                             | Expected Result           | Status    |
| ----- | --------------- | --------------------------------- | ------------------------- | --------- |
| 31    | Chrome v120     | 1. Test login on Chrome           | All features work         | Pass/Fail |
| 32    | Firefox v115    | 1. Test login on Firefox          | All features work         | Pass/Fail |
| 33    | Safari v16      | 1. Test login on Safari           | All features work         | Pass/Fail |
| 34    | Edge v120       | 1. Test login on Edge             | All features work         | Pass/Fail |
| 35    | iOS Safari      | 1. Test on iPhone 14 (iOS 16)     | Responsive and functional | Pass/Fail |
| 36    | Android Chrome  | 1. Test on Samsung Galaxy S23     | Responsive and functional | Pass/Fail |
| 37    | Tablet View     | 1. Test on iPad (1024x768)        | Form adjusts to screen    | Pass/Fail |
| 38    | High DPI Screen | 1. Test on 4K monitor             | No UI distortion          | Pass/Fail |
| 39    | Zoom In/Out     | 1. Zoom to 150% → Test login      | Form remains usable       | Pass/Fail |
| 40    | Incognito Mode  | 1. Test login in incognito window | Works as expected         | Pass/Fail |

## **Edge Cases**

| TC ID | Scenario                      | Steps                                | Expected Result                      | Status    |
| ----- | ----------------------------- | ------------------------------------ | ------------------------------------ | --------- |
| 41    | 100-Character Username        | 1. Enter username with 100 chars     | Input accepted                       | Pass/Fail |
| 42    | Leading/Trailing Spaces       | 1. Enter " user " as username        | Spaces trimmed automatically         | Pass/Fail |
| 43    | Non-ASCII Chars               | 1. Enter username: `üßër`            | Login succeeds                       | Pass/Fail |
| 44    | Password with Emoji           | 1. Enter password: `P@ss😀123`       | Login succeeds                       | Pass/Fail |
| 45    | Concurrent Logins             | 1. Login on 2 devices simultaneously | Sessions allowed or blocked          | Pass/Fail |
| 46    | Cookie Deletion Post-Login    | 1. Login → Delete cookies → Refresh  | Redirect to login page               | Pass/Fail |
| 47    | Password Toggle               | 1. Click "Show Password" icon        | Password visible in plaintext        | Pass/Fail |
| 48    | Login After Browser Crash     | 1. Login → Crash browser → Reopen    | Session restored or expired          | Pass/Fail |
| 49    | API Response Time             | 1. Measure login API response        | < 1 second                           | Pass/Fail |
| 50    | Login with Bookmarked URL     | 1. Access profile page via bookmark  | Redirect to login if unauthenticated | Pass/Fail |
| 51    | Accessibility (Screen Reader) | 1. Use NVDA/JAWS to navigate         | All elements announced correctly     | Pass/Fail |
