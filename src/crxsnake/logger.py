import sys
from loguru import logger


logger.remove(0)
logger.add(
    sys.stderr,
    format="<blue>[{time:HH:mm:ss}]</blue> <yellow>({level})</yellow> <red>|→</red> <green>{message}</green>",
    colorize=True,
    level="INFO",
    filter=lambda record: record["level"].name == "INFO",
)

logger.add(
    sys.stderr,
    format="<blue>[{time:HH:mm:ss}]</blue> <yellow>({level})</yellow> |> <yellow>{message}</yellow>",
    colorize=True,
    level="WARNING",
    filter=lambda record: record["level"].name == "WARNING",
)

logger.add(
    sys.stderr,
    format="<blue>[{time:HH:mm:ss}]</blue> <red>({level})|→ {message}</red>",
    colorize=True,
    level="ERROR",
    filter=lambda record: record["level"].name == "ERROR",
)
