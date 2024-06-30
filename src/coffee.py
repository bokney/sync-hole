import time, asyncio
from sprint import sprint, wait

async def brew_coffee():
    sprint("> brewing coffee")
    await asyncio.sleep(3)
    sprint("> brewing complete")
    return "coffee is ready"

async def toast_crumpet():
    sprint("> toasting crumpet")
    await asyncio.sleep(2)
    sprint("> toasting complete")
    return "crumpet is ready"

async def main():
    start_time = time.time()

    # batch = asyncio.gather(brew_coffee(), toast_crumpet())
    # coffee, crumpet = await batch
    make_coffee = asyncio.create_task(brew_coffee())
    make_crumpet = asyncio.create_task(toast_crumpet())

    coffee = await make_coffee
    crumpet = await make_crumpet

    end_time = time.time()
    total_time = end_time - start_time
    sprint(f"{coffee} and {crumpet}")
    sprint(f"Breakfast took {total_time} seconds to make")

if __name__ == "__main__":
    asyncio.run(main())