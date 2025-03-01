# DemoQA Login Page - Sample Bug Reports

---

## **Bug 1: Login Fails with Valid Credentials**
**Title**: Valid credentials result in "Invalid username or password" error  
**Description**: Users cannot log in even with correct credentials.  
**Steps to Reproduce**:  
1. Navigate to `https://demoqa.com/login`.  
2. Enter valid username (e.g., `test_user`).  
3. Enter valid password (e.g., `P@ssw0rd123`).  
4. Click "Login".  
**Expected Result**: Redirect to profile page (`/profile`).  
**Actual Result**: Error message: "Invalid username or password".  
**Environment**:  
- Browser: Chrome v120, Windows 11  
- Device: Desktop  
**Severity**: High  
**Priority**: Critical  
**Attachments**: [Screenshot of error message]  

---

## **Bug 2: Password Field Accepts 500+ Characters**  
**Title**: No input validation for password length  
**Description**: Password field allows excessively long input (500+ characters), violating security best practices.  
**Steps to Reproduce**:  
1. Go to `https://demoqa.com/login`.  
2. Paste 500+ characters into the password field.  
3. Click "Login".  
**Expected Result**: Password length restricted to 50 characters.  
**Actual Result**: Password field accepts 500+ characters.  
**Environment**:  
- Browser: Firefox v115, macOS Ventura  
**Severity**: Medium  
**Priority**: Low  
**Attachments**: [Video of input]  

---

## **Bug 3: UI Misalignment on Mobile View**  
**Title**: Login form elements overflow on mobile screens  
**Description**: On mobile devices, the login form elements (username/password fields) overflow the screen.  
**Steps to Reproduce**:  
1. Open `https://demoqa.com/login` on an iPhone 14 (375x812 resolution).  
2. Observe the login form layout.  
**Expected Result**: Responsive design with properly aligned elements.  
**Actual Result**: Username field is cut off on the right side.  
**Environment**:  
- Device: iPhone 14, iOS 16  
- Browser: Safari  
**Severity**: Low  
**Priority**: Medium  
**Attachments**: [Screenshot]  

---

## **Bug 4: Missing Error Message for SQL Injection Attempt**  
**Title**: No sanitization for SQL injection in username field  
**Description**: Entering `admin' --` as the username does not trigger an error message.  
**Steps to Reproduce**:  
1. Go to `https://demoqa.com/login`.  
2. Enter `admin' --` in the username field.  
3. Enter any password.  
4. Click "Login".  
**Expected Result**: Error: "Invalid input detected".  
**Actual Result**: Generic error: "Invalid username or password".  
**Environment**:  
- Browser: Edge v120, Windows 11  
**Severity**: High (Security Risk)  
**Priority**: High  
**Attachments**: [Network request logs]  

---

## **Bug 5: Session Persists After Logout**  
**Title**: User remains logged in after clicking "Logout"  
**Description**: Clicking "Logout" does not invalidate the session.  
**Steps to Reproduce**:  
1. Log in with valid credentials.  
2. Click "Logout".  
3. Press the browser’s back button.  
**Expected Result**: Redirect to login page.  
**Actual Result**: User remains on the profile page.  
**Environment**:  
- Browser: Chrome v120, Android 13  
**Severity**: Medium  
**Priority**: Medium  
**Attachments**: [Screen recording]  

---

## **Bug 6: Accessibility Issue - Missing Alt Text for Logo**  
**Title**: Logo image lacks `alt` text for screen readers  
**Description**: The DemoQA logo image has no `alt` attribute, failing accessibility standards.  
**Steps to Reproduce**:  
1. Open `https://demoqa.com/login`.  
2. Inspect the logo image element.  
**Expected Result**: `alt="DemoQA Logo"` present.  
**Actual Result**: No `alt` text provided.  
**Environment**:  
- Browser: Chrome v120, NVDA screen reader  
**Severity**: Low  
**Priority**: Low  
**Attachments**: [HTML snippet]  

---

## **Bug 7: Case-Sensitive Username**  
**Title**: Login fails with uppercase username (e.g., `TEST_USER`)  
**Description**: Usernames are case-sensitive, causing confusion for users.  
**Steps to Reproduce**:  
1. Register with username `test_user`.  
2. Try logging in with `TEST_USER`.  
3. Enter valid password.  
**Expected Result**: Login succeeds (case-insensitive).  
**Actual Result**: Error: "Invalid username or password".  
**Environment**:  
- Browser: Safari v16, macOS  
**Severity**: Medium  
**Priority**: Medium  

---

# How to Use These Templates:
1. **Customize**: Replace steps/results with your actual findings.  
2. **Add Evidence**: Attach screenshots, videos, or logs.  
3. **Prioritize**: Use severity levels (Critical/High/Medium/Low).  
4. **Track**: Use tools like Jira, Trello, or Excel to manage bugs.  

Let me know if you’d like more examples or a specific type of bug! 😊  