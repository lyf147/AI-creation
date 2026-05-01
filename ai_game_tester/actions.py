import random

async def random_action(page):
    actions = ["click", "type", "scroll"]
    action = random.choice(actions)

    try:
        if action == "click":
            await page.mouse.click(
                random.randint(0, 800),
                random.randint(0, 600)
            )
            return {"action": "click"}

        elif action == "type":
            await page.keyboard.type("test")
            return {"action": "type"}

        elif action == "scroll":
            await page.mouse.wheel(0, random.randint(100, 500))
            return {"action": "scroll"}

    except Exception as e:
        return {"action": action, "error": str(e)}
