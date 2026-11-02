"""Monthly report exports for staff."""
import subprocess


def export_report(name: str) -> int:
    """Zip the reports folder as <name>.zip. Returns the exit code."""
    return subprocess.run(f"zip -r {name}.zip reports", shell=True).returncode
