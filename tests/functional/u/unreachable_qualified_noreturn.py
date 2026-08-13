"""Calls to functions annotated with a qualified never-returning type."""
# pylint: disable=missing-function-docstring
import typing


def terminate() -> typing.NoReturn:
    raise SystemExit(1)


def func1():
    terminate()
    print("unreachable")  # [unreachable]
