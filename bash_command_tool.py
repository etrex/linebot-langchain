from langchain.tools import BaseTool
from langchain.agents import AgentType
from typing import Optional, Type
from pydantic import BaseModel, Field
import subprocess


class BashCommandInput(BaseModel):
    """Input for Bash command execution."""

    command: str = Field(...,
                         description="Bash command to execute")


class BashCommandTool(BaseTool):
    name = "execute_bash_command"
    description = "Useful for when you need to execute a bash command."

    def _run(self, command: str):
        print("\n\n\n正在執行命令：" + command + " ...")
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check if the command was successful
        if result.returncode != 0:
            print("執行錯誤：")
            print(result.stderr.decode())
            return None

        command_response = result.stdout.decode()
        print("\n命令的輸出是：\n" + command_response)

        return command_response

    def _arun(self, command: str):
        raise NotImplementedError("This tool does not support async")

    args_schema: Optional[Type[BaseModel]] = BashCommandInput
