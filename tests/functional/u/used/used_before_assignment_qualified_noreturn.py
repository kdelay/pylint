"""Never-returning functions can be annotated with a qualified name."""
# pylint: disable=missing-class-docstring, missing-function-docstring, too-few-public-methods
import typing


def terminate(msg) -> typing.NoReturn:
    raise SystemExit(msg)


def qualified_noreturn_in_else(flag):
    if flag:
        cmd = "ls"
    else:
        terminate("unsupported")
    return cmd


class PlatformChecks:
    def skip(self, msg) -> typing.NoReturn:
        raise SystemExit(msg)

    def print_platform_specific_command(self, flag):
        if flag:
            cmd = "ls"
        else:
            self.skip("only runs on Linux")
        print(cmd)
