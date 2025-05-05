import asyncio
from mcpcli.__main__ import main

async def run_main():
    config_path = "./server_config.json"
    server_names = ["git"]
    await main(config_path, server_names)

if __name__ == "__main__":
    asyncio.run(run_main())

