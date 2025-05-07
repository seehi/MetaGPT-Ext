import asyncio
from pathlib import Path

from metagpt.rag.engines import SimpleEngine
from metagpt.rag.schema import LLMRankerConfig


async def main():
    DOC_PATH = Path(__file__).parent / "data" / "simple.txt"
    engine = SimpleEngine.from_docs(input_files=[DOC_PATH], ranker_configs=[LLMRankerConfig()])
    answer = await engine.aquery("What does Bob like?")
    print(answer)

if __name__ == "__main__":
    asyncio.run(main())
