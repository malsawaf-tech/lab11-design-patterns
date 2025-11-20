"""Replaces the PII text entity with initials"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    """Replace old PII text entity with initials."""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """Return initials for the given text."""
        if not text:
            return ""

        parts = [p for p in text.split() if p]
        initials = [f"{p[0].upper()}." for p in parts]
        return " ".join(initials)

    def validate(self, params: Dict = None) -> None:
        """No parameters required for initials operator."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize
