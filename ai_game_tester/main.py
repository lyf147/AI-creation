import asyncio
from agent import GameTestAgent

GAME_URL = "https://example.com"

async def main():
    agent = GameTestAgent(GAME_URL)
    await agent.run(test_steps=50)

if __name__ == "__main__":
    asyncio.run(main())
