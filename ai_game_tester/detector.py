async def detect_issues(page):
    issues = []

    content = await page.content()

    if "error" in content.lower():
        issues.append("ERROR_TEXT")

    try:
        await page.evaluate("1 + 1")
    except:
        issues.append("CRASH")

    return issues
