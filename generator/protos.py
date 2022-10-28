import logging
import subprocess
from pathlib import Path
from typing import Generator

logger = logging.getLogger("gen-protos")

# https://github.com/SocialSisterYi/bilibili-API-collect/tree/master/grpc_api
PB_PATH = Path("protos/grpc_api")

INTERNAL = Path("bilibiliq/internal")
PB_OUT = INTERNAL / "pb"
GRPC_OUT = INTERNAL / "grpc"


def _parse_subprocess_stdout(
    process: subprocess.Popen,
) -> Generator[str, None, None]:
    line: bytes
    with process.stdout:  # type: ignore
        for line in iter(process.stdout.readline, b''):  # type: ignore
            if not line:
                continue
            yield line.decode("utf-8").strip()
    process.wait()


def _log_grpc(process: subprocess.Popen):
    for msg in _parse_subprocess_stdout(process):
        if "is not defined." in msg:
            logger.warning(f"grpc: {msg}")
        else:
            logger.info(f"grpc: {msg}")


def generate_py_files(file: Path) -> None:
    generated_file = Path("/".join(file.parts[2:]))
    [i.mkdir(parents=True, exist_ok=True) for i in (PB_OUT, GRPC_OUT)]

    logger.info(f"Generating {file} to {GRPC_OUT/generated_file.parent}")
    process = subprocess.Popen(
        [
            "python",
            "-m",
            "grpc_tools.protoc",
            "-I=.",
            f"--python_out=../../{PB_OUT}",
            f"--grpc_python_out=../../{GRPC_OUT}",
            f"--mypy_out=../../{PB_OUT}",
            str(generated_file),
        ],
        cwd=PB_PATH,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    _log_grpc(process)
    logger.info(f"Generated {GRPC_OUT/generated_file.parent}")


def change_import(file: Path) -> None:
    type_ = "grpc" if file.stem.endswith("_grpc.py") else "pb"
    logger.info(f"Changing the imports of the file {file}")
    with open(file, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith("from bilibili."):
                changed_import = line.replace(
                    "from bilibili.",
                    f"from bilibiliq.internal.{type_}.bilibili.",
                )
                lines[i] = changed_import
                logger.info(f"{line} -> {changed_import}")
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(lines)
    logger.info(f"Changed {file}")


def run_formatting(cmd: str) -> None:
    process = subprocess.Popen(
        ["python", "-m", cmd, str(INTERNAL)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    for msg in _parse_subprocess_stdout(process):
        logger.info(f"{cmd}: {msg}")


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    for file in PB_PATH.rglob("*.proto"):
        generate_py_files(file)
    for files in (PB_OUT.rglob("*.py"), GRPC_OUT.rglob("*.py")):
        for file in files:
            change_import(file)

    logger.info("Run isort and black")
    run_formatting("isort")
    run_formatting("black")

    logger.info("All done!")
