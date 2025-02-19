import sys
import traceback

from loguru import logger


class CustomLogger:
    _logger = logger
    _logger.remove()

    _logger.add(
        sys.stderr,
        format="<blue>[{time:DD.MM.YY / HH:mm:ss}]</blue> <green>({level})</green> <green>{message}</green>",
        colorize=True,
        level="INFO",
        filter=lambda record: record["level"].name == "INFO",
    )
    _logger.add(
        sys.stderr,
        format="<blue>[{time:DD.MM.YY / HH:mm:ss}]</blue> <yellow>({level})</yellow> <yellow>{message}</yellow>",
        colorize=True,
        level="WARNING",
        filter=lambda record: record["level"].name == "WARNING",
    )
    _logger.add(
        sys.stderr,
        format=(
            "<blue>[{time:DD.MM.YY / HH:mm:ss}]</blue> <red>({level})</red> <red>{message}</red>\n"
            "<red>╰─> {extra[traceback]}</red>"
        ),
        colorize=True,
        level="ERROR",
        filter=lambda record: record["level"].name == "ERROR",
    )

    @classmethod
    def info(cls, message, module: str = None):
        log_message = f"[{module}] {message}" if module else str(message)
        cls._logger.info(log_message)

    @classmethod
    def warning(cls, message, module: str = None):
        log_message = f"[{module}] {message}" if module else str(message)
        cls._logger.warning(log_message)

    @classmethod
    def error(cls, message, module: str = None, error: Exception = None):
        if error:
            tb = traceback.format_exc()
            log_message = f"[{module}] {message}" if module else str(message)
            cls._logger.bind(traceback=tb).error(log_message)
        else:
            log_message = f"[{module}] {message}" if module else str(message)
            cls._logger.error(log_message)

log = CustomLogger()
