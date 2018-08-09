# -*- coding: utf-8 -*-
"""Dialog module."""
from typing import ClassVar

import attr

from .connection import CDPSession

__all__ = ["Dialog"]


@attr.dataclass(slots=True)
class DialogType(object):
    Alert: str = attr.ib(default="alert")
    BeforeUnload: str = attr.ib(default="beforeunload")
    Confirm: str = attr.ib(default="confirm")
    Prompt: str = attr.ib(default="prompt")


@attr.dataclass
class Dialog(object):
    """Dialog class.

    Dialog objects are dispatched by page via the ``dialog`` event.
    """

    client: CDPSession = attr.ib(repr=False)
    type: str = attr.ib()
    message: str = attr.ib()
    defaultValue: str = attr.ib(default="")
    handled: str = attr.ib(default=False)
    Type: ClassVar[DialogType] = DialogType()

    async def accept(self, promptText: str = "") -> None:
        """Accept the dialog.

        * ``promptText`` (str): A text to enter in prompt. If the dialog's type
          is not prompt, this does not cause any effect.
        """
        self.handled = True
        await self.client.send(
            "Page.handleJavaScriptDialog", {"accept": True, "promptText": promptText}
        )

    async def dismiss(self) -> None:
        """Dismiss the dialog."""
        self.handled = True
        await self.client.send("Page.handleJavaScriptDialog", {"accept": False})
