# Defect Report — Day 02

## BUG-001: Error message not cleared when user starts retyping

**Severity:** Low  
**Priority:** Medium  
**Status:** Open  
**Reported by:** Hrithika  
**Date:** 31-05-2026  

### Environment
- URL: https://the-internet.herokuapp.com/login
- Browser: Chrome
- OS: Windows 11

### Steps to Reproduce
1. Open the login page
2. Enter wrong username and password
3. Click Login button
4. Observe the red error message
5. Start typing in the username field again

### Expected Result
Error message should disappear when user starts correcting input

### Actual Result
Error message stays visible while user is typing

### Impact
Confusing user experience — user sees error even while fixing it